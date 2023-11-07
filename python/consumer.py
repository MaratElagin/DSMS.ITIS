import json
import pulsar
from weatherMessage import WeatherMessage
from pulsar.schema import JsonSchema
import psycopg2

# Загрузка секретных данных из secrets.json.
with open('python/secrets/secrets.json', 'r') as secrets_file:
    db_connection_string = json.load(secrets_file)["db_params"]

# Скрипт создания таблицы Weather.
with open('python/weatherTableInit.sql', 'r') as sql_file:
    create_weather_table = sql_file.read()


def write_weather_to_db(weather_message):
    conn = None
    try:
        # Коннектимся к базе Postgresql.
        conn = psycopg2.connect(**db_connection_string)
        
        # Создаем курсор для выполнения SQL-запросов.
        cursor = conn.cursor()

        cursor.execute(create_weather_table)

        # Вставка данных о погоде в таблицу weather.
        insert_query = "INSERT INTO weather(id, temperature, wind_speed) VALUES (%s, %s, %s)"
        
        if hasattr(weather_message, "wind_speed"):
            wind_speed = weather_message.wind_speed
        else:
            wind_speed = None
        
        data = (weather_message.id, weather_message.temperature, wind_speed)
        cursor.execute(insert_query, data)

        # Завершаем транзакцию.
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print(f"Ошибка при записи в базу данных: {error}")
    finally:
        if conn is not None:
            conn.close()

client = pulsar.Client('pulsar://localhost:6650')

try:
    consumer = client.subscribe(
                    topic='weather-topic',
                    subscription_name='my-subscription',
                    schema=JsonSchema(WeatherMessage))

    while True:
        weather_message = consumer.receive()
        print(weather_message.value())
        write_weather_to_db(weather_message.value())
        consumer.acknowledge(weather_message)
            
finally:
    client.close()