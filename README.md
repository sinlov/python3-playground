[![python-pipenv](https://github.com/sinlov/python3-playground/workflows/python-pipenv/badge.svg?branch=main)](https://github.com/sinlov/python3-playground/actions/workflows/python-pipenv.yml)

# this is python3 playground

- repo: [https://github.com/sinlov/python3-playground](https://github.com/sinlov/python3-playground)

## env

- run on [python pipenv](https://pypi.org/project/pipenv/) 

## dev

```bash
$ pipenv install --three --skip-lock
$ pipenv lock
# or use proxy
$ pipenv lock --pypi-mirror https://pypi.tuna.tsinghua.edu.cn/simple
# just into shell
$ pipenv shell
```

### want proxy of pipenv

```bash
# proxy tsinghua
$ echo PIPENV_PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/ >.env
# or aliyun
$ echo PIPENV_PYPI_MIRROR=https://mirrors.aliyun.com/pypi/simple/ >.env
```

just make file `.env` at root of project

```env
PIPENV_PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/
PIP_DEFAULT_TIMEOUT=300
PIPENV_IGNORE_VIRTUALENVS=-1
```
base as
```bash
echo -e 'PIPENV_PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/
PIP_DEFAULT_TIMEOUT=300
PIPENV_IGNORE_VIRTUALENVS=-1' \
 >.env
```

### Pipenv use

- at `Pipfile` file

```Pipfile
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[scripts]
main = "python main.py"
test_main = "python -m unittest discover"

[packages]
requests = "*"
urllib3 = ">=1.26.5"
Pygments = ">=2.7.4"

[dev-packages]
httpie = "*"
faker = ">=8"

[requires]
python_version = "3.9.5"
```

### simple run main

- code at [main.py](main.py)

```bash
$ pipenv run main
```

### simple test run

- code at [tests/test_main.py](tests/test_main.py)

```bash
$ pipenv run test_main
```