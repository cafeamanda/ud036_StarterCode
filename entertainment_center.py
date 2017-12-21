import fresh_tomatoes
import media

# Creates new instances of Movie()
up = media.Movie("UP",
                 "2009",
                 "Seventy-eight year old Carl Fredricksen travels to Paradise "
                 "Falls in his home equipped with balloons, inadvertently "
                 "taking a young stowaway.",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NDE"
                 "2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_UX182_CR0,0,182,26"
                 "8_AL_.jpg",
                 "https://www.youtube.com/watch?v=qas5lWp7_R0")

mean_girls = media.Movie("Mean Girls",
                         "2004",
                         "Cady Heron is a hit with The Plastics, the A-list "
                         "girl clique at her new school, until she makes the "
                         "mistake of falling for Aaron Samuels, the "
                         "ex-boyfriend of alpha Plastic Regina George.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5"
                         "BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw@@._V1_UY"
                         "268_CR3,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=KAOmTMCtGkI")

pulp_fiction = media.Movie("Pulp Fiction",
                           "1994",
                           "The lives of two mob hitmen, a boxer, a gangster's"
                           " wife, and a pair of diner bandits intertwine in"
                           " four tales of violence and redemption.",
                           "https://images-na.ssl-images-amazon.com/images/M/M"
                           "V5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V"
                           "1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

truman_show = media.Movie("The Truman Show",
                          "1998",
                          "An insurance salesman/adjuster discovers his entire"
                          " life is actually a television show.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV"
                          "5BMDIzODcyY2EtMmY2MC00ZWVlLTgwMzAtMjQwOWUyNmJjNTYyX"
                          "kEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268"
                          "_AL_.jpg",
                          "https://www.youtube.com/watch?v=loTIzXAS7v4")

beautiful_mind = media.Movie("A Beautiful Mind",
                             "2001",
                             "After John Nash, a brilliant but asocial "
                             "mathematician, accepts secret work in "
                             "cryptography, his life takes a turn for the "
                             "nightmarish.",
                             "https://images-na.ssl-images-amazon.com/images/M"
                             "/MV5BMzcwYWFkYzktZjAzNC00OGY1LWI4YTgtNzc5MzVjMDV"
                             "mNjY0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,"
                             "0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=WFJgUm7iOKw")

dead_poets_society = media.Movie("Dead Poets Society",
                                 "1989",
                                 "English teacher John Keating inspires his "
                                 "students to look at poetry with a different "
                                 "perspective of authentic knowledge and "
                                 "feelings.",
                                 "https://images-na.ssl-images-amazon.com/imag"
                                 "es/M/MV5BOGYwYWNjMzgtNGU4ZC00NWQ2LWEwZjUtMzE"
                                 "1Zjc3NjY3YTU1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V"
                                 "1_UX182_CR0,0,182,268_AL_.jpg",
                                 "https://www.youtube.com/watch?v=wrBk780aOis")

# Creates a movie array to be passed into open_movies_page()
movies = [up, mean_girls, pulp_fiction, truman_show, beautiful_mind,
          dead_poets_society]

# Creates and opens Movie App
fresh_tomatoes.open_movies_page(movies)
