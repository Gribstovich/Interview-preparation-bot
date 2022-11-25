import sqlite3

from bot.config import load_config


def create_db() -> None:
    config = load_config()
    with sqlite3.connect(config.misc.path_to_db) as connection:
        cur = connection.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER NOT NULL PRIMARY KEY)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER REFERENCES categories(category_id),
        task_name TEXT NOT NULL,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        photo_path TEXT,
        file_id TEXT,
        telegraph_url TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS selected_categories (
        user_id INTEGER REFERENCES users(user_id),
        category_id INTEGER REFERENCES categories(category_id))''')

        cur.execute('''CREATE TABLE IF NOT EXISTS favorites_tasks (
        user_id INTEGER REFERENCES users(user_id),
        task_id INTEGER REFERENCES tasks(task_id))''')

        cur.execute('''CREATE TABLE IF NOT EXISTS user_config (
        user_id INTEGER REFERENCES users(user_id),
        favorites TEXT NOT NULL DEFAULT 'FALSE',
        prefer_telegraph TEXT NOT NULL DEFAULT 'FALSE')''')
