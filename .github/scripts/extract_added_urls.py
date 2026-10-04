"""Extract every HTTP(S) URL on added lines of a unified Git diff."""

import re
import sys


URL_PATTERN = re.compile(r"https?://[^\s<>()\"']+", re.IGNORECASE)


def extract_added_urls(diff: str) -> list[str]:
    urls = set()
    in_hunk = False
    for line in diff.splitlines():
        if line.startswith("diff --git "):
            in_hunk = False
        elif line.startswith("@@ "):
            in_hunk = True
        elif in_hunk and line.startswith("+"):
            urls.update(URL_PATTERN.findall(line[1:]))
    return sorted(urls)


if __name__ == "__main__":
    for url in extract_added_urls(sys.stdin.read()):
        print(url)
