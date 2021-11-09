def get_url():
    city = input("Please enter a city name: ")
    state_abbreviation = input("Please enter a two letter state abbreviation: \n")

    city_title = city.title()
    global city_final_name
    city_final_name = city_title.replace(' ', '-')

    state_abbreviation_final = state_abbreviation.upper()

    url = f"https://www.myvisajobs.com/{city_final_name}-{state_abbreviation_final}-2021WC.htm"
    return(url)

# remote test change