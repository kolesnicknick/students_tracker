import logging
import os
from datetime import datetime, timezone


class MiddleWareFileLogger:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        logging.basicConfig(filename=os.getcwd() + "/students_tracker/requestlogs.log",
                            level=logging.INFO)

    def __call__(self, request):
        start = datetime.now(timezone.utc)
        request_info = f'{start}: {request.path} {request.method}'
        response = self.get_response(request)
        end = datetime.now(timezone.utc)
        logging.info(
            f"{request_info} returned status code:"
            f" {response.status_code} in {str(end - start).split('.')[-1]} microseconds"
        )
        return response
