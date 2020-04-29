.PHONY: setup network build start qa style safety test test-travis flake8 \
    isort-check isort license stop clean logs black-check black

################################################################################
# Variables                                                                     #
################################################################################

IMAGE ?= gcr.io/{{cookiecutter.gcloud_project}}/{{cookiecutter.project_slug}}
BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)
BUILD_COMMIT ?= $(shell git rev-parse HEAD)
SHORT_COMMIT ?= $(shell git rev-parse --short HEAD)
BUILD_TIMESTAMP ?= $(shell date --utc --iso-8601=seconds)
BUILD_DATE ?= $(shell date --utc --iso-8601=date)
BUILD_TAG ?= ${BRANCH}_${BUILD_DATE}_${SHORT_COMMIT}

################################################################################
# Commands                                                                     #
################################################################################

## Create the docker bridge network if necessary.
network:
	docker network inspect {{cookiecutter.github_username}} >/dev/null 2>&1 || \
		docker network create {{cookiecutter.github_username}}

## Run all initialization targets.
setup: network

## Generate the compiled requirements files.
lock:
	$(eval LATEST_BASE_TAG := $(shell tag-spy dddecaf/wsgi-base alpine \
		dk.dtu.biosustain.wsgi-base.alpine.build.timestamp))
	$(file >LATEST_BASE_TAG, $(LATEST_BASE_TAG))
	$(eval COMPILER_TAG := $(subst alpine,alpine-compiler,$(LATEST_BASE_TAG)))
	$(info ************************************************************)
	$(info * Compiling service dependencies on the basis of:)
	$(info * dddecaf/wsgi-base:$(COMPILER_TAG))
	$(info ************************************************************)
	docker pull dddecaf/wsgi-base:$(COMPILER_TAG)
	docker run --rm --mount \
		"source=$(CURDIR)/requirements,target=/opt/requirements,type=bind" \
		dddecaf/wsgi-base:$(COMPILER_TAG) \
		pip-compile --allow-unsafe --verbose --generate-hashes --upgrade \
		/opt/requirements/requirements.in

## Change file ownership from root to local user.
own:
	sudo chown "$(shell id --user --name):$(shell id --group --name)" \
		requirements/requirements.txt
	sudo chown -R "$(shell id --user --name):$(shell id --group --name)" .tox

## Build local docker images.
build:
	$(eval LATEST_BASE_TAG := $(shell cat LATEST_BASE_TAG))
	$(info ************************************************************)
	$(info * Building the service on the basis of:)
	$(info * dddecaf/wsgi-base:$(LATEST_BASE_TAG))
	$(info * Today is $(shell date --utc --iso-8601=date).)
	$(info * Please re-run `make lock` if you want to check for and)
	$(info * depend on a later version.)
	$(info ************************************************************)
	docker pull dddecaf/wsgi-base:$(LATEST_BASE_TAG)
	docker build --build-arg BASE_TAG=$(LATEST_BASE_TAG) \
		--build-arg BUILD_COMMIT=$(BUILD_COMMIT) \
		--build-arg BUILD_TIMESTAMP=$(BUILD_TIMESTAMP) \
		--tag $(IMAGE):$(BRANCH) \
		--tag $(IMAGE):$(BUILD_TAG) \
		.

## Build the local docker-compose image.
build-local:
	$(eval LATEST_BASE_TAG := $(shell cat LATEST_BASE_TAG))
	BASE_TAG=$(LATEST_BASE_TAG) docker-compose build

## Push local Docker images to their registries.
push:
	docker push $(IMAGE):$(BRANCH)
	docker push $(IMAGE):$(BUILD_TAG)

## Start all services in the background.
start:
	docker-compose up --force-recreate -d

## Apply all quality assurance (QA) tools.
qa:
	docker-compose exec web tox -e isort -- ''
	docker-compose exec web tox -e black -- ''

## Run all style checks.
style:
	docker-compose exec -e ENVIRONMENT=testing web \
		tox -e isort,black,flake8,license

safety:
	docker-compose exec -e ENVIRONMENT=testing web \
		tox -e safety

## Run the test suite.
test:
	docker-compose exec -e ENVIRONMENT=testing web \
		tox -e py36

## Run all quality control (QC) tools.
qc: style safety test

## Stop all services.
stop:
	docker-compose stop

## Stop all services and remove containers.
clean:
	docker-compose down

## Follow the logs.
logs:
	docker-compose logs --tail="all" -f

################################################################################
# Self Documenting Commands                                                    #
################################################################################

.DEFAULT_GOAL := show-help

# Inspired by
# <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
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
	| more $(shell test $(shell uname) = Darwin \
	&& echo '--no-init --raw-control-chars')
