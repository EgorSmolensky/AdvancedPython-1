import application.salary as salary
import application.db.people as people
from datetime import date


if __name__ == '__main__':
    print(date.today().strftime('%d.%m.%Y'))
    salary.calculate_salary()
    people.get_employees()
