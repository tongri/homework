import sys
import datetime as dt
from models.employee import Programmer, Recruiter, Candidate, Vacancy, UnableToWorkException, Employee
import traceback


if __name__ == '__main__':

	programmist1 = Programmer('Anthony', 'antoha@', 100, True, {'c++', 'php', 'js', 'python'})
	#print(programmist1.full_str)
	#print(Employee.count_working_days())
	b = Candidate.create_from_csv("candidates.csv")
	for x in b:
		print(x.technologies)
	#python_jun.work()