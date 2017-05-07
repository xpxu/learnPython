import datetime
import functools

def GetRunTime(func):
    @functools.wraps(func)
    def check(*args, **args2):
        startTime = datetime.datetime.now()
        func(*args,**args2)
        endTime = datetime.datetime.now()
        print(endTime-startTime)
    return check

@GetRunTime
def test():
     print("hello world")

test()
