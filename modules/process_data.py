# Pandas
import pandas

from modules.insta_get_follows import printB


def process(followers, followings):
    """
    Processes data into dataframes and csv
    - followers: list
    - followings: list
    - returns: void
    """
    printB(f"Followers: {len(followers)}")
    printB(f"Followings: {len(followings)}")
    # Seguidores del usuario -----------------------------

    if len(followers) != 0:
        # devuelve un data frame con 2 columnas, los seguidores que tambien sigues y los que no
        seguidos = list()
        no_seguidos = list()
        
        for follower in followers:
            if follower in followings:
                seguidos.append(follower)
            else:
                no_seguidos.append(follower)

        # listas de mismo len
        same_len = same_len_lists(seguidos, no_seguidos)

        seguidoresDF = pandas.DataFrame({
            f"seguidos ({len(seguidos)})": same_len[0],
            f"no seguidos ({len(no_seguidos)})":  same_len[1]
        })
        seguidoresDF.index += 1

        seguidoresDF.to_csv(
            f'seguidores.csv', encoding='utf-8')

    # Seguidos por el usuario --------------------------------

    if len(followings) != 0:
        # mapea el usuario seguido y un texto segun si también nos sigue o no
        siguiendo = list()
        no_siguiendo = list()

        for following in followings:
            if following in followers:
                siguiendo.append(following)
            else:
                no_siguiendo.append(following)

        # listas de mismo len
        same_len = same_len_lists(siguiendo, no_siguiendo)

        seguidosDF = pandas.DataFrame({
            f"te siguen ({len(siguiendo)})": same_len[0],
            f"no te siguen ({len(no_siguiendo)})":  same_len[1]
        })
        seguidosDF.index += 1

        seguidosDF.to_csv('seguidos.csv', encoding='utf-8')


def same_len_lists(A,B):
    # create lists of same size
    arrays = [A, B]
    max_length = 0
    for array in arrays:
        max_length = max(max_length, len(array))

    for array in arrays:
        array += ['------'] * (max_length - len(array))

    return arrays