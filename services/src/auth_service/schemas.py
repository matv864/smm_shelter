from pydantic import BaseModel


class User_form(BaseModel):
    username: str
    password: str


class Auth_record(BaseModel):
    username: str
    password: str


class Its_me(BaseModel):
    username: str


class Access_token(BaseModel):
    access_token: str


class Refresh_token(BaseModel):
    refresh_token: str


class Pair_tokens(BaseModel):
    token_type: str = "bearer"
    access_token: str
    refresh_token: str
