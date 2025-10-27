# each tag change this
ENV_DIST_VERSION := 1.0.0

ENV_PROJECT_NAME ?=python3-playground

ENV_CHECK_FILES=src/ tests/
ENV_BLACK_OPTS=
ENV_PYTHON_ENV_VERSION =3.11.7
py_warn =PYTHONDEVMODE=1

ifeq ($(OS),Windows_NT)
 PLATFORM=Windows
 # do windows
 ENV_ROOT ?= $(shell pwd)
 #py_warn = $$env:PYTHONDEVMODE=1;
 py_warn=
else
 OS_UNAME ?= $(shell echo `uname`) # Linux Darwin
 OS_BIT ?= $(shell echo `uname -m`) # x86_64 arm64
 ifeq ($(shell uname),Darwin)
  PLATFORM="MacOS"
  ifeq ($(shell echo ${OS_BIT}),arm64)
    PLATFORM="MacOS-Apple-Silicon"
  else
    PLATFORM="MacOS-Intel"
  endif
 else
  PLATFORM="Unix-Like"
 endif
 # do unix
 ENV_ROOT ?= $(shell pwd)
 py_warn=
endif
ENV_MODULE_FOLDER ?= ${ENV_ROOT}
ENV_MODULE_MANIFEST = ${ENV_ROOT}/package.json

.PHONY: env
env:
	@echo ------- start show env ---------
	@echo ""
	@echo "ROOT_NAME                          ${ROOT_NAME}"
	@echo "PLATFORM                           ${PLATFORM}"
	@echo "ENV_ROOT                           ${ENV_ROOT}"
	@echo "ENV_MODULE_FOLDER                  ${ENV_MODULE_FOLDER}"
	@echo "ENV_MODULE_MANIFEST                ${ENV_MODULE_MANIFEST}"
	@echo ""
	@echo "- now python version is -"
	@python -V
	@echo "- this project manager by uv -"
ifeq ($(OS),Windows_NT)
	@echo ""
	@echo "windows install as:"
	@echo "-> scoop install main/uv"
	@echo ""
endif
	@echo "= if poetry install error try use"
	@echo "$$ pyenv shell ${ENV_PYTHON_ENV_VERSION}"
	@echo "or target version to fix"
	@echo "- start show uv info -"
	@uv --version
	@uv tool dir --color never
	@uv tool list --color never
	@echo ""
	@echo "- end show uv info -"

.PHONY: up
up:
	@uv sync --upgrade

.PHONY: dep
dep:
	@uv sync

.PHONY: dep.fix
dep.fix:
	@uv lock

.PHONY: dep.check
dep.check:
	$(info check: uv sync --dry-run)
	@uv sync --dry-run
	@uv lock --check

.PHONY: dep.lock
dep.lock:
	@uv lock

.PHONY: init
init: dep
	@echo "=> just init finish this project by uv"

.PHONY: style
style: dep
	@uv run ruff format $(ENV_CHECK_FILES)

.PHONY: check
check:
	@uv run ruff check $(ENV_CHECK_FILES)

.PHONY: test
test: dep
	${py_warn} uv run pytest

.PHONY: test.with.warn
test.with.warn:
	${py_warn} uv run pytest -W error::UserWarning

.PHONY: test.disable.warn
test.disable.warn:
	${py_warn} uv run pytest --disable-warnings

.PHONY: test.coverage
test.coverage:
	${py_warn} uv run pytest --cov-append --cov-report=html --cov=./

.PHONY: test.clean
test.clean:
	@$(RM) -r .pytest_cache/

.PHONY: test.coverage.clean
test.coverage.clean:
	@$(RM) .coverage
	@$(RM) .coverage.*
	@$(RM) -r htmlcov/

.PHONY: ci
ci: check test

.PHONY: build
build: dep
	@uv build

.PHONY: build.only
build.only:
	@uv build

.PHONY: publish
publish: dep
	@uv publish --build

.PHONY: shell
shell:
	@echo "-> activate uv virtual environment"
	@echo ""
	@echo "run: source .venv/bin/activate"
	@echo "or: uv run python"

.PHONY: clean.dist
clean.dist:
	@$(RM) -r dist

.PHONY: clean.logs
clean.logs:
	@$(RM) -r logs

.PHONY: clean.all
clean.all: clean.dist clean.logs test.coverage.clean test.clean
	@echo "has clean all"

.PHONY: helpProjectRoot
helpProjectRoot:
	@echo "Help: Project root Makefile"
ifeq ($(OS),Windows_NT)
	@echo ""
	@echo "warning: other install make cli tools has bug"
	@echo " run will at make tools version 4.+"
	@echo "windows use this kit must install tools blow:"
	@echo "-> scoop install main/make"
	@echo ""
endif
	@echo " module folder   path: ${ENV_MODULE_FOLDER}"
	@echo " module version    is: ${ENV_DIST_VERSION}"
	@echo " module manifest path: ${ENV_MODULE_MANIFEST}"
	@echo ""
	@echo ""
	@echo "This project use python 3.9.+"
	@echo "= if poetry install error try use"
	@echo "$$ pyenv shell ${ENV_PYTHON_ENV_VERSION}"
	@echo "or target version to fix"
	@echo ""
	@echo "------    ------"
	@echo "- first run you can use make init to check environment"
	@echo "------    ------"
	@echo ""
	@echo "$$ make init                      ~> init this project"
	@echo ""
	@echo "$$ make dep                       ~> run install dependencies"
	@echo "$$ make dep.fix                   ~> run change dependencies to lock"
	@echo "$$ make up                        ~> run update dependencies"
	@echo "$$ make test                      ~> run test case"
	@echo "$$ make test.coverage             ~> run test case with coverage"
	@echo "$$ make ci                        ~> run ci check"
	@echo ""

.PHONY: help
help: helpProjectRoot
	@echo ""
	@echo "-- more info see Makefile"
