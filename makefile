.PYHONY: test
test:
	@pytest -vv

.PYHONY: up-test
up-test:
	@pytest --force-regen

.PYHONY: check-format
check-format:
	@black . --check --exclude=".venv"

.PYHONY: format
format:
	@black . --exclude=".venv"

