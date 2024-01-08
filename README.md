# Python Console App Assignment - Team [Group 6]
## API Selection:
Numbers API: Utilized in the numbersapi_url() function, fetching interesting facts about a specified date.
COVID-19 API: Used in the get_data() function and the covid19() main function, retrieving global or country-specific COVID-19 data.
## Unique Problem or Scenario:
It involved providing interesting facts about a user-specified date (Numbers API) and tracking COVID-19 data globally or for specific countries.
## Coding Practices:
Comments: Code includes comments explaining the purpose of specific sections and providing context.
Variable Naming: Variable names like BASE_URL_1 and BASE_URL_2 are meaningful.
## Code Formatting: Generally follows good code formatting practices.
Boolean Values and Branching Logic: Uses boolean values in the main loop for user interaction (cont.lower() == "n").
## Data Structure: Utilizes data structures like dictionaries to store and display COVID-19 data.
Loops: Employs loops (while True and for country in countries) to manage program flow.
## API Integration:
Numbers API Integration: Achieved in the numbersapi_url() function by constructing a URL based on user input and fetching data using urlopen.
COVID-19 API Integration: Implemented in the get_data() function, constructing a URL based on date and country ISO code and fetching data using urlopen.
## Module Usage:
urllib Module: Imported for working with URLs (from urllib.request import urlopen).
datetime Module: Imported for handling date-related functionality (from datetime import datetime).
json Module: Used to parse JSON data from the API responses (import json).
