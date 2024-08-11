import os

from typing import Optional, Literal, List, Any
from uuid import UUID


class Context:
    def __init__(self):
        self.get_first_message: bool = False
        self.mode: \
            Literal["create", "edit", "delete", "add_photo", None] = None
        self.record_uuid: Optional[UUID] = None
        self.data_of_record: dict[str, Any] = dict()
        self.set_of_photo: list[Any] = []

    def drop(self) -> None:
        self.get_first_message: bool = False
        self.mode = None
        self.record_uuid = None
        self.data_of_record = None
        self.set_of_photo: list[Any] = []


class Developer:
    def __init__(self):

        self.__developer_username = os.getenv("DEVELOPER_USERNAME")

        self.white_user_list: List[str] = [self.__developer_username]
        self.contexts_of_admins: dict[str, Context] = dict()

    async def is_it_developer(self, username: str) -> bool:
        return username == self.__developer_username

    async def is_it_admin(self, username: str) -> bool:
        return username in self.white_user_list

    async def __add_admin(self, username: str) -> None:
        self.white_user_list.append(username)
        self.contexts_of_admins[username] = Context()

    async def __delete_admin(self, username: str) -> None:
        self.white_user_list.remove(username)
        self.contexts_of_admins.pop(username)

    async def command_from_developer(self, text: str) -> str:
        command, *args = text.split()
        if args:
            username = args[0].replace("@", "", 1)
        match command:
            case "add":
                if username in self.white_user_list:
                    return f"user @{username} is already on whitelist"
                await self.__add_admin(username)
                return f"I added user @{username}"
            case "del":
                if username not in self.white_user_list:
                    return f"user @{username} was not on whitelist"
                await self.__delete_admin(username)
                return f"I deleted user @{username}"
            case "list":
                return "all admins\n" + "\n".join(self.white_user_list)
            case _:
                return "I don't know this command"


developer = Developer()
