***Task 1***: June – Python Voice Assistant

June is a Python-based voice assistant that can greet you, listen to your commands, and respond using speech. It can perform tasks like searching Wikipedia, opening websites such as Google and YouTube, and telling the current time. The assistant uses SpeechRecognition to understand voice commands and pyttsx3 for text-to-speech responses.

How it Works:

When you run June, it first greets you based on the current time. It then continuously listens to your voice commands through the microphone. Commands are converted to text using the SpeechRecognition library. Based on your command, June can fetch information from Wikipedia, open web pages, or tell the current time. You can stop the assistant at any time by saying “exit,” “quit,” or “stop.”

To use June, clone the repository, install the required Python packages, and run the program. Speak commands like “Open Google,” “Search Wikipedia for Albert Einstein,” “What is the time?” or “Exit” to interact with the assistant.

===========================================================================================================================================

***Task 2***: BMI Calculator

A simple command-line BMI (Body Mass Index) calculator written in Python. This program allows users to input their weight in kilograms and height in feet to calculate their BMI and determine their health category.

The calculator uses the standard BMI formula:
BMI = weight (kg)/height (m)^2

Since height is entered in feet, the program automatically converts it to meters before calculating the BMI.

Features:
1. Input weight in kilograms and height in feet.
2. Automatic conversion from feet to meters.
3. Calculates BMI and displays it rounded to two decimal places.
4. Classifies BMI into categories:
    -Underweight
    -Normal weight
    -Overweight
    -High BMI
5. Handles invalid or non-numeric inputs gracefully.

===========================================================================================================================================

***Task 3***: Password Generator

A simple command-line password generator written in Python. This program allows users to create secure, random passwords based on their preferred length and character types, including letters, numbers, and symbols. 

The generator uses Python's random module to randomly select characters from the allowed character sets specified by the user.

Features:
1. Input desired password length.
2. Option to include letters (both uppercase and lowercase).
3. Option to include numbers (0-9).
4. Option to include symbols (e.g., !@#$%^&*).
5. Generates a random password based on selected criteria.
6. Handles invalid inputs, such as non-positive lengths or no character types selected.
7. Displays the generated password directly in the command line.

===========================================================================================================================================

***Task 4***: Weatheria – Your Personal Weather App

Weatheria is a Python-based terminal weather application that provides real-time weather information for any city. It can automatically detect your current location based on your IP if no city is entered. The app displays temperature, humidity, and weather conditions and runs in a continuous loop until the user types “exit.” The application securely hides the API key using environment variables.

How it Works:

When you run Weatheria, it first displays a welcome message. It then prompts the user to enter a city name. If no city is provided, Weatheria attempts to detect the current location automatically. Using the OpenWeatherMap API, the app fetches the latest weather data for the city and displays the temperature, humidity, and weather condition. The program continues running in a loop, allowing you to check multiple cities, until you type “exit” to quit. The API key is stored in a `.env` file or system environment variable to keep it secure.

To use Weatheria:

1. Clone the repository.
2. Create a `.env` file in the project root and store your API key as:
     `api_key = (Your API Key)`
3. Install the required Python packages: `requests` and `python-dotenv`.
4. Run the program and enter a city name or leave blank to use your current location. Type “exit” to quit.

===========================================================================================================================================




