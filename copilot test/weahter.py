# import the module
import python_weather
import asyncio

def convert_from_farenheit(temp):
    return (temp - 32) * 5 / 9


async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("Neumarkt in der Steiermark")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature, weather.current.wind_speed, weather.current.sky)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())






