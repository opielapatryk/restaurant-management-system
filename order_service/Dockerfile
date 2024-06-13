FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m grpc_tools.protoc -I=src/gRPC --python_out=src/gRPC --grpc_python_out=src/gRPC src/gRPC/order.proto

CMD ["python", "run.py"]