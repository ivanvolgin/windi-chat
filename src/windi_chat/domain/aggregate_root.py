from __future__ import annotations
import uuid
from typing import List


class DomainEvent:
    pass


class AggregateRoot:
    """
    Базовый класс для всех Aggregate Root’ов.
    Держит id, версию и список событий.
    """

    __slots__ = ("id", "version", "_events")

    def __init__(self, id_: uuid.UUID | None = None, version: int = 0) -> None:
        self.id: uuid.UUID = id_ or uuid.uuid4()
        self.version: int = version  # для optimistic lock
        self._events: List[DomainEvent] = []  # «внутренний outbox»

    # --- инфраструктурные методы ---

    def pull_events(self) -> list[DomainEvent]:
        """
        Забрать и очистить накопленные события,
        чтобы UoW мог их опубликовать после commit.
        """
        events = self._events.copy()
        self._events.clear()
        return events

    def push_event(self, event: DomainEvent) -> None:
        self._events.append(event)
