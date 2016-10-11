import fresh_tomatoes
import media

"""
declare favorite movies, with 4 args each:
movie_title
movie_storyline
poster_image (url to a poster image)
trailer_youtube (url to youtube trailer)
"""

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://youtu.be/5PSNL1qE6VY")

jungle_book = media.Movie("Jungle Book",
                          "A story of a boy named Mowgli raised in jungle by "
                          "Indial wolf Raksha",
                          "http://ia.media-imdb.com/images/M/MV5BMTc3NTUzNTI4MV5BMl5BanBnXkFtZTgwNjU0NjU5NzE@._V1_SY1000_SX675_AL_.jpg",  # NOQA
                          "https://youtu.be/5mkm22yO-bs")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                          "https://youtu.be/c3sBBRxDAqk")

star_wars = media.Movie("Star Wars Episode 4",
                        "Luke Skywalker joins forces with a Jedi "
                        "Knight, a cocky pilot, a wookiee and "
                        "two droids to save the galaxy from the Empire's "
                        "world-destroying battle-station, while also "
                        "attempting to rescue Princess Leia from "
                        "the evil Darth Vader.",
                        "http://ia.media-imdb.com/images/M/MV5BOTIyMDY2NGQtOGJjNi00OTk4LWFhMDgtYmE3M2NiYzM0YTVmXkEyXkFqcGdeQXVyNTU1NTcwOTk@._V1_SY1000_CR0,0,654,1000_AL_.jpg",  # NOQA
                        "https://youtu.be/9gvqpFbRKtQ")

mad_max = media.Movie("Mad Max : Fury Road",
                      "A woman rebels against a tyrannical ruler in "
                      "postapocalyptic Australia in search for "
                      "her home-land with the help of a group of "
                      "female prisoners, a psychotic worshipper, "
                      "and a drifter named Max.",
                      "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SY1000_CR0,0,687,1000_AL_.jpg",  # NOQA
                      "https://youtu.be/hEJnMQG9ev8")


# movies array which has individual movies
movies = [toy_story, avatar, jungle_book, ratatouille, star_wars, mad_max]

# call open_movies_page method and pass movies array
fresh_tomatoes.open_movies_page(movies)
