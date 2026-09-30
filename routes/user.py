from fastapi import APIRouter


user = APIRouter();

@user.get("/users")
def hello_user():
    return {"message": "Hello, User!"}