# Given a list of people with their birth year and death year,
# come up with a solution which shows the years with the highest population

# Assumption :
# - list of people object with name, birth_year, death_year



def highest_population_year(people):
    birth_years = {}
    for person in people: # iterate over peoples list
        # count the birth years
        if person['birth_year'] in birth_years:
            birth_years[person['birth_year']] += 1
        else:
            birth_years[person['birth_year']] = 1

        # substract death years.
        if person['death_year'] in birth_years:
            birth_years[person['death_year']] -= 1

    # Get the back value in the dictionary, return key
    return max(birth_years, key=birth_years.get)


if __name__ == '__main__':

    people = [
        {'name': 'Bob', 'birth_year': 1955, 'death_year': 2000},
        {'name': 'Robert', 'birth_year': 1955, 'death_year': 2000},
        {'name': 'Dick', 'birth_year': 1960, 'death_year': 1980},
        {'name': 'Peter', 'birth_year': 1960, 'death_year': 2020},
        {'name': 'Paul', 'birth_year': 1985, 'death_year': 2019},
        {'name': 'Mary', 'birth_year': 1985, 'death_year': 2020},
        {'name': 'Jane', 'birth_year': 1985, 'death_year': 1995}
    ]

    highest = highest_population_year(people)
    print(highest)