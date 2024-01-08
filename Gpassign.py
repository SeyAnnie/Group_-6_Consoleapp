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
        # Get list of countries
        with urlopen(BASE_URL_2 + "regions") as resp:
            body = resp.read()
        countries = eval(body)["data"]
        for country in countries:
            print(f'{country["iso"]}: {country["name"]}')
    elif choice == "1":
        date_input = input("Enter the date in YYYY-MM-DD forma(default to current date): ") or datetime.now().strftime(
            "%Y-%m-%d")
        # Get global data
        get_data(date_input)
    elif choice == "2":
        date_input = input("Enter the date in YYYY-MM-DD forma(default to current date): ") or datetime.now().strftime(
            "%Y-%m-%d")
        # Get country data
        country_iso = input("Enter the country code(NGA for Nigeria): ")
        get_data(date_input, country_iso)