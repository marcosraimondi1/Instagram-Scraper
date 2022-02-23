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

        ts = len(seguidos)
        nts = len(no_seguidos)

        # listas de mismo len
        same_len = same_len_lists(seguidos, no_seguidos)

        create_data_frames(same_len, [f"los sigues ({ts})", f"no los sigues ({nts})"], "seguidores")
        

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

        ts = len(siguiendo)
        nts = len(no_siguiendo)

        # listas de mismo len
        same_len = same_len_lists(siguiendo, no_siguiendo)

        create_data_frames(same_len, [f"te siguen ({ts})", f"no te siguen ({nts})"], "seguidos")

def same_len_lists(A,B):
    """
    Create lists of same size
    - A: list
    - B: list
    - returns: list (2 lists of same size)
    """
    arrays = [A, B]
    max_length = 0
    for array in arrays:
        max_length = max(max_length, len(array))

    for array in arrays:
        array += ['------'] * (max_length - len(array))

    return arrays

def create_data_frames (lists, listNames, name):
    """
    Creates Dataframes and .csv files
    - lists: list (2 lists with same len)
    - listNames: list (strings for columns titles)
    - name: string (file name)
    - returns: void
    """
    dF = pandas.DataFrame({
            f"{listNames[0]}": lists[0],
            f"{listNames[1]}":  lists[1]
        })
    
    dF.index += 1

    dF.to_csv(
        f'{name}.csv', encoding='utf-8')
