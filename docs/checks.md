
# CI Checks — Lab 04

## API CI

Repository: https://github.com/sarccasm/wishlist-api

Workflow: `.github/workflows/ci.yml`

The API workflow runs on pushes and pull requests.

### Checks
- Python 3.11 environment setup
- Dependency installation
- Ruff linting
- Pytest tests
- PostgreSQL 15 service
- Redis 7 service

### Results
- Initial CI runs failed due to Ruff E722 and Python module import errors.
- The issues were fixed in subsequent commits.
- Final CI run passed successfully.

## UI CI

Repository: https://github.com/sarccasm/wishlist-ui

Workflow: `.github/workflows/ci.yml`

The UI workflow checks the frontend build and code quality.

### Results
- UI CI completed successfully.
- The pull request was merged into `main`.

## Branch Protection

Both repositories have a `Protect main` ruleset.

Required checks:
- API: `lint-and-test`
- UI: `lint-and-build`

Pull requests and successful CI checks are required before merging.

## Environment

The API CI uses PostgreSQL and Redis services provided by GitHub Actions.

Local Docker execution was not performed because hardware virtualization was disabled.
