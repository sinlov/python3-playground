.PHONY: test check clean build dist all

ENV_CLI_NAME ?= py-cli-temp.py

all:
	@echo "~> start base info"
	python down_all_git_repo.py -v -s

init:
	@echo "if error can use [make updatePip] "
	pip install fabric==1.9.2

updatePip:
	@echo "if install error can use [ sudo -H pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple ]"
	@echo "Error: Consider using the `--user` option or check the permissions. "
	@echo "just use [ sudo -H pip install --upgrade pip ]"
	pip install --upgrade pip

historyPip:
	@echo "just see by curl and jq [ sudo apt-get install jq ] or see https://stedolan.github.io/jq/download/"
	curl -s 'https://pypi.org/pypi/fabric/json' | jq

dep:
	@echo "need python and pip install of fabric"
	python -V
	pip freeze | grep fabric

clean:
	python ${ENV_CLI_NAME} -v -c

test:
	python ${ENV_CLI_NAME} -v -t

help:
	@echo "first use just [ make init ]"
	python down_all_git_repo.py --help