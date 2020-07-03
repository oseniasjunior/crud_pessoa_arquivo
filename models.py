from datetime import datetime


class Person:
    def __init__(self, name=None, gender=None, date_birth=None, salary=None):
        self.name = name
        self.gender = gender
        self.date_birth = date_birth
        self.salary = salary

    @property
    def age(self):
        _now = datetime.now().date()
        diff = _now - self.date_birth
        return int(diff.days / 365)

    def __repr__(self):
        return '{name};{gender};{salary};{date_birth};\n'.format(
            name=self.name,
            gender=self.gender,
            salary=self.salary,
            date_birth=self.date_birth
        )
