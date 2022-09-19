from typing import Type
from injector import singleton, Binder

from stfu import manager, event, event_listener


def bind_singleton(binder: Binder, obj):
    binder.bind(obj, to=obj, scope=singleton)


def managers(binder: Binder):
    # @todo bind_manager with ModelFactory and ModelEventDispatcher
    bind_singleton(binder, manager.UserManager)


def bind_event_listener(
    binder: Binder,
    stfu_event: Type[event.StfuEvent],
    stfu_event_listener: Type[event_listener.StfuEventListener]
):
    bind_singleton(binder, stfu_event_listener)
    binder.injector.get(event.StfuEventDispatcher).register(
        stfu_event.id,
        binder.injector.get(stfu_event_listener).on
    )


def events(binder: Binder):
    bind_singleton(binder, event.StfuEventDispatcher)
    # bind_event_listener(
    #     binder,
    #     event.DoThingEvent,
    #     event_listener.do_thing.DoThingEventListener
    # )


modules = [
    managers,
    events,
]
