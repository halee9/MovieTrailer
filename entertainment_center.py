import media
import fresh_tomatoes

# movie instance
the_intern = media.Movie("The Intern",
                         "PG-13",
                         "Comedy",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/The_Intern_Poster.jpg/440px-The_Intern_Poster.jpg",
                         "https://youtu.be/HGQNM8OHyIE")

ant_man = media.Movie("Ant Man",
                      "PG-13",
                      "Adventure",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
                      "https://youtu.be/xInh3VhAWs8")

maze_runner = media.Movie("Maze Runner",
                          "PG-13",
                          "Action",
                          "https://upload.wikimedia.org/wikipedia/en/d/d6/Maze-Runner-The-Scorch-Trials-Poster.jpg",
                          "https://youtu.be/9gbMAYdISsM")

# make movie list array all movies together
movies = [the_intern, ant_man, maze_runner]

# create web page with movies
fresh_tomatoes.open_movies_page(movies)
