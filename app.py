import helpers
import models
import utils


class Menu:
    option = -1

    def __init__(self):
        self.database = utils.Database()

    def add(self):
        person = models.Person()
        person.name = input('Name: ')
        person.gender = input('Gender: ')
        person.salary = float(input('Salary: '))
        person.date_birth = helpers.transform_date(input('Date birth (YYYY-MM-DD): '))
        self.database.save(str(person))

    def list(self):
        for person in self.database.all():
            print(
                ' Name: ', person.name, '\n',
                'Gender: ', person.gender, '\n',
                'Salary: ', person.salary, '\n',
                'Date birth: ', person.date_birth, '\n',
                'Age: ', person.age, '\n\n'
            )

    def sum_male(self):
        print('Male salary: ', sum(map(
            lambda person: person.salary,
            filter(
                lambda item: item.gender == 'M',
                self.database.all()
            )
        )))

    def sum_famale(self):
        print('Famale salary: ', sum(map(
            lambda person: person.salary,
            filter(
                lambda item: item.gender == 'F',
                self.database.all()
            )
        )))

    def show(self):
        while not self.option == 0:
            print('1 - Add employee')
            print('2 - Employee list')
            print('3 - Sum male salary')
            print('4 - Sum famale salary')
            self.option = int(input('Option: '))

            print('\n')

            if self.option == 1:
                self.add()
            elif self.option == 2:
                self.list()
            elif self.option == 3:
                self.sum_male()
            elif self.option == 4:
                self.sum_famale()
            else:
                if not self.option == 0:
                    print('Invalid option')


menu = Menu()
menu.show()
