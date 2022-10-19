FROM python:3.10

RUN python -m pip install --upgrade pip

ARG wheel=first_project-0.1.0-py3-none-any.whl

WORKDIR /code

COPY ./dist/$wheel /code/$wheel

RUN pip install --no-cache-dir --upgrade /code/$wheel


CMD ["python", "-m", "demo.first.main"]

# Example if this were a FastAPI app
# ENTRYPOINT ["uvicorn", "demo.first:app", "--host:0.0.0.0", "---port=5000"]
