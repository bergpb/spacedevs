.PYHONY: test
test:
	@pytest -vv

.PYHONY: check-format
check-format:
	@black . --check --exclude=".venv"

.PYHONY: format
format:
	@black . --exclude=".venv"

