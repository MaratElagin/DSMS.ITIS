from pulsar.schema import Record, Double, Integer

class WeatherMessage(Record):
    id = Integer()
    temperature = Integer()
    wind_speed = Double()
    
    def __str__(self):
        functional_vars = {
            'id': self.id,
            'temperature': self.temperature,
            'wind_speed': self.wind_speed
        }
        return str(functional_vars)