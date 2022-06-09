from datetime import datetime
import psutil


def cpu_usage(func):
    """
    It takes a function as an argument, and returns a wrapper function that prints out the CPU usage of
    the original function

    :param func: The function to be decorated
    :return: A function object
    """
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('-'*60)
        print(f'Elapsed time: {time_elapsed} sec')
        print(f'CPU %: {psutil.cpu_percent()} %')
        print(f'CPU STATS: {psutil.cpu_stats()}')
        print(f'RAM usage: {psutil.virtual_memory().percent} %')
    return wrapper
