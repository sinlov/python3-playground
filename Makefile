.PHONY: test check clean build dist all

# each tag change this
ENV_DIST_VERSION := 1.0.0

ENV_PROJECT_NAME ?= tudm-cli
ENV_ROOT ?= $(shell pwd)
ENV_MODULE_FOLDER ?= ${ENV_ROOT}
ENV_MODULE_MANIFEST = ${ENV_ROOT}/package.json

runMain:
	pipenv run main

runTest:
	pipenv run test_main

env:
	pipenv --version
	pipenv check

init:
	pipenv install --skip-lock --dev

rmEnv:
	pipenv --rm

install:
	pipenv sync --dev
	pipenv sync

graph:
	pipenv graph

dependencies:
	-pipenv check --verbose
	-pipenv lock --verbose

dependenciesUpdate:
	-pipenv check --clear
	-pipenv update --outdated
	-pipenv lock

shell:
	@echo "-> in pipenv shell"
	@echo " install runtime like: pipenv install requests"
	@echo " install develop like: pipenv install httpie --dev"
	@echo " uninstall like: pipenv uninstall requests"
	@echo ""
	@echo "and will load environment file as .env"
	pipenv shell

utils:
	node -v
	npm -v
	npm install -g commitizen cz-conventional-changelog conventional-changelog-cli

tagVersionHelp:
	@echo "-> please check to change version, now is ${ENV_DIST_VERSION}"
	@echo "change check at ${ENV_ROOT}/Makefile:4"
	@echo "change check at ${ENV_MODULE_MANIFEST}:3"
	@echo "change check at ${ENV_ROOT}/tudm.py:27"
	@echo ""
	@echo "please check all file above!"
	@echo ""

tagBefore: tagVersionHelp
	conventional-changelog -i CHANGELOG.md -s  --skip-unstable
	@echo ""
	@echo "place check all file, then add git tag to push!"

help:
	@echo "unity makefile template"
	@echo " module project  name: ${ENV_PROJECT_NAME}"
	@echo " module folder   path: ${ENV_MODULE_FOLDER}"
	@echo " module version    is: ${ENV_DIST_VERSION}"
	@echo " module manifest path: ${ENV_MODULE_MANIFEST}"
	@echo ""
	@echo "  first need init utils"
	@echo "$$ make utils               ~> npm install git cz"
	@echo "  1. add change log, then write git commit , replace [ git commit -m ] to [ git cz ]"
	@echo "  2. generate CHANGELOG.md doc: https://github.com/commitizen/cz-cli#conventional-commit-messages-as-a-global-utility"
	@echo ""
	@echo "  then you can generate CHANGELOG.md as"
	@echo "$$ make tagVersionHelp      ~> print version when make tageBefore will print again"
	@echo "$$ make tagBefore           ~> generate CHANGELOG.md and copy to module folder"
	@echo ""
	@echo "This project use python 3.9.+"
	@echo "------    ------"
	@echo "- first run you can use make init to check environment"
	@echo "------    ------"
	@echo ""
	@echo "$$ make init                     ~> init this project"
	@echo "$$ make rmEnv                    ~> remove pipenv environment"
	@echo "$$ make env                      ~> show env of this project"
	@echo "$$ make graph                    ~> show graph of this project"
	@echo "$$ make shell                    ~> into shell, out use exit or ctrl-D"
	@echo ""
	@echo "$$ make runMain                  ~> pipenv run main"
	@echo "$$ make runTest                  ~> pipenv run test_main"

all:
	@echo "~> start base info"