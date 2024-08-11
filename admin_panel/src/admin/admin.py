from src.developer import developer

from src.admin.interface import Common_handler


async def admin_helper(
    chat_id: int,
    username: str,
    message_text: str
) -> None:
    if developer.contexts_of_admins[username].get_first_message is False:
        # handler to tell to admin what he can
        await Common_handler.send_first_message(chat_id)
    elif developer.contexts_of_admins[username].mode is None:
        # handler to understand what admin want to do
        await Common_handler.working_with_mode(chat_id, username, message_text)
    elif (
        developer.contexts_of_admins[username].mode != "create" and
        developer.contexts_of_admins[username].record_id is None
    ):
        # handler to understand which record admin want to
        # - edit
        # - delete
        # - add photo
        await Common_handler.working_with_record_id(
            chat_id,
            username,
            message_text
        )
    else:
        # go to write data of record and (if need) drop admin context
        ...

    # await send_message(chat_id, message_text, [username])
