# I defined the number Api

from urllib.request import urlopen
from datetime import datetime
import json

#function for numbers api
def numbersapi_url():
    BASE_URL_1 = "http://numbersapi.com/"
    print("""
        Welcome to the Numbers App
        Input the day and month you want to know about.
        """)
    month = int(input("Enter a month(1-12): "))

    day = int(input("Enter a day(1-31): "))
    url = BASE_URL_1 + str(month) + "/" + str(day) + "/date"  # Corrected URL

    with urlopen(url) as response:
        data = response.read().decode()  # Decoding the response to a string

    # If the API returns JSON, parse it with json.loads. If it's plain text, adjust accordingly.
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        # Handle plain text or other formats here
        pass

    print(data)