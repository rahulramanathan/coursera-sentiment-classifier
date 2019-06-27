import requests_with_caching


def get_movies_from_tastedive(movie):
    parameters = {'q': movie, 'type': 'movies', 'limit': '5'}
    result = requests_with_caching.get("https://tastedive.com/api/similar", params=parameters)
    return result.json()


def extract_movie_titles(dic):
    movies = []
    for ele in dic['Similar']['Results']:
        movies.append(ele['Name'])
    return movies


def get_related_titles(movie_list):
    final_list = []
    for movie in movie_list:
        related_list = extract_movie_titles(get_movies_from_tastedive(movie))
        for i in related_list:
            if i not in final_list:
                final_list.append(i)
    return final_list

import requests_with_caching
def get_movie_data(movie_name):
    parameters = {'t': movie_name, 'r': 'json'}
    result = requests_with_caching.get("http://www.omdbapi.com/", params = parameters)
    return result.json()


def get_movie_rating(dic):
    ratings = dic['Ratings']
    r = 0
    for i in ratings:
        if i['Source'] is 'Rotten Tomatoes':
            r = int(i['Value'][:-1])
    return r

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

