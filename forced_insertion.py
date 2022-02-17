# -*- coding: utf-8 -*-
'''
新物品等插入队列
'''

def forced_insertion(new_doc, items, nums):
    # new_items, items, pos
    # 这里是建议版本：new_doc集体插在pos == nums位置上
    items_tmp = []
    max_score = items[0]['score']
    if nums == 1:
        # 插入前面
        for i, n in enumerate(new_doc):
            items_tmp.append(
                {'item_id': n, 'score': max_score + (len(new_doc) - i) * 0.01})
        for it in items:
            items_tmp.append(it)
        return items_tmp
    else:
        max_score = items[nums - 2]['score']
        min_score = items[nums - 1]['score']
        score = (max_score - min_score - 0.01) / len(new_doc)

        for i, it in enumerate(items):
            if i == nums - 1:
                for j, n in enumerate(new_doc):
                    items_tmp.append(
                        {'item_id': n, 'score': max_score - (j + 1) * score})
            items_tmp.append(it)

    return items_tmp
