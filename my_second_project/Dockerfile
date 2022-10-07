FROM python:3.10

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/second-0.1.0-py3-none-any.whl /code/second-0.1.0-py3-none-any.whl

RUN pip install --no-cache-dir --upgrade /code/second-0.1.0-py3-none-any.whl


CMD ["python", "-m", "my_second_project.second.main"]
