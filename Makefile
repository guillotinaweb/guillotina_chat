mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))


run-postgres:
	docker run -e POSTGRES_DB=guillotina -e POSTGRES_USER=postgres -e POSTGRES_HOST_AUTH_METHOD=trust -p 127.0.0.1:5432:5432 postgres:9.6
