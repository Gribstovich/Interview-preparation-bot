import sqlite3
from typing import Any

from bot.config import load_config
from bot.misc.custom_exceptions import InvalidArgumentPassed

_config = load_config()
_conn = sqlite3.connect(_config.misc.path_to_db)
_cursor = _conn.cursor()


async def insert(table: str, column_values: dict[str, Any]):
    if isinstance(table, str) and isinstance(column_values, dict):
        columns = ', '.join(column_values.keys())
        values = [tuple(column_values.values())]
        placeholders = ', '.join('?' * len(column_values.keys()))
        _cursor.executemany(
            f'INSERT INTO {table} '
            f'({columns}) '
            f'VALUES ({placeholders})',
            values)
        _conn.commit()
    else:
        raise InvalidArgumentPassed('Type of table MUST be a str, type of column_values MUST be a dict[str, Any].')


async def fetchall(table: str, columns: list[str]) -> list[dict[str, Any]]:
    if isinstance(table, str) and isinstance(columns, list):
        columns_joined = ', '.join(columns)
        _cursor.execute(f'SELECT {columns_joined} FROM {table}')
        rows = _cursor.fetchall()
        result = []
        for row in rows:
            dict_row = {}
            for index, column in enumerate(columns):
                dict_row[column] = row[index]
            result.append(dict_row)
        return result
    else:
        raise InvalidArgumentPassed('Type of table MUST be a str, type of columns MUST be a list[str].')


async def delete(table: str, row_id: int) -> None:
    if isinstance(table, str) and isinstance(row_id, int):
        row_id = int(row_id)
        _cursor.execute(f'DELETE FROM {table} WHERE rowid={row_id}')
        _conn.commit()
    else:
        raise InvalidArgumentPassed('Type of table MUST be a str, type of row_id MUST be an int.')
