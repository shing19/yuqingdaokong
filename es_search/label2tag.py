import sys
from typing import Dict, List, Tuple
# 主程序运行时用如下引入
# from es_search.search import es_search
# 子文件夹内用如下引入
from search import es_search

sys.path.append("..")
from config import get_config



def label2tag(label: str, scene: str) -> List[Tuple]:
    es_url = get_config('search', 'search_label_url')
    must = []
    must.append({"match_phrase": {"label": label}})
    must.append({"match_phrase": {"scene": scene}})
    data = {
        "query": {
            "bool": {
                "must": must
            }
        }
    }
    search_status, search_result = es_search(es_url, data)
    if search_status:
        tags = [(x['_source']['emotion'], x['_source']['focus']) for x in search_result]
        return tags
    else:
        print('查询失败')
        return None
    

if __name__ == '__main__':
    label = '活动暗讽/拒绝参加'
    scene = '角色活动'
    tags = label2tag(label, scene)
    print(tags)