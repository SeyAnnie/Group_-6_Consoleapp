BASE_URL_2 = "https://covid-api.com/api/"
 
#main function for covid API using the get_data function
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
    if choice == "4":
        exit()
    elif choice == "3":