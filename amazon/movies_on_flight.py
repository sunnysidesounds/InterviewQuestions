"""
You are on a flight and wanna watch two movies during this flight.
You are given int[] movie_duration which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
Find the pair of movies with the longest total duration. If multiple found, return all pairs.

Input
movie_duration: [90, 85, 75, 60, 120, 150, 125]
d: 250

Output
[90, 125]
90min + 125min = 215 is the maximum number within 220 (250min - 30min)

"""


def movies_on_flight_2(flight_duration, movie_duration):
    flight_duration -= 30
    movie_duration = sorted(movie_duration)
    left_index = 0
    right_index = len(movie_duration) - 1
    closest_value = 0
    while(left_index < right_index):
        if movie_duration[left_index] + movie_duration[right_index] <= flight_duration:
            if closest_value < (movie_duration[left_index] + movie_duration[right_index]):
                closest_value = movie_duration[left_index] + movie_duration[right_index]
                x = left_index
                y = right_index
            left_index += 1
        else:
            right_index -= 1
    return (movie_duration[x], movie_duration[y])




def movies_on_flight(flight_duration, movie_duration):
    movies_flight_duration = flight_duration - 30
    if movies_flight_duration == movie_duration:
        return movie_duration

    movie_dict = {}
    list_of_final_durations = []
    # build a map of all possible sums with a list of their associated indexes {215: (0, 5)}
    # Time complexity O(n^2) Not very efficient
    for d in range(len(movie_duration)):
        for dd in range(len(movie_duration) -1):
            sub_sum = movie_duration[d] + movie_duration[dd+1]
            if sub_sum in movie_dict:
                movie_dict[sub_sum].append((d, dd+1))
            else:
                movie_dict[sub_sum] = []
                movie_dict[sub_sum].append((d, dd+1))

    # find matching sum key in dictionary, return a list of associated indexes.
    if movies_flight_duration in movie_dict:
        indexes = movie_dict[movies_flight_duration]
    else:
        # Get the closest value to movies_flight_duration and return list of indexes
        closest_value = min(movie_dict, key=lambda x:abs(x-movies_flight_duration))
        indexes = movie_dict[closest_value]

    # create final list (converts index values into actual values.)
    # Time complexity O(n)
    for index in indexes:
        list_of_final_durations.append((movie_duration[index[0]], movie_duration[index[1]]))

    # Space complexity O(n)
    # Time complexity O(n^2)

    return list_of_final_durations


if __name__ == '__main__':
    results = movies_on_flight_2(250, [90, 85, 75, 60, 120, 150, 125])
    print(results)