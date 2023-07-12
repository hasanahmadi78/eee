

from datetime import datetime

def looger(func):

    def wraped_func(*args, **keyword):
        start_time = datetime.now()
        res = func(*args, **keyword)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"the time for this matsh {duration.days} : {duration.seconds} : {duration.microseconds}")
        return res
    return wraped_func