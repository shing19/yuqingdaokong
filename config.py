import os
import configparser


config = configparser.ConfigParser()
path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'
config.read(path)


#获取config配置文件
def get_config(section, key):
    return config.get(section, key)


def get_dict(name):
    dict_path = config.items(name)
    dict_path = dict_path[0][1]
    with open (dict_path, 'r') as f:
        dict_list = [x.strip() for x in f]
    return dict_list
    

# 这个还没写
def get_url():
    search_reply_url = config.get('search', 'search_reply_url')
    return search_reply_url


if __name__ == '__main__':
    result = get_dict('scene')
    print(result)
