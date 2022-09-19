from .stfu_exception import StfuException


class NotFoundException(StfuException):
    code = 404

    def __init__(self, model_class: str, id_: int):
        super().__init__("Model not found: [%s] for id [%s]" % (model_class, id_))
