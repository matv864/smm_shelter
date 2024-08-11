from uuid import UUID

from src.developer import developer

from src.sender import send_message


class Common_handler:
    @staticmethod
    async def send_first_message(
        chat_id: int,
        username: str
    ) -> None:
        developer.contexts_of_admins[username].get_first_message = True
        await send_message(chat_id, "выберите, что хотите сделать", [
            ("создать запись о питомце", "create"),
            ("редактировать запись о питомце", "edit"),
            ("удалить запись о питомце", "delete"),
            ("добавить фото питомца", "add_photo")
        ])

    @staticmethod
    async def working_with_mode(
        chat_id: int,
        username: str,
        message_text: str
    ) -> None:
        message_text = message_text.strip().lower()
        if message_text in ["create", "edit", "delete", "add_photo"]:
            developer.contexts_of_admins[username].mode = message_text
            if developer.contexts_of_admins[username].mode == "create":
                await send_message(
                    chat_id, "начать заполение данных о питомце", [
                        ("поехали", "start write data")
                    ]
                )
            else:
                await send_message(chat_id, "напишите id записи о питомце")
        else:
            await Common_handler.send_first_message(chat_id)

    @staticmethod
    async def working_with_record_id(
        chat_id: int,
        username: str,
        message_text: str
    ) -> None:
        try:
            uuid_of_record = UUID(message_text, version=4)
        except ValueError:
            Common_handler.working_with_mode(chat_id, username, message_text)

        developer.contexts_of_admins[username].record_uuid = uuid_of_record

        await send_message(chat_id, "начать заполение данных о питомце", [
            ("поехали", "start write data")
        ])
