from typing import Set
from uuid import UUID

from windi_chat.domain.entities.message import Message
from windi_chat.domain.errors import (
    NotMemberError,
    InvalidChatTitleError,
    EmptyMembersError,
)
from windi_chat.domain.aggregate_root import AggregateRoot


class Chat(AggregateRoot):
    __slots__ = AggregateRoot.__slots__ + (
        "title",
        "member_ids",
        "_messages",
        "_events",
    )

    def __init__(self, title: str, members: Set[UUID], **kw):
        super().__init__(**kw)

        if not title.strip():
            raise InvalidChatTitleError("Chat title cannot be empty")

        if len(title) > 100:
            raise InvalidChatTitleError("Chat title is too long (max 100 characters)")

        if not members:
            raise EmptyMembersError("Chat must have at least one member")

        self.title = title
        self.member_ids = members
        self._messages: list[Message] = []
        self._events: list[object] = []

    def send_message(self, sender: UUID, text: str) -> None:
        if sender not in self.member_ids:
            raise NotMemberError("The sender of message must be a member of the chat")

        msg = Message(sender_id=sender, text=text)
        self._messages.append(msg)
        self.push_event(MessageSent(msg))
