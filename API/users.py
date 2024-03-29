from typing import Annotated
from fastapi import APIRouter,Path,Query,Body,Depends
from models import User,Gender
from db import get_session
from API_functions import get_all_user_db,get_user_db,add_user_db,delete_user_db,update_user_db
users=APIRouter()

@users.post("/users/{user_name}")
def add_users(
    user_name:Annotated[str,Path(...,title="user_name",description="username for each user")],
    data: User = Body(...)
    ):
    data=add_user_db(data=data,ses=get_session(),user_name=user_name)
    return data
    
@users.delete("/users/{user_name}")
def delete_users(
    user_name:Annotated[str,Path(...,description="delete any user")],
    ):
    data=delete_user_db(username=user_name,ses=get_session())
    return data

@users.put("/users/{user_name}")
def update_users(
    user_name:Annotated[str,Path(...,title="user_name",description="username for each user")],
    body:User=Body(...),
    ):
    data=update_user_db(username=user_name,ses=get_session(),body=body)
    return data


@users.get("/users/{user_name}")
def get_user(
    user_name:Annotated[str,Path(...,description="give username")]
    ):
    data=get_user_db(user_name=user_name,ses=get_session())
    return data

@users.get("/users")
def get_all_users():
    data=get_all_user_db(ses=get_session())
    return data

