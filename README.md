# PlantDaddy-Backend
REST API for PlantDaddy web app. Leverages a modern, typed Python stack.

## Value Prop:
One place with all the info you need to keep the plant alive

## Features:
- Name, classify, categorize, and perform lookups for plants
- Create PlantGroups
- Schedule events for watering/care

## Stack:
- FastAPI (api framework)
- SQLModel (orm)
- Poetry (dependencies/venv)
- Black (formatting)
- Flake8 (linting)
- MyPy (strong typing)

# Contributor Quickstart
**Prerequisite:** _[Poetry installation](https://python-poetry.org/docs/)_

(VSCode)
- install Python/Pylance/Toml extensions
- update poetry virtual environments setting to keep it in the project instead of default location by running: `poetry config virtualenvs.in-project true`

## setup virtual environment
- Create Virtual Environments with poetry: `poetry env use python3.10` and `poetry env use python3.9`.
- Activate the venv using `poetry shell`
- Install the packages listed in `pyproject.toml` into your **venv** using `poetry install`.


## setup database
- Create a local SQLite database file by creating a file ending in `.db`. 
- Create a file ".env" in the project root and add the absolute path to your `.db` file to a variable `SQLITE_FILE`.

## run the server
- Start the server by running `python3 -m app.console` from the project root. 
- Alternatively, run from the command line with `uvicorn app.api.v1.endpoints.plant:app --reload`
- Test the endpoints by going to the localhost link which appears in the console and appending "/docs" to the URL
