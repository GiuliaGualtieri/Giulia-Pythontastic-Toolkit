.PHONY: format
.PHONY: lint
.PHONY: test

format:
	ruff --fix src tests
	black src tests

test:
	pytest tests

