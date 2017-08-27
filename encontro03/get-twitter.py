import os
import twitter

from twitter.error import TwitterError


ROOT_NODE = 'Disney'

DATA_FOLDER = 'tarefa1'


def build_path(node):
    return os.path.join(DATA_FOLDER, node + '.txt')


def main():
    api = twitter.Api(
        consumer_key='',
        consumer_secret='',
        access_token_key='',
        access_token_secret='',
        sleep_on_rate_limit=True,
    )

    root_path = build_path(ROOT_NODE)

    with open(root_path, 'w', encoding='utf-8') as root_file:
        root_data = api.GetFriends(screen_name=ROOT_NODE)

        for root_subdata in root_data:
            node = root_subdata.screen_name

            print(node)

            try:
                data = api.GetFriends(screen_name=node)
            except TwitterError:
                continue

            root_file.write(node + '\n')

            path = build_path(node)

            with open(path, 'w', encoding='utf-8') as file:
                for subdata in data:
                    file.write(subdata.screen_name + '\n')


if __name__ == '__main__':
    main()
