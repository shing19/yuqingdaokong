import json
import requests
from typing import Dict, List, Tuple


def es_search(url: str, data: Dict) -> List:
    search_status = False
    search_result = None
    headers = {
        'Content-Type': 'application/json',
        'charset': 'UTF-8'
    }
    data = json.dumps(data)
    response = requests.get(url, headers=headers, data=data)
    response.encoding = 'utf-8'
    result = json.loads(response.text)
    # 报错
    try:
        if result.get('error'):
            error_type = result['error'].get('type')
            error_reson = result['error'].get('reason')
            print(f'es检索错误\n[type] {error_type}\n[reason] {error_reson}')
            return search_status, search_result
        elif result['hits']['total'] == 0:
            print('未查询到相关数据，原因可能如下：\n1. 数据库中不存在\n2. 查询语句错误')
            return search_status, search_result
        elif result['hits']['total'] != 0:
            search_result = result['hits']['hits']
            search_status = True
            return search_status, search_result
    except Exception as e:
        print('发生未知错误', e)
        return search_status, search_result
        
    

if __name__ == '__main__':
    pass