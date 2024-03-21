from pydantic import BaseModel


class User_form(BaseModel):
    mail: str
    password: str


class Auth_record(BaseModel):
    mail: str
    hashed_password: str


class Its_me(BaseModel):
    mail: str


class Access_token(BaseModel):
    access_token: str


class Refresh_token(BaseModel):
    refresh_token: str


class Pair_tokens(BaseModel):
    access_token: str
    refresh_token: str
