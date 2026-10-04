"""Offline regression tests for the Stargazers workflow's diff extraction."""

import subprocess
import sys
import unittest
from pathlib import Path

from extract_added_urls import extract_added_urls


HEADER = """diff --git a/README.md b/README.md
--- a/README.md
+++ b/README.md
@@ -1 +1 @@
"""


class ExtractAddedUrlsTests(unittest.TestCase):
    def test_single_markdown_link(self):
        self.assertEqual(
            extract_added_urls(HEADER + "+[tool](https://github.com/example/tool)\n"),
            ["https://github.com/example/tool"],
        )

    def test_multiple_links_on_one_line(self):
        self.assertEqual(
            extract_added_urls(
                HEADER
                + "+[first](https://github.com/example/first) "
                + "[second](https://github.com/example/second)\n"
            ),
            ["https://github.com/example/first", "https://github.com/example/second"],
        )

    def test_non_github_link_cannot_hide_before_github_link(self):
        self.assertEqual(
            extract_added_urls(
                HEADER
                + "+[external](https://example.invalid/tool) "
                + "[tool](https://github.com/example/tool)\n"
            ),
            ["https://example.invalid/tool", "https://github.com/example/tool"],
        )

    def test_http_and_case_variant_schemes_are_not_silently_skipped(self):
        self.assertEqual(
            extract_added_urls(
                HEADER + "+http://example.invalid/tool HTTPS://example.invalid/other\n"
            ),
            ["HTTPS://example.invalid/other", "http://example.invalid/tool"],
        )

    def test_removed_and_context_lines_are_ignored(self):
        self.assertEqual(
            extract_added_urls(
                HEADER
                + "-https://example.invalid/removed\n"
                + " https://example.invalid/context\n"
                + "+https://github.com/example/tool\n"
            ),
            ["https://github.com/example/tool"],
        )

    def test_diff_metadata_is_ignored(self):
        self.assertEqual(
            extract_added_urls(
                "diff --git a/old.md b/https://example.invalid/metadata\n"
                "--- a/old.md\n"
                "+++ b/https://example.invalid/metadata\n"
                "@@ -1 +1 @@ https://example.invalid/heading\n"
                "+https://github.com/example/tool\n"
                "diff --git a/other.md b/other.md\n"
                "+++ b/https://example.invalid/another-header\n"
            ),
            ["https://github.com/example/tool"],
        )

    def test_urls_are_sorted_and_deduplicated(self):
        self.assertEqual(
            extract_added_urls(
                HEADER
                + "+https://github.com/example/z\n"
                + "+https://github.com/example/a https://github.com/example/z\n"
            ),
            ["https://github.com/example/a", "https://github.com/example/z"],
        )

    def test_autolinks_tabs_and_markdown_titles(self):
        self.assertEqual(
            extract_added_urls(
                HEADER
                + '+<https://github.com/example/a>\t'
                + '[tool](https://github.com/example/b "title")\n'
            ),
            ["https://github.com/example/a", "https://github.com/example/b"],
        )

    def test_added_content_starting_with_plus_signs_is_not_metadata(self):
        self.assertEqual(
            extract_added_urls(HEADER + "++++ https://github.com/example/tool\n"),
            ["https://github.com/example/tool"],
        )

    def test_empty_or_link_free_diff(self):
        for diff in ("", HEADER + "+no links\n", HEADER + "-https://example.invalid/old\n"):
            with self.subTest(diff=diff):
                self.assertEqual(extract_added_urls(diff), [])

    def test_cli_reads_stdin_and_prints_one_url_per_line(self):
        script = Path(__file__).with_name("extract_added_urls.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            input=HEADER + "+https://github.com/example/b https://github.com/example/a\n",
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertEqual(
            result.stdout,
            "https://github.com/example/a\nhttps://github.com/example/b\n",
        )
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
