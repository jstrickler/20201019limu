from datetime import datetime
from functools import wraps
import logging

logging.basicConfig(filename="liberty.log", level=logging.INFO)

logging.info("Starting program")

def ham(old_func):

    def new_func(*args):
        result = old_func()
        return 2 * result

    return new_func

@ham
def spam():
    logging.debug("calling spam")
    print("hello from spam()")
    return 100
# spam = ham(spam)

result = spam()  # what are we calling
print(result)
print("spam after decorating:", spam.__name__)

def timestamp(func):

    @wraps(func)  # update replacement with name of func
    def replacement(*args, **kwargs):
        print("==> {} called at {}".format(
            func.__name__, datetime.now()
        ))
        return func(*args, **kwargs)

    return replacement

@timestamp
def foo(value):
    print("hello from foo()")

@timestamp
def bar():
    print("hello from bar()")

foo(1)
foo(2)
bar()
foo(3)
foo(4)
bar()
bar()
print(foo.__name__, bar.__name__)

def timestamp_to_log(level):

    def deco(func):

        @wraps(func)
        def replacement(*args, **kwargs):
            message = "{} called at {}".format(
                func.__name__, datetime.now()
            )
            if hasattr(logging, level):
                logging_func = getattr(logging, level)
                logging_func(message)
            else:
                raise ValueError("Invalid debugging level")
            return func(*args, **kwargs)

        return replacement

    return deco


@timestamp_to_log('debug')
def fee():
    pass

@timestamp_to_log('info')
def fi():
    pass

@timestamp_to_log('critical')
def fo():
    pass

fee()
fi()
fo()
fee()
fo()
fi()

