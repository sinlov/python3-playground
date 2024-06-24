.PHONY: test check clean build dist all

# each tag change this
ENV_DIST_VERSION := 1.0.0

ENV_PROJECT_NAME ?=python3-playground
ENV_CHECK_FILES=src/ tests/
ENV_BLACK_OPTS=
py_warn =PYTHONDEVMODE=1
ENV_PYTHON_ENV_VERSION =3.11.7

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
	@echo "- this project manager by poetry -"
ifeq ($(OS),Windows_NT)
	@echo ""
	@echo "windows install as:"
	@echo "-> scoop install main/poetry"
	@echo ""
endif
	@echo "= if poetry install error try use"
	@echo "$$ pyenv shell ${ENV_PYTHON_ENV_VERSION}"
	@echo "or target version to fix"
	@echo "- show poetry env list -"
	@poetry env list
	@echo ""
	@echo ------- end  show env ---------

.PHONY: up
up:
	@poetry env info
	@poetry update

.PHONY: dep
dep:
	@poetry env info
	@poetry install

.PHONY: depFix
depFix:
	@poetry env info
	@poetry lock --no-update

.PHONY: depCheck
depCheck:
	$(info check: poetry env info)
	@poetry env info
	$(info check: poetry env list)
	poetry env list
	@poetry check

.PHONY: depLock
depLock:
	@poetry lock

.PHONY: init
init: dep depFix
	@poetry about
	@echo "=> just init finish this project by poetry"

.PHONY: style
style: dep
	@poetry env info
	@poetry run ruff format $(ENV_CHECK_FILES)

.PHONY: check
check:
	@poetry env info
	@poetry run ruff check $(ENV_CHECK_FILES)

.PHONY: test
test: dep
	${py_warn} poetry run pytest

.PHONY: testWithWarn
testWithWarn:
	${py_warn} poetry run pytest -W error::UserWarning

.PHONY: testDisableWarn
testDisableWarn:
	${py_warn} poetry run pytest --disable-warnings

.PHONY: testCoverage
testCoverage:
	${py_warn} poetry run pytest --cov-append --cov-report=html --cov=./

.PHONY: testClean
testClean:
	@$(RM) -r .pytest_cache/

.PHONY: testCoverageClean
testCoverageClean:
	@$(RM) .coverage
	@$(RM) .coverage.*
	@$(RM) -r htmlcov/

.PHONY: ci
ci: check test

.PHONY: build
build: dep
	@poetry build

.PHONY: buildOnly
buildOnly:
	@poetry build

.PHONY: publish
publish: dep
	@poetry publish --build

.PHONY: shell
shell:
	@echo "-> in poetry shell"
	@echo ""
	@echo "and will load environment file as .env"
	poetry shell

.PHONY: clean
cleanDist:
	@$(RM) -r dist

.PHONY: cleanLogs
cleanLogs:
	@$(RM) -r logs

.PHONY: cleanAll
cleanAll: cleanDist cleanLogs testCoverageClean testClean
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
	@echo "$$ make init                     ~> init this project"
	@echo ""
	@echo "$$ make dep                      ~> run install dependencies"
	@echo "$$ make depFix                   ~> run change dependencies to lock"
	@echo "$$ make up                       ~> run update dependencies"
	@echo "$$ make test                     ~> run test case"
	@echo "$$ make testCoverage             ~> run test case with coverage"
	@echo "$$ make ci                       ~> run ci check"
	@echo ""

.PHONY: help
help: helpProjectRoot
	@echo ""
	@echo "-- more info see Makefile"
