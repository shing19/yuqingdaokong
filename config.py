import configparser


def get_dict(name):
    dict_path = config.items(name)
    dict_path = dict_path[0][1]
    with open (dict_path, 'r') as f:
        dict_list = [x.strip() for x in f]
    return dict_list
    

# 这个还没写
def get_url():
    search_reply_url = self.get('search', 'search_reply_url')
    return search_reply_url


config = configparser.ConfigParser()
config.read('./config.ini')


if __name__ == '__main__':
    result = get_dict('scene')
    print(result)
