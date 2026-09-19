# Security Policy

Universal Prompt System is a declarative prompt repository, not an executable service. It does not itself accept credentials, issue tokens, or provide a production API.

## Reporting a vulnerability

Do not publish secrets, personal data, exploit details, or sensitive exports in a public issue. Contact the repository maintainer through the private reporting channel configured by the repository owner. If no private channel is configured, report only a minimal, non-sensitive description and wait for maintainer guidance before sharing details.

## Sensitive data

Never commit API keys, passwords, access tokens, private URLs, `.env` files, personal exports, or real user project state. Use the repository `.gitignore` and review `git status` before any commit.

