class Movie:
    """ This class privides a way to store movie related information """
    def __init__(self, movie_title, movie_rating, movie_genre, box_art, trailer_youtube):
        self.title = movie_title
        self.rating = movie_rating
        self.genre = movie_genre
        self.poster_image_url = box_art
        self.trailer_youtube_url = trailer_youtube
