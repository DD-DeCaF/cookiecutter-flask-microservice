.PHONY: start qa test flake8 isort isort-save license stop clean logs

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Create the docker bridge network if necessary.
network:
	docker network inspect {{cookiecutter.github_username}} >/dev/null 2>&1 || \
		docker network create {{cookiecutter.github_username}}

## Build local docker images.
build: network
	docker-compose build

## Start all services in the background.
start:
	docker-compose up -d

## Run all QA targets.
qa: test style

## Run all style related targets.
style: flake8 isort license

## Run the tests.
test:
	docker-compose run --rm -e ENVIRONMENT=testing web \
		/bin/sh -c "pytest -s --cov=src/{{cookiecutter.project_module}} tests"

## Run the tests and report coverage.
test-travis:
	docker-compose run --rm -e ENVIRONMENT=testing \
		-e $$(printenv | egrep "^CI$|^TRAVIS$|^TRAVIS_" ) web \
		pytest --cov=src/{{cookiecutter.project_module}} tests && codecov

## Run flake8.
flake8:
	docker-compose run --rm web \
		flake8 src/{{cookiecutter.project_module}} tests

## Check Python package import order.
isort:
	docker-compose run --rm web \
		isort --check-only --recursive src/{{cookiecutter.project_module}} tests

## Sort imports and write changes to files.
isort-save:
	docker-compose run --rm web \
		isort --recursive src/{{cookiecutter.project_module}} tests

## Verify source code license headers.
license:
	./scripts/verify_license_headers.sh src/{{cookiecutter.project_module}} tests

## Stop all services.
stop:
	docker-compose stop

## Stop all services and remove containers.
clean:
	docker-compose down

## Follow the logs.
logs:
	docker-compose logs --tail="all" -f

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
