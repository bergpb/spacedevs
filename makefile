.PYHONY: test
test:
	FLASK_ENV=testing pytest -vv

.PYHONY: up-test
up-test:
	FLASK_ENV=testing @pytest --force-regen

.PYHONY: check-format
check-format:
	@black . --check --exclude=".venv"

.PYHONY: format
format:
	@black . --exclude=".venv"

