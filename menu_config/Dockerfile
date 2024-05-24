FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m grpc_tools.protoc -I=/code --python_out=. --grpc_python_out=. /code/auth.proto

CMD ["fastapi", "run", "main.py", "--port", "1028"]