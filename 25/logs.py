date: 2020-12-14 21:37
not working yet
UnableToWorkException
Traceback (most recent call last):
  File "app.py", line 22, in <module>
    python_jun.work()
  File "/Users/antonhryb/Desktop/level/homework/24/models/employee.py", line 120, in work
    raise UnableToWorkException()
models.employee.UnableToWorkException: not working yet
date: 2020-12-17 21:17
'datetime.datetime' object has no attribute 'days'
AttributeError
Traceback (most recent call last):
  File "app.py", line 23, in <module>
    print(programmist1.full_str)
  File "/Users/antonhryb/Desktop/level/homework/25/models/employee.py", line 61, in full_str
    already_worked = dt.datetime.now().days
AttributeError: 'datetime.datetime' object has no attribute 'days'
