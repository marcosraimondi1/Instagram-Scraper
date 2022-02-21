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

    # Seguidores -----------------------------

    data = dict()
    data["yo"] = "te sigue"

    for follower in followers:
        if follower in followings:
            data[follower] = "te sigue"
        else:
            data[follower] = "no te sigue"

    seguidoresDF = pandas.DataFrame(data.items())
    seguidoresDF.columns = ["seguidores", "estado"]

    seguidoresDF.to_csv('seguidores.csv', encoding='utf-8')

    # Seguidos --------------------------------

    data2 = dict()

    for following in followings:
        if following in followers:
            data2[following] = "lo sigues"
        else:
            data2[following] = "no lo sigues"

    seguidosDF = pandas.DataFrame(data2.items())
    seguidosDF.columns = ["seguidos", "estado"]

    seguidosDF.to_csv('seguidos.csv', encoding='utf-8')
