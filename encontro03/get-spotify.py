import os

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


ROOT_NODE = '4Rxn7Im3LGfyRkY2FlHhWi'

ROOT_NAME = 'Nick Jonas'

ROOT_DEPTH = 2

DATA_FOLDER = 'tarefa2'


def get_successors(api, node, depth=1, names=None):
    successors = set()

    data = api.artist_related_artists(node)

    for subdata in data['artists']:
        successor = subdata['id']

        successors.add(successor)

        if names is not None:
            names[successor] = subdata['name']

    if depth > 1:
        successors_copy = successors.copy()

        for successor in successors_copy:
            successors |= get_successors(api, successor, depth - 1, names)

    return successors


def save_successors(node, successors, names=None):
    path = os.path.join(DATA_FOLDER, node + '.txt')

    with open(path, 'w', encoding='utf-8') as file:
        for successor in successors:
            file.write(successor)

            if names is not None:
                file.write(' ' + names[successor])

            file.write('\n')


def main():
    client_credentials_manager = SpotifyClientCredentials(
        client_id='',
        client_secret='',
    )

    api = Spotify(client_credentials_manager=client_credentials_manager)

    names = {}

    nodes = get_successors(api, ROOT_NODE, ROOT_DEPTH, names)

    del names[ROOT_NODE]

    nodes.discard(ROOT_NODE)

    save_successors(ROOT_NODE, nodes, names)

    for node in nodes:
        print(node, names[node])

        successors = get_successors(api, node)

        save_successors(node, successors)


if __name__ == '__main__':
    main()
