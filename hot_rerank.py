import pandas as pd
import numpy as np
import redis
import traceback

def hot_rerank(file_path, doc_list):
    ds = pd.read_csv(file_path,
        names=['index_id', 'user_id', 'timestamp', 'hist', 'doc_id'], sep='\t')

    ds = ds[['doc_id']]  # art1-0曝光未点击，art2-1曝光且点击

    doc_show_count = {}
    doc_click_count = {}

    for item in ds.values:
        tmp_iter = item[0].split(' ')
        for tmp in tmp_iter:
            item, behavior = tmp.split('-')
            doc_click_count.setdefault(item, 0)
            doc_show_count.setdefault(item, 0)
            if behavior == '1':
                doc_click_count[item] += 1
            doc_show_count[item] += 1

    item_show_click_dic = []
    for doc, show in doc_show_count.items():
        click = doc_click_count.get(doc, 0)
        item_show_click_dic.append(
            {
                "doc": doc,
                "show": show,
                "click": click,
            }
        )

    item_show_click = pd.DataFrame(item_show_click_dic)

    # 简单筛选
    item_show_click = item_show_click[item_show_click['show'] > 288]
    print(len(item_show_click))

    # 度量1 - 归一化点击数
    reg = lambda x: x / np.max(x)
    item_show_click['click_reg'] = item_show_click[['click']].apply(reg)

     # 度量2 - 点击/曝光率
    item_show_click['ctr'] = item_show_click['click'] / item_show_click['show']

    w1 = 0.3
    w2 = 0.7
    item_show_click['ctr_click'] = w1 * item_show_click['click_reg'] + w2 * \
                                item_show_click['ctr']

    item_hotrank = {}
    for d in item_show_click[['doc', 'ctr_click']].values:
        item_hotrank[d[0]] = d[1]

    doc_dict = {}
    for doc in doc_list:
        if doc not in item_hotrank.keys():
            continue
        doc_dict[doc] = item_hotrank[doc]
    return sorted(doc_dict.items(), key = lambda x:x[1], reverse = True)



