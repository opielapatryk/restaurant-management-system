# Local modules
import auth_pb2
import auth_pb2_grpc
from database import SessionLocal, init_db
from users import User
from auth_utils import verify_password, get_password_hash, create_access_token, create_refresh_token, verify_token

# Third party modules
import grpc
from sqlalchemy.orm import Session

# Built-in modules
from concurrent import futures

class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def Authenticate(self, request, context):
        email = request.email
        password = request.password

        db: Session = SessionLocal()
        user = db.query(User).filter(User.email == email).first()
        hashed_password = bytes(user.hashed_password)
        if not user or not verify_password(password, hashed_password):
            return auth_pb2.AuthResponse(success=False, message="Invalid credentials", access_token="", refresh_token="")
        
        access_token = create_access_token(data={"sub": email})
        refresh_token = create_refresh_token(data={"sub": email})
        return auth_pb2.AuthResponse(success=True, message="Authenticated", access_token=access_token, refresh_token=refresh_token)

    def RefreshToken(self, request, context):
        refresh_token = request.token
        email = verify_token(refresh_token)
        if email is None:
            return auth_pb2.AuthResponse(success=False, message="Invalid refresh token", access_token="", refresh_token="")
        
        new_access_token = create_access_token(data={"sub": email})
        new_refresh_token = create_refresh_token(data={"sub": email})
        return auth_pb2.AuthResponse(success=True, message="Token refreshed", access_token=new_access_token, refresh_token=new_refresh_token)

    def VerifyToken(self, request, context):
        token = request.token
        email = verify_token(token)
        if email is None:
            return auth_pb2.TokenResponse(valid=False, message="Invalid token")
        return auth_pb2.TokenResponse(valid=True, message="Token is valid")

def serve():
    init_db()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
