# Third party modules
import grpc

# Local modules
import auth_pb2
import auth_pb2_grpc

# built-in modules
import os

class AuthClient:
    def __init__(self, host=os.getenv('AUTH_GRPC','localhost'), port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)

    def authenticate(self, email, password):
        request = auth_pb2.AuthRequest(email=email, password=password)
        return self.stub.Authenticate(request)

    def refresh_token(self, refresh_token):
        request = auth_pb2.TokenRequest(token=refresh_token)
        return self.stub.RefreshToken(request)

    def verify_token(self, token):
        request = auth_pb2.TokenRequest(token=token)
        return self.stub.VerifyToken(request)
