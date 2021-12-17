from search_input import Input
from es_search.label2tag import label2tag


# class Reply():
    



if __name__ == '__main__':
    # input = Input.from_input()
    test = Input('好耶', '1', '角色活动', '活动暗讽/拒绝参加')
    tags = label2tag(test.label, test.scene)
    print(test, '\n', tags)