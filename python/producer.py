import pulsar
import sys
from weatherMessage import WeatherMessage
from pulsar.schema import JsonSchema

client = pulsar.Client('pulsar://localhost:6650')

try: 
    producer = client.create_producer('weather', schema=JsonSchema(WeatherMessage))
    
    id = 1
    for line in sys.stdin:
        line = line.strip()
        try:
            temperature = int(line.split()[0])
            wind_speed = float(line.split()[1])
        except (IndexError):
            temperature = int(line.split()[0])
            wind_speed = None
        
        weather_message = WeatherMessage(id = id, temperature = temperature, wind_speed = wind_speed)

        print(weather_message)
        producer.send(weather_message)
        id += 1

finally:
    client.close()