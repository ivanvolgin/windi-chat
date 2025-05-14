import pytest
from uuid import uuid4
from windi_chat.domain.entities.message import Message
from windi_chat.domain.errors import (
    InvalidSenderError,
    EmptyMessageTextError,
    MessageTooLongError,
)


@pytest.mark.asyncio
async def test_message_created_successfully():
    msg = Message(chat_id=uuid4(), sender_id=uuid4(), text="Hello")
    assert msg.text == "Hello"
    assert msg.is_read is False


@pytest.mark.asyncio
async def test_invalid_sender_raises():
    with pytest.raises(InvalidSenderError):
        Message(chat_id=uuid4(), sender_id="not-a-uuid", text="test")


@pytest.mark.asyncio
async def test_empty_text_raises():
    with pytest.raises(EmptyMessageTextError):
        Message(chat_id=uuid4(), sender_id=uuid4(), text="   ")


@pytest.mark.asyncio
async def test_too_long_text_raises():
    with pytest.raises(MessageTooLongError):
        Message(chat_id=uuid4(), sender_id=uuid4(), text="a" * 1001)
