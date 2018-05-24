TAG ?= dev

# docker
build-image:
	docker build -t twigafoods/badge-automation-service:$(TAG) .;
	docker-compose up;