from typing import List

import helpers
import models


class Database:
    path = 'person.txt'

    def save(self, content):
        with open(self.path, 'a') as file:
            file.write(content)

    def all(self) -> List['models.Person']:
        person_list = []
        with open(self.path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                columns = line.split(';')

                person = models.Person()
                person.name = columns[0]
                person.gender = columns[1]
                person.salary = float(columns[2])
                person.date_birth = helpers.transform_date(columns[3])

                person_list.append(person)

        return person_list
