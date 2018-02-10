import sqlite3
import os.path as Path

SQL_SELECT_ALL = '''
select id, task, created, closed
from daily
'''

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

SQL_SELECT_ACTIVE_TASKS = SQL_SELECT_ALL + ' WHERE closed is NULL'

SQL_INSERT_TASK = '''
insert into daily (task) values (?)
'''

SQL_UPDATE_TASK = '''update daily set task=? where id=?
'''
SQL_CLOSE_TASK = '''update daily set closed=CURRENT_TIMESTAMP where id=?
'''
SQL_RESTART_TASK = '''update daily set created=CURRENT_TIMESTAMP, closed=NULL where id=?
'''


def connect(db_name=None):
    """    Устанавливаем соединение с БД    тройные двойные кавычки перед кодом - блок документации"""
    if db_name is None:
        db_name = ':memory:'
    conn = sqlite3.connect(db_name)
    # вжух
    return conn


def initialize(conn, creation_script=None):
    """Иницилизирует структуру БД"""
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__), 'resources', 'schema.sql')

    with conn, open(creation_script) as f:
        conn.executescript(f.read())


def add_task(conn, task):
    """Добавляет задание в БД"""
    if not task:
        raise RuntimeError('Нужно записать задание в ежеденевник!')  # выбрасываем исключение
    with conn:
        conn.execute(SQL_INSERT_TASK, (task, ))
        # pk = cursor.lastrowid   # лежит последний вставленный идентификатор
        # short_url = '{}/{}'.format(domain.strip('/'), pk)
        # conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))
    return task

# def find_url_by_origin(conn, url):
#     """ Найти короткий url-адрес по оригинальному """
#     url = url.strip('/')
#     with conn:
#         cursor = conn.execute(SQL_SELECT_URL_BY_ORIGIN, (url, ))
#         return cursor.fetchone()


def edit_task(conn, task, id_task):
    with conn:
        conn.execute(SQL_UPDATE_TASK, (task, id_task))
    return task


def show_all(conn):
    """Найти все адреса в БД"""
    with conn:
        return conn.execute(SQL_SELECT_ALL).fetchall()


def close_task(conn, id_task):
    with conn:
        conn.execute(SQL_CLOSE_TASK, (id_task))
    return id_task


def restart_task(conn, id_task):
    with conn:
        conn.execute(SQL_RESTART_TASK, (id_task))
    return id_task


def show_active(conn):
    with conn:
        return conn.execute(SQL_SELECT_ACTIVE_TASKS).fetchall()
