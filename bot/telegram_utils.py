from typing import Optional
from telegram import Update, Message
from telegram.constants import ParseMode

PARSE_MODE_MAPPING = {
    "html": ParseMode.HTML,
    "markdown": ParseMode.MARKDOWN
}

MESSAGE_LENGTH_LIMIT = 4096

UNKNOWN_USER_USERNAME = "unknown user"


def get_username(update: Update) -> str:
    if update.edited_message is not None and update.edited_message.from_user is not None:
        return update.edited_message.from_user.username or UNKNOWN_USER_USERNAME

    if update.message is None or update.message.from_user is None:
        return UNKNOWN_USER_USERNAME

    return update.message.from_user.username or UNKNOWN_USER_USERNAME


def get_language(source: Update | Message) -> Optional[str]:
    if isinstance(source, Update):
        return source.message.from_user.language_code

    if isinstance(source, Message):
        return source.from_user.language_code

    raise ValueError("Expected an Update or a Message object")


def get_parse_mode(parse_mode: str) -> ParseMode:
    if parse_mode not in PARSE_MODE_MAPPING:
        raise ValueError(f"Unknown parse mode <{parse_mode}>")

    return PARSE_MODE_MAPPING[parse_mode]
