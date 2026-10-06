# Contribution Guidelines

Please follow the [Code of Conduct](code-of-conduct.md) when participating in this project.

## Adding or updating a tool

- Add the tool under the most relevant existing section in `README.md`.
- Use an HTTPS link to the tool's public GitHub repository and a short, factual description.
- Check that the repository exists, has at least 50 stars, and is not already listed.
- Keep the existing Markdown list format. Update the table of contents only when you add, remove, or rename a heading.

The pull request workflow checks new README links for valid GitHub repositories, duplicate entries, and the 50-star minimum. Non-GitHub links are rejected.

## Before opening a pull request

Run the offline regression tests:

```sh
python3 -m unittest discover -s .github/scripts -p 'test_extract_added_urls.py'
```

Then review the pull request checklist and describe the change clearly.
