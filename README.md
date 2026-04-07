# python-ci-demo

Simple Python project with linting (`ruff`), tests (`pytest`), and GitHub Actions CI.

## Local setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ruff check calc.py test_calc.py
pytest -v
```
