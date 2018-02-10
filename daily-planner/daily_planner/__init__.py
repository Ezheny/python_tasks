import sys

from daily_planner import storage

get_connection = lambda: storage.connect('daily.sqlite')    # функция автоматически возвращает значение - return не нужен


def action_add():
    """ Добавить задачу """
    task = input('\nВведите новую задачу: ')
    with get_connection() as conn:
        new_task = storage.add_task(conn, task)
    print('Новая задача: {}'.format(new_task))


def action_edit():
    """ Отредактировать задачу """
    id_task = input('\nКакую задачу нужно отредактировать? ')
    task = input('\nНовая формулировка задачи: ')
    with get_connection() as conn:
        new_task = storage.edit_task(conn, task, id_task)
    print('Задача отредактирована: {}'.format(new_task))


def action_find_all():
    """ Вывести все задачи """
    with get_connection() as conn:
        tasks = storage.show_all(conn)
    # print(tasks)
    for task in tasks:
        template = '{task[0]} - {task[1]} - {task[2]} - {task[3]}'
        print(template.format(task=task))


def action_find_active():
    """ Вывести все активные задачи """
    with get_connection() as conn:
        tasks = storage.show_active(conn)
    for task in tasks:
        template = '{task[0]} - {task[1]} - {task[2]} - {task[3]}'
        print(template.format(task=task))


def action_exit():
    """ Выход """
    sys.exit(0)     # 0 - отсутствие ошибок при выходе программы


def action_restart():
    """Начать задачу сначала"""
    id_task = input('\nКакую задачу нужно начать сначала? ')
    with get_connection() as conn:
        restarted_task = storage.restart_task(conn, id_task)
    print('{} задача снова активна '.format(restarted_task))


def action_close():
    """Завершить задачу"""
    id_task = input('\nКакую задачу нужно отредактировать? ')
    with get_connection() as conn:
        closed_task = storage.close_task(conn, id_task)
    print('{} задача завершена '.format(closed_task))


def action_active():
    """Вывести список активных задач"""


def action_show_menu():
    """ Отображает меню """
    print('''
    1. Вывести список задач
    2. Добавить задачу
    3. Отредактировать задачу
    4. Завершить задачу
    5. Начать задачу сначала
    6. Вывести список активных задач
    7. Выход
    ''')


def main():
    with get_connection() as conn:
        storage.initialize(conn)
    actions = {
    '1': action_find_all,
    '2': action_add,
    '3': action_edit,
    '4': action_close,
    '5': action_restart,
    '6': action_find_active,
    '7': action_exit,
    }
    action_show_menu()
    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)
        if action:
            try:
                action()
            except Exception as e:
                print(e)
        else:
            print('Неизвестная команда')

