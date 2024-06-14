FROM tiangolo/uvicorn-gunicorn:python3.11

WORKDIR /code
COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m grpc_tools.protoc -I=/code --python_out=. --grpc_python_out=. /code/order.proto