"""
    You work on a team whose job is to understand the most sought after toys for the holiday season.
    A teammate of yours has built a webcrawler that extracts a list of quotes about toys from different articles.
    You need to take these quotes and identify which toys are mentioned most frequently.
    Write an algorithm that identifies the top N toys out of a list of quotes and list of toys.

    Your algorithm should output the top N toys mentioned most frequently in the quotes.

     Input:
    The input to the function/method consists of five arguments:

    numToys, an integer representing the number of toys
    topToys, an integer representing the number of top toys your algorithm needs to return;
    toys, a list of strings representing the toys,
    numQuotes, an integer representing the number of quotes about toys;
    quotes, a list of strings that consists of space-sperated words representing articles about toys

    Output:
    Return a list of strings of the most popular N toys in order of most to least frequently mentioned

    Note:
    The comparison of strings is case-insensitive.
    If the value of topToys is more than the number of toys,
    return the names of only the toys mentioned in the quotes.
    If toys are mentioned an equal number of times in quotes, sort alphabetically.

    Example:

    Input:
    numToys = 6
    topToys = 2
    toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
    numQuotes = 6
    quotes = [
    "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
    "The new Elmo dolls are super high quality",
    "Expect the Elsa dolls to be very popular this year, Elsa!",
    "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
    "For parents of older kids, look into buying them a drone",
    "Warcraft is slowly rising in popularity ahead of the holiday season"
    ];

    Output:
    ["elmo", "elsa"]

    Explanation:
    elmo - 4
    elsa - 4
    "elmo" should be placed before "elsa" in the result because "elmo" appears in 3 different quotes and "elsa" appears in 2 different quotes.


"""

import re


def top_n_buzzword(num_toys, top_toys, toys, num_quotes, quotes):

    buzzwords = {}  # init dictionary

    # O(n^2)
    for toy in toys: # iterate over toys
        buzzwords[toy] = 0
        buzzword_count = 0
        for quote in quotes: # iterate over quotes list, counting occurrences of tpy names
            clean_quote = re.sub('[^A-Za-z0-9]+', ' ', quote).lower()
            buzzword_count += clean_quote.split(" ").count(toy)
        buzzwords[toy] = buzzword_count

    # O(n Log n) python uses Timesort (merge and insertion)
    sorted_buzzwords = sorted(buzzwords.items(), key=lambda kv: kv[1], reverse=True)

    counter = 1
    buzzword_list = []
    # O(n)
    for (name, count) in sorted_buzzwords:
        buzzword_list.append(name)
        if counter == top_toys:
            break

        counter += 1

    return buzzword_list



if __name__ == '__main__':
    #str = "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!".lower()

    #print(str.split(" ").count('elmo'))
    toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
    quotes = [
        "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
        "The new Elmo dolls are super high quality",
        "Expect the Elsa dolls to be very popular this year, Elsa!",
        "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
        "For parents of older kids, look into buying them a drone",
        "Warcraft is slowly rising in popularity ahead of the holiday season"
    ]
    print(top_n_buzzword(6, 2, toys, 6, quotes))