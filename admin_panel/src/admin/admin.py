from src.sender import send_message


async def admin_helper(
    chat_id: int,
    username: str,
    message_text: str
) -> None:
    await send_message(chat_id, message_text, [username])
