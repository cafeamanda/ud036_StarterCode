import webbrowser


class Movie():
    """ Instances of this class store movie related information """

    def __init__(self, movie_title, movie_year, movie_storyline, poster_image,
                 trailer_youtube):
        """ This constructor creates properties for each movie instance and
            stores their values according to given arguments on call """
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This function opens a webbrowser on YouTube to show a movie
            trailer """
        webbrowser.open(self.trailer_youtube_url)
