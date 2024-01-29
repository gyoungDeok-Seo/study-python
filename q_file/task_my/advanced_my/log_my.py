import datetime


def log_time(original_function):
    def logging(*args, **kwargs):
        self, other = args
        error_code = kwargs['error_code']
        with open('log.txt', 'a') as file:
            if error_code is None:
                result = original_function(*args, **kwargs)
                now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                file.w
            return

    return logging