import sys
from models.employee import Programmer, Recruiter, Candidate, Vacancy


if __name__ == '__main__':

	programmist1 = Programmer('Anthony', 'antoha@', 100, True, {'c++', 'php', 'js', 'python'})
	programmist2 = Programmer('Sergey', "sergey@", 800, True, {'c#', 'python', 'html'})

	recruit1 = Recruiter('Alexey', 'alex', 200, False)

	python_jun = Candidate('Pavel', 'pavel@', {'oracle', 'django'}, 'python', 6)
	js_jun = Candidate('Nikita', 'nikita@', {'oracle', 'django'}, 'python', 5)
	cpp_middle = Candidate('Daniil', 'daniil@', {'c++', 'c#', 'ruby'}, 'c++', 2)

	python_vacancy = Vacancy('needs a python developer', 'python', 5)
	js_vacancy = Vacancy('needs a js developer', 'js', 6)