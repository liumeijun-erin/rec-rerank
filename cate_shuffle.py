# -*- coding: utf-8 -*-
'''
类别打散'''

def cate_shuffle(items):
    # items已经是分值从高到底排列的结果了
    # 但是iter1中的类别还是要按照rank分数来排序
    cate_items = {}
    cate_sort = []

    for item in items:
        cate = item['cate']
        cate_items.setdefault(cate, [])
        cate_items[cate].append(item)
        if cate not in cate_sort:
            cate_sort.append(cate)
    
    result = []
    for i in range(len(items)):
        for c in cate_sort:
            res = cate_items[c]
            if i > len(res) - 1:
                continue
            result.append(res[i])

    return result
