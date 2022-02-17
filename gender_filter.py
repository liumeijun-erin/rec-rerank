# -*- coding: utf-8 -*-
'''
按喜好过滤
gender_filter可以理解为用户画像属性
'''

def gender_filter(items, gender):
    # new_items, items, pos
    items_tmp = []
    for it in items:
        if it['cate'] in gender:
            items_tmp.append(it)
    return items_tmp