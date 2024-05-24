FROM python

WORKDIR /service/auth
COPY . /service/auth

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I=/service/auth --python_out=. --grpc_python_out=. /service/auth/auth.proto

EXPOSE 50051
ENTRYPOINT [ "python", "auth_server.py" ]
