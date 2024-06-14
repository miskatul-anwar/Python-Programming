movies = []
while True:
    movie_name = input("Enter movie name(enter 'quit' to stop):")
    if movie_name == "quit":
        break
    movies.append(movie_name)
print("The list of movies you have entered are:")
print(movies)
