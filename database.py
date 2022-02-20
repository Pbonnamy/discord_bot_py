import mysql.connector
import settings


async def create_database(client):
    mydb = mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD
    )

    dbcursor = mydb.cursor()

    dbcursor.execute("CREATE DATABASE IF NOT EXISTS " + settings.DB_NAME)

    await client.get_channel(settings.LOG_CHANNEL).send('Database : ' + settings.DB_NAME + ' **initialised**')


async def init_db(client):
    await create_database(client)



