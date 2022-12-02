from random import randrange

#random movie option generator

def pickMovie():
    movies = []
    x = input('how many movies do you have to pick from?: ')
    len_list = int(x)

    for i in range(len_list):
        movie = input('what movie do you want to watch?: ')
        movies.append(movie)


    m = randrange(len(movies))
    choice = movies[m]
    c = choice.upper()

    return c


y = pickMovie()



print(f'you will watch "{y}" because you are indecisive and cant make a basic film choice')