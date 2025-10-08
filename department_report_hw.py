from typing import List, Dict
import csv


def csv_read(
    filename: str = 'Corp_Summary.csv',
) -> List[Dict]:
    """Принимает на вход csv файл и выдает список словарей.

    Args:
        filename (str, optional): Имя файла. Defaults to "Corp_Summary.csv".

    Returns:
        List[Dict[str, str, str, str, str, str]]: список словарей, содержащих информацию о сотрудниках
    """
    with open(filename) as csv_file:
        input_file = csv.DictReader(csv_file, delimiter=';')
        data = []
        for row in input_file:
            data.append(row)
    return data


def display_teams(data: List[Dict]):
    """Выводит данные о департаментах и командах.

    Args:
        data (List[Dict]): список словарей с данными о работниках
    """
    departments_teams = {}
    for worker in data:
        department = worker['Департамент']
        team = worker['Отдел']
        if department not in departments_teams:
            departments_teams[department] = set()
        departments_teams[department].add(team)
    for department in departments_teams:
        print(f'{department}:')
        for team in departments_teams[department]:
            print(f'\t{team}')
        print('-' * 100)


def department_report(data: List[Dict]) -> Dict[str, Dict]:
    """Генерирует и выдает словарь с данными о департаментах.

    Args:
        data (List[Dict[str, str,str,str,str,str]]): Список словарей с данными о работниках

    Returns:
        Dict[str, Dict[str, str, str]]: Словарь: ключ - департамент, значения - другой словарь со следующими характеристиками: численность, вилка, средняя зарплата
    """
    report = {}
    for worker in data:
        department = worker['Департамент']
        salary = int(worker['Оклад'])
        if department not in report:
            report[department] = {
                'size': 0,
                'min_salary': salary,
                'max_salary': salary,
                'total_salary': 0,
            }
        report[department]['size'] += 1
        report[department]['total_salary'] += salary
        report[department]['min_salary'] = min(
            report[department]['min_salary'], salary
        )
        report[department]['max_salary'] = max(
            report[department]['max_salary'], salary
        )
            # Создаю итоговый вид словаря, добавляя среднюю зарплату и вилку
    for department in report:
        report[department]['average_salary'] = round(
            report[department]['total_salary'] / report[department]['size'], 2
        )
        report[department]['fork'] = (
            f'{report[department]['min_salary']}-{report[department]['max_salary']}'
        )
    return report


def display_department_report(report: Dict[str, Dict]):
    """С выравниванием печатает сводный отчет о департаментах."""
    # Для выравнивания задаю ширину столбцов
    col_widths = [12, 12, 14, 17]
    header = (
        f'{"Название".ljust(col_widths[0])}{"Численность".ljust(col_widths[1])}'
        f'{"Вилка".center(col_widths[2])}{"Средняя зарплата".ljust(col_widths[3])}'
    )
    print(header)
    print('-' * sum(col_widths))
    for department, stats in report.items():
        row = (
            f'{department.ljust(col_widths[0])}'
            f'{str(stats["size"]).center(col_widths[1])}'
            f'{str(stats["fork"]).ljust(col_widths[2])}'
            f'{str(stats["average_salary"]).ljust(col_widths[3])}'
        )
        print(row)


def save_to_csv(
    report: Dict[str, Dict], filename: str = 'department-report.csv'
):
    """Сохраняет отчет в csv файл.

    Args:
        report (Dict[str, Dict]): отчет
        filename (str, optional): путь к файлу. Defaults to
        'department-report.csv'.
    """
    with open(filename, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Отдел', 'Размер', 'Вилка', 'Средняя зарплата'])
        for department, stats in report.items():
            writer.writerow([
                department,
                stats['size'],
                stats['fork'],
                stats['average_salary'],
            ])
    print(f'Ваш отчет сохранился в {filename}')


def menu():
    """Печатает меню"""
    data = csv_read()
    report = department_report(data)
    while True:
        print('\nМеню:')
        print('1. Вывести в понятном виде иерархию команд')
        print('2. Вывести сводный отчет по департаментам')
        print('3. Сохранить сводный отчет в виде CSV-файла')
        print('0. Выход')

        choice = int(input('Выберите пункт меню: '))
        print()
        if choice == 1:
            display_teams(data)
        elif choice == 2:
            display_department_report(report)
        elif choice == 3:
            save_to_csv(report)
        elif choice == 0:
            print('До свидания!')
            break
        else:
            print('Некорректный выбор. Попробуйте снова.')


if __name__ == '__main__':
    menu()
