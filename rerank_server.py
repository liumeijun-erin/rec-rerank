# -*- codingL utf-8 -*-
'''
四个常用重排策略
'''

from cate_shuffle import cate_shuffle
from forced_insertion import forced_insertion
from gender_filter import gender_filter
from hot_rerank import hot_rerank

if __name__ == '__main__':
    items = [
        {'item_id': 'N2031', 'cate': '01', 'score': 0.92},
        {'item_id': 'N2032', 'cate': '01', 'score': 0.71},
        {'item_id': 'N2033', 'cate': '01', 'score': 0.70},
        {'item_id': 'N2034', 'cate': '02', 'score': 0.65},
        {'item_id': 'N2035', 'cate': '02', 'score': 0.64},
        {'item_id': 'N2036', 'cate': '03', 'score': 0.63},
        {'item_id': 'N2037', 'cate': '03', 'score': 0.61},
    ]

    result1 = cate_shuffle(items)
    print(result1)

    result2 = forced_insertion(['N2073', 'N2075'], items, 2)
    print(result2)

    result3 = gender_filter(items, ['02','03'])
    print(result3)

    # news click record
    result4 = hot_rerank('data/behaviors.tsv', ['N59186','N47061'])
    print(result4)