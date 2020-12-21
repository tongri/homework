import sys
import datetime as dt
from models.employee import Programmer, Recruiter, Candidate, Vacancy, UnableToWorkException
import traceback


if __name__ == '__main__':

	try:
		programmist1 = Programmer('Anthony', 'antoha@', 100, True, {'c++', 'php', 'js', 'python'})
		programmist2 = Programmer('Sergey', "antoha@", 800, True, {'c#', 'python', 'html'})

		recruit1 = Recruiter('Alexey', 'alex', 200, False)

		python_jun = Candidate('Pavel', 'pavel@', {'oracle', 'django'}, 'python', 6)
		js_jun = Candidate('Nikita', 'nikita@', {'oracle', 'django'}, 'python', 5)
		cpp_middle = Candidate('Daniil', 'daniil@', {'c++', 'c#', 'ruby'}, 'c++', 2)

		python_vacancy = Vacancy('needs a python developer', 'python', 5)
		js_vacancy = Vacancy('needs a js developer', 'js', 6)

		python_jun.work()

	except Exception as error:
		with open('logs.py', 'a+') as file:
			tb = traceback.format_exc()
			day = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
			file.write(f'date: {day}\n{str(error)}\n{type(error).__name__}\n{tb}')