# Pandas
import pandas

from insta_get_follows import printB


def process_data(followers, followings):
    """
    Processes data into dataframes
    - followers: list
    - followings: list
    - returns: void
    """

    # Seguidores del usuario -----------------------------

    if len(followers) != 0:

        data = dict()

        for follower in followers:
            if follower in followings:
                data[follower] = "lo sigues"
            else:
                data[follower] = "no lo sigues"

        seguidoresDF = pandas.DataFrame(data.items())
        seguidoresDF.columns = ["seguidores", "estado"]

        seguidoresDF.to_csv('seguidores.csv', encoding='utf-8')

    # Seguidos por el usuario --------------------------------

    if len(followings) != 0:

        data2 = dict()

        for following in followings:
            if following in followers:
                data2[following] = "te sigue"
            else:
                data2[following] = "no te sigue"

        seguidosDF = pandas.DataFrame(data2.items())
        seguidosDF.columns = ["seguidos", "estado"]

        seguidosDF.to_csv('seguidos.csv', encoding='utf-8')
