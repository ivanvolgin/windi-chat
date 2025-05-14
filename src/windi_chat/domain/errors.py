class ChatError(Exception):
    """Базовая ошибка для Chat."""


class InvalidChatTitleError(ChatError):
    """Название чата некорректно."""


class EmptyMembersError(ChatError):
    """У чата должен быть хотя бы один участник."""


class NotMemberError(ChatError):
    """Отправитель не состоит в чате."""


class MessageError(Exception):
    """Базовая ошибка для сообщений."""


class EmptyMessageTextError(MessageError):
    """Текст сообщения не может быть пустым."""


class MessageTooLongError(MessageError):
    """Текст сообщения превышает допустимую длину."""


class InvalidSenderError(MessageError):
    """Недопустимый ID отправителя."""
