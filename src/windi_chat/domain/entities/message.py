from datetime import datetime, UTC
from uuid import UUID, uuid4

from windi_chat.domain.errors import (
    InvalidSenderError,
    EmptyMessageTextError,
    MessageTooLongError,
)


class Message:
    __slots__ = ("msg_id", "chat_id", "sender_id", "text", "ts", "is_read")

    def __init__(
        self, chat_id: UUID, sender_id: UUID, text: str, is_read: bool = False
    ):
        if not isinstance(sender_id, UUID):
            raise InvalidSenderError("Sender ID must be a valid UUID")

        if not text.strip():
            raise EmptyMessageTextError("Message text cannot be empty")

        if len(text) > 1000:
            raise MessageTooLongError("Message too long")

        self.msg_id = uuid4()
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.text = text
        self.ts = datetime.now(UTC)
        self.is_read = is_read
