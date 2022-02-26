import mysql.connector
import settings


async def create_database(client):
    mydb = mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD
    )

    dbcursor = mydb.cursor()

    dbcursor.execute("CREATE DATABASE IF NOT EXISTS " + settings.DB_NAME + " CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")

    await client.get_channel(settings.LOG_CHANNEL).send('DATABASE : ' + settings.DB_NAME + ' **initialised**')


async def create_tables(client):
    settings.DB_CURSOR.execute("CREATE TABLE IF NOT EXISTS feeds_types ("
                               "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
                               "type VARCHAR(25)"
                               ") ENGINE = INNODB")

    await client.get_channel(settings.LOG_CHANNEL).send('TABLE : feeds_types **initialised**')

    settings.DB_CURSOR.execute("CREATE TABLE IF NOT EXISTS feeds ("
                               "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
                               "title VARCHAR(255),"
                               "feeds_types_id INT,"
                               "FOREIGN KEY(feeds_types_id) REFERENCES feeds_types(id)"
                               ") ENGINE = INNODB")

    await client.get_channel(settings.LOG_CHANNEL).send('TABLE : feeds **initialised**')

    settings.DB_CURSOR.execute("CREATE TABLE IF NOT EXISTS users ("
                               "id BIGINT PRIMARY KEY NOT NULL,"
                               "points INT"
                               ") ENGINE = INNODB")

    await client.get_channel(settings.LOG_CHANNEL).send('TABLE : users **initialised**')


async def populate_tables(client):
    sql = "INSERT INTO feeds_types (id, type) VALUES (%s, %s)"
    val = [
        (1, 'patchnote'),
        (2, 'esport')
    ]

    try:
        settings.DB_CURSOR.executemany(sql, val)
        settings.DB.commit()
    except:
        pass

    await client.get_channel(settings.LOG_CHANNEL).send('TABLES **populated**')


async def init_db(client):
    await create_database(client)
    settings.connect_db()

    await create_tables(client)
    await populate_tables(client)
