from bot import database as db


async def category_is_exists_check(category_name: str):
    existing_categories = await db.fetchall(table='categories', columns=['category_name'])
    return any(map(lambda category: category['category_name'] == category_name,
                   existing_categories))
