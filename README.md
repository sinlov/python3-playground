[![python-pipenv](https://github.com/sinlov/python3-playground/workflows/python-pipenv/badge.svg?branch=main)](https://github.com/sinlov/python3-playground/actions/workflows/python-pipenv.yml)

# this is python3 playground

- repo: [https://github.com/sinlov/python3-playground](https://github.com/sinlov/python3-playground)

## env

- run on [python pipenv](https://pypi.org/project/pipenv/) 

## dev

```bash
pipenv install --three
```

### want proxy of pipenv

just make file `.env` at root of project

```env
PIPENV_PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/
```

### simple test run

- code at [tests/test_main.py](tests/test_main.py)

```bash
$ pipenv run test_main
```