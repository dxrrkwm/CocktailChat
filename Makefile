PYTHON = python
POETRY = poetry

.PHONY: help
help:
	@echo "Usage: make [target] [path=<path>]"
	@echo ""
	@echo "Targets:"
	@echo "  deps      Install dependencies"
	@echo "  run       Start the app with uvicorn"
	@echo "  lint      Run isort and Ruff on a specific path"
	@echo "  clean     Remove __pycache__ files"

.PHONY: deps
deps:
	${POETRY} install

.PHONY: run
run:
	${POETRY} run uvicorn main:app --reload

.PHONY: lint
lint:
	@echo "Running isort and Ruff on: $(path)"
	${POETRY} run isort $(path)
	${POETRY} run ruff check --fix $(path)

.PHONY: clean
clean:
	find . -name "__pycache__" -exec rm -rf {} +