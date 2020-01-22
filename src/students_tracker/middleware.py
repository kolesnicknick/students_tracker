import logging
import os


class MiddleWareFileLogger:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        logging.basicConfig(filename=os.getcwd() + "/students_tracker/requestlogs.log",
                            level=logging.INFO)
        logging.info(str(request))
        response = self.get_response(request)
        logging.info(str(response))
        return response
