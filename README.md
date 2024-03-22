[![ci](https://github.com/sinlov/python3-playground/actions/workflows/ci.yml/badge.svg)](https://github.com/sinlov/python3-playground/actions/workflows/ci.yml)

[![GitHub license](https://img.shields.io/github/license/sinlov/python3-playground)](https://github.com/sinlov/python3-playground)
[![GitHub latest SemVer tag)](https://img.shields.io/github/v/tag/sinlov/python3-playground)](https://github.com/sinlov/python3-playground/tags)
[![GitHub release)](https://img.shields.io/github/v/release/sinlov/python3-playground)](https://github.com/sinlov/python3-playground/releases)

# this is python3 playground

- repo: [https://github.com/sinlov/python3-playground](https://github.com/sinlov/python3-playground)

## env

- run on [python-poetry.org](https://python-poetry.org/docs/)
- now under `pyenv shell 3.11.7`

### Warning

- this project use [gevent](https://www.gevent.org/), but `gevent` [not support windows 10 x64](https://github.com/gevent/gevent/issues/1918)

```bash

### poetry 使用镜像源

- see [https://python-poetry.org/docs/repositories/#disabling-the-pypi-repository](https://python-poetry.org/docs/repositories/#disabling-the-pypi-repository)

```bash
poetry source add --default aliyun https://mirrors.aliyun.com/pypi/simple
poetry source add --default tuna https://pypi.tuna.tsinghua.edu.cn/simple/
# 设置私有源
poetry source add --priority=PRIORITY [name] [url]
```

## dev

```bash
# show help
$ make help

# check env
$ make env

# install dependencies
$ make dep
```

## test

### run all test

```bash
$ make test
```

### simple test run

- code at [tests/test_main.py](tests/test_main.py)

```bash
$ poetry run python -m unittest tests/test_main.py
```