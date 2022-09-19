from typing import Callable
from whistle import Event, EventDispatcher


class StfuEvent(Event):
    id: str


class StfuEventDispatcher:
    dispatcher: EventDispatcher

    def __init__(self):
        self.dispatcher = EventDispatcher()

    def dispatch(self, event: StfuEvent):
        self.dispatcher.dispatch(event.id, event)

    def register(self, event_id, fn: Callable):
        self.dispatcher.add_listener(event_id, fn)
