from sqlalchemy import create_engine, MetaData, Table

engine = create_engine("postgresql://postgres:123123@localhost:5432/postgres")

metadata = MetaData()
metadata.reflect(bind=engine)

# Назва таблиці, яку хочеш видалити
table_to_drop = Table("alembic_version", metadata, autoload_with=engine)

# Видалення таблиці
table_to_drop.drop(engine)

print("Таблицю успішно видалено.")
