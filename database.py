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
    mydb = mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )

    dbcursor = mydb.cursor()

    dbcursor.execute("CREATE TABLE IF NOT EXISTS feeds ("
                     "id INT PRIMARY KEY NOT NULL,"
                     "title VARCHAR(255),"
                     "feeds_types_id INT "
                     ") ENGINE = INNODB")

    await client.get_channel(settings.LOG_CHANNEL).send('TABLE : feeds **initialised**')


async def init_db(client):
    await create_database(client)
    await create_tables(client)
