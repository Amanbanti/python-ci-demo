# Python CI Demo

[![CI](https://github.com/your-username/python-ci-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/python-ci-demo/actions/workflows/ci.yml)

Simple DevOps demo: linting + testing + Docker build/push + deployment with GitHub Actions.

## Local app run

Install dependencies and start the API:

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

Example endpoint:

- `http://localhost:8000/add/5/3`

## Docker

Build and run locally:

```bash
docker build -t calc-api .
docker run -p 8000:8000 calc-api
```

## CI/CD workflow

Workflow file: `.github/workflows/ci.yml`

- `lint-and-test`: runs `ruff` and `pytest` for Python `3.9` to `3.12`
- `build-and-push`: builds Docker image and pushes to GHCR on pushes to `main`
- `deploy`: optional VPS deployment over SSH (runs only if VPS secrets are set)
- `deploy-to-render`: optional Render deploy hook trigger (runs only if hook secret is set)

## Required GitHub secrets

For VPS deploy (Option A):

- `DEPLOY_HOST`
- `DEPLOY_USER`
- `DEPLOY_SSH_KEY`

For Render deploy hook (Option B):

- `RENDER_DEPLOY_HOOK`

GHCR push uses built-in `${{ secrets.GITHUB_TOKEN }}`.
