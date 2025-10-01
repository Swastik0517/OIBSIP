import requests
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

def detect_city():
    try:
        res = requests.get("https://ipinfo.io/json")
        if res.ok:
            city = res.json().get("city")
            return city
    except:
        return None
    return None

def main():
    configure()
    print("=====Welcome to Weatheria — Your Personal Weather App=====\n")

    while True:
        city_name = input("Enter city name (leave blank for current location, type 'exit' to quit): ").strip()

        if city_name.lower() == "exit":
            print("Goodbye!")
            break

        if not city_name:
            city_name = detect_city()
            if city_name:
                print(f"Using your current location: {city_name}")
            else:
                city_name = input("Could not detect location. Please enter a city: ").strip()
                if city_name.lower() == "exit":
                    print("Goodbye!")
                    break

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            print(f"\nWeather in {city_name}:")
            print('Temperature:', data['main']['temp'], '°C')
            print('Humidity:', data['main']['humidity'], '%')
            print('Condition:', data['weather'][0]['description'].title())
            print()  # <-- blank line after each output

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}\n")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}\n")
        except KeyError:
            print("Could not retrieve weather data. Check city name or API key.\n")

if __name__ == "__main__":
    main()
