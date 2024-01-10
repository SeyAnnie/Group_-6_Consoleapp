# Contributor: Precious Nnodi
# Numbers API and Covid-19 Tracker Integration

## Explaining what this Repository is about

This repository contains a powerful integration of the Numbers API and a Covid-19 Tracker app, providing users with a comprehensive tool to explore numerical trivia and real-time Covid-19 statistics. Whether you're a developer, data enthusiast, or someone interested in staying informed about the global pandemic, this integration offers a seamless and intuitive experience. 
This documentation explains 3 parts of this project, so let's dive right in:
1.	Numbers API
2.	Covid-19 Tracker App
3.	API Integration

## Numbers API
This API is for interesting facts about numbers. We picked this because it can be used to bring interesting facts about metrics and stories about dates. When used with the COVID-19 tracker app, it can bring interesting information about the metrics and dates. 

### Numbers API Integration
On this project, we got the url for the Api from the website; http://numbersapi.com/, then went ahead to define  the function on VS Code:
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
        data = response.read().decode()

‘’’’COVID 19 Tracker App
leverages data from the Covid-19 API to provide real-time and historical information about the global Covid-19 pandemic. It serves as a valuable tool for users seeking accurate and up-to-date statistics on the spread of the virus at both a global and country-specific level. 

“””Covid-19 API Integration
We got the Url for the website; https://covid-api.com/api/, then went ahead to define the function for the Api:
def get_data(date=None, iso=None):
    url = BASE_URL_2 + "reports/total?date=" + date
    if iso:
        url += "&iso=" + iso
    print("Fetching data...")
    with urlopen(url) as response:
        data = response.read()
    data = eval(data)
    data = data["data"]

We then proceeded to define the main function for the API using the get data function, which directs you to the choice of information you would like to get about the COVID19 Pandemic: 
def covid19():
    print(
        """Welcome to the COVID-19 Tracker App
        Please select from the following options:
        1. Global Data
        2. Country Data
        3. See the list of countries
        4. Exit
        """
    )
    choice = input("Enter your choice: ")

“” API Integration
We worked on integrating the two apps to work concurrently. So that you can get data about the covid19 pandemic, as well as get interesting facts about the dates from the pandemic, using the numbers API.
We called the function for this, which means, you could select which of the APIs you want to use.
if __name__ == "__main__":
    while True:
        print(
            """
            Welcome to the Group 6 Python Console App.
            Please choose which API you want to use.
            1 - Numbers App
            2 - COVID-19 App
            3 - Exit Program
            """
        )
        tmp = input("Enter a number: ")
        
        if tmp == "1":
            while True:
                numbersapi_url()
                print("\n")
                cont = input("Do you want to continue using Numbers API? (y/n): ")
                if cont.lower() == "n":
                    break
        elif tmp == "2":
            while True:
                covid19()
                print("\n")
                cont = input("Do you want to continue using COVID-19 API? (y/n): ")
                if cont.lower() == "n":
                    break
        elif tmp == "3":
            print("Exiting program.")
            break


##### Git Repository
We completed this project by cloning the git repository, using:
 git clone https://github.com/SeyAnnie/Group_-6_Consoleapp.git
 
##### Contributors
Team Lead
Precious Nnodi

Team Members
Aniedi Bassey
Favor Alozie
Adeola Adeagbo
Sherifat Sanni
Vessina Udoh 
Onyinye Alago
