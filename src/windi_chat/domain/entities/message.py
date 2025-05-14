from uuid import UUID

from windi_chat.domain.errors import (
    InvalidSenderError,
    EmptyMessageTextError,
    MessageTooLongError,
)


class Message:
    __slots__ = ("sender_id", "text", "is_read")

    def __init__(
        self,
        sender_id: UUID,
        text: str,
        is_read: bool = False,
    ):
        if not isinstance(sender_id, UUID):
            raise InvalidSenderError("Sender ID must be a valid UUID")

        if not text.strip():
            raise EmptyMessageTextError("Message text cannot be empty")

        if len(text) > 1000:
            raise MessageTooLongError("Message too long")

        self.sender_id = sender_id
        self.text = text
        self.is_read = is_read
