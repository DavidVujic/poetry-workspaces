FROM python:3.10

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/poetry_workspaces-0.1.0-py3-none-any.whl /code/poetry_workspaces-0.1.0-py3-none-any.whl

RUN pip install --no-cache-dir --upgrade /code/poetry_workspaces-0.1.0-py3-none-any.whl


CMD ["python", "-m", "my_first_project.my_project.main"]
