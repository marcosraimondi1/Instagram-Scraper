# Pandas
import pandas

from insta_get_follows import printB


def process_data(followers, followings):
    """
    Processes data into dataframes and csv
    - followers: list
    - followings: list
    - returns: void
    """

    # Seguidores del usuario -----------------------------

    if len(followers) != 0:
        # mapea el usuario que nos sigue y un texto si lo seguimos también o no
        data = dict()

        for follower in followers:
            if follower in followings:
                data[follower] = "lo sigues"
            else:
                data[follower] = "no lo sigues"

        seguidoresDF = pandas.DataFrame(data.items())
        seguidoresDF.index += 1
        seguidoresDF.columns = [f"seguidores ({len(followers)})", "estado"]

        seguidoresDF.to_csv(
            f'seguidores.csv', encoding='utf-8')

    # Seguidos por el usuario --------------------------------

    if len(followings) != 0:
        # mapea el usuario seguido y un texto segun si también nos sigue o no
        data2 = dict()

        for following in followings:
            if following in followers:
                data2[following] = "te sigue"
            else:
                data2[following] = "no te sigue"

        seguidosDF = pandas.DataFrame(data2.items())
        seguidosDF.index += 1
        seguidosDF.columns = [f"seguidos ({len(followings)})", "estado"]

        seguidosDF.to_csv('seguidos.csv', encoding='utf-8')
