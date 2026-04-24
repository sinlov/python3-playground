## env

- run on [python uv](https://docs.astral.sh/uv/) as version `0.9.2`
- python version now under `.venv` directory
- style check by [ruff](https://github.com/charliermarsh/ruff)

## dev

```bash
# show help
$ make help

# check env
$ make env

# install dependencies
$ make dep

# run ci pipeline
$ make ci

# fix code style
$ make style

# check style
$ make check
```

## test

### run all test

```bash
$ make test
```