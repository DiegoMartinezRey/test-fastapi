from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", age=35)]


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def users():
    return users_list


@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


@app.get("/userquery/")
async def userByQuery(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
