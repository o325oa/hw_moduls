from application.salary import calculate_salary
from application.db.people import get_emp
from datetime import datetime


def time():
    now = datetime.now()
    format_date = now.strftime("%Y-%m-%d")
    print(f'Текущая дата: {format_date}')
if __name__ == '__main__':
    print("Программа Бухгалтерия успешно запущена")
    calculate_salary()
    get_emp()
    time()

