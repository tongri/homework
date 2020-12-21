import datetime as dt


class UnableToWorkException(Exception):
	def __str__(self):
		return 'not working yet'


class Employee:
	def __init__(self, name, email, salary):
		self.validate_email(email)
		self.name = name
		self.email = email
		self.save_email()
		self.salary = salary

	def __lt__(self, other):
		return self.salary < other.salary

	def __le__(self, other):
		return self.salary <= other.salary

	def __gt__(self, other):
		return self.salary > other.salary

	def __ge__(self, other):
		return self.salary >= other.salary

	def __eq__(self, other):
		return self.salary == other.salary

	def __ne__(self, other):
		return self.salary != other.salary

	@staticmethod
	def count_working_days():
		td = dt.datetime.today()
		begin = dt.datetime(td.year, td.month, 1).weekday()
		entire = td.day // 7
		part = td.day % 7
		if part > 6 - td.weekday():
			part -= 2
		elif part > 7 - td.weekday():
			part -= 1
		return (part + (entire * 5))

	@property
	def full_str(self):
		already_worked = dt.datetime.now()
		begining = dt.datetime(already_worked.year, already_worked.month, 1)
		return f'{self.name} has already worked {(already_worked - begining).days + 1}'

	def validate_email(self, email):
		with open('mails.py', 'r') as file:
			print(file.read())
			if email in file.read():
				raise ValueError

	def save_email(self):

		with open('mails.py', 'w+') as file:
			file.write(self.email)

	def work(self):
		return 'I come to the office.'

	def check_salary(self):
		td = dt.datetime.today()
		begin = dt.datetime(td.year, td.month, 1).weekday()
		entire = td.day // 7
		part = td.day % 7
		if part > 6 - td.weekday():
			part -= 2
		elif part > 7 - td.weekday():
			part -= 1
		return (part + (entire * 5)) * self.salary


class Programmer(Employee):
	def __init__(self, name, email, salary, closed_this_month, tech_stack):
		super().__init__(name, email, salary)
		self.closed_this_month = closed_this_month
		self.tech_stack = tech_stack

	def work(self):
		return f'{super().work()[:-1]} and start coding'

	def __str__(self):
		return f'Rank: {__class__.__name__}'

	def __add__(self, other):
		return self.tech_stack | other.tech_stack

	def __lt__(self, other):
		return len(self.tech_stack) < len(other.tech_stack)

	def __le__(self, other):
		return len(self.tech_stack) <= len(other.tech_stack)

	def __gt__(self, other):
		return len(self.tech_stack) > len(other.tech_stack)

	def __ge__(self, other):
		return len(self.tech_stack) >= len(other.tech_stack)

	def __eq__(self, other):
		return len(self.tech_stack) == len(other.tech_stack)

	def __ne__(self, other):
		return len(self.tech_stack) != len(other.tech_stack)


class Recruiter(Employee):
	def __init__(self, name, email, salary, hired_this_month):
		super().__init__(name, email, salary)
		self.hired_this_month = hired_this_month

	def work(self):
		return f'{super().work()[:-1]} and start hiring'


	def __str__(self):
		return f'Rank: {__class__.__name__}'


class Offers():
	def __init__(self, main_skill, main_skill_level):
		self.main_skill = main_skill
		self.main_skill_level = main_skill_level


class Candidate(Offers):

	def __init__(self, full_name, email, technologies, main_skill, main_skill_level):
		super().__init__(main_skill, main_skill_level)
		self.full_name = full_name
		self.email = email
		self.technologies = technologies

	@classmethod
	def create_from_csv(cls, path):
		everything = []
		with open(path, "r") as file:
			for line in file:
				full_name, mail, tech_stack, main_skill, main_skill_level= line.rstrip().split(",")
				candidate = cls(full_name, mail, set(tech_stack.split("|")), main_skill, main_skill_level)
				everything.append(candidate)
			print(everything)
		return everything

	def work(self):
		raise UnableToWorkException()

	


class Vacancy(Offers):
	def __init__(self, title, main_skill, main_skill_level):
		super().__init__(main_skill, main_skill_level)
		self.title = title


if __name__ == '__main__':
	pass
 

