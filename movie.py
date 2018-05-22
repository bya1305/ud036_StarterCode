class Movie():
    """Creates a Movie instance with basic info about individual movie"""
    def __init__(self, movie_title, poster, trailer):
        self.title = movie_title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
