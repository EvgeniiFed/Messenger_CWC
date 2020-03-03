# from checker import check_list
from theory import checker
import datetime
print(checker.check_list([1, 3, 4, 6]))
print(checker.check_list([1, 3, -4, 6]))

print(datetime.datetime.now())
print(type(datetime.datetime.now()))
print(str(datetime.datetime.now()))
print(type(str(datetime.datetime.now())))