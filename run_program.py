import movie
import fresh_tomatoes

movie1 = movie.Movie("Darkest Hour",
                     "https://ia.media-imdb.com/images/M/MV5BNTU4MjMwOTgyMV5BMl5BanBnXkFtZTgwODQzNjY2NDM@._V1_SX300.jpg",
                     "https://www.youtube.com/watch?v=LtJ60u7SUSw")

movie2 = movie.Movie("Thor: Ragnarok",
                     "https://ia.media-imdb.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_SX300.jpg",
                     "https://www.youtube.com/watch?v=v7MGUNV8MxU")

movie3 = movie.Movie("Justice League",
                     "https://ia.media-imdb.com/images/M/MV5BYWVhZjZkYTItOGIwYS00NmRkLWJlYjctMWM0ZjFmMDU4ZjEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
                     "https://www.youtube.com/watch?v=r9-DM9uBtVI")

movie4 = movie.Movie("Skyfall",
                     "https://ia.media-imdb.com/images/M/MV5BNDVhZmJiYWMtNmIzMC00ZWNiLTkzZDYtNGNlZmViMGM4OGExXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=6kw1UVovByw")

movie5 = movie.Movie("The Dark Knight",
                     "https://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movie6 = movie.Movie("The Dark Knight Rises",
                     "https://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=GokKUqLcvD8")

movie7 = movie.Movie("Ready Player One",
                     "https://ia.media-imdb.com/images/M/MV5BY2JiYTNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3XkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=cSp1dM2Vj48")

movie_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7]

# Function pulled from the fresh_tomatoes module that passes in the array of
# movie data here to generate a webpage
fresh_tomatoes.open_movies_page(movie_list)
