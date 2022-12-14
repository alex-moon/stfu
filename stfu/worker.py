from stfu.service.queue import QueueService

from . import create_app
from .injector import injector
from .job import *

if __name__ == '__main__':
    app = create_app()
    queue_service = injector.get(QueueService)
    queue_service.get_worker().work()
