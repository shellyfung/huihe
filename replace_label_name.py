import os
import json
import numpy as np
import path_and_files as pf


def read_json(json_path):

    with open(json_path, 'r', encoding='utf-8') as json_file:
        temp = json.load(json_file)
        json_file.close()

    temp_list = temp['labels']
    return temp_list


def save_json(path, name, data):
    with open(path + name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
        json_file.close()


def replace_name(json_file, save_path, label_list):
    json_paths = pf.get_file_path_with_type(json_file, '.json')

    for json_path in json_paths:
        new_dict = {}
        new_list = []
        json_name = os.path.basename(json_path)
        anno = read_json(json_path)
        for num in range(len(anno)):
            cell_dict = {}
            name = anno[num]['name']
            if name in label_list:
            # if name == 'XueBiNingMengPET500ML':
            #     name = 'xuebi500ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            '''
            elif name == 'KeKouKeLePET500ML':
                name = 'kele500ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            elif name == 'MeiZhiYuanGuoLiChengPET450ML':
                name = 'guolc450ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            elif name == 'FenDaChengPET500ML':
                name = 'fenda500ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            elif name == 'ChunYueYinYongShuiPET550ML':
                name = 'chunyue500ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            elif name == 'XueBiNingMengSLEEKCAN330ML':
                name = 'xuebi330ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            elif name == 'KeKouKeLeSLEEKCAN330ML':
                name = 'kele330ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            elif name == 'XueBiXianWeiPlusPET500ML':
                name = 'xuebixianwei500ml'
                cell_dict['name'] = name
                cell_dict['x1'] = anno[num]['x1']
                cell_dict['y1'] = anno[num]['y1']
                cell_dict['x2'] = anno[num]['x2']
                cell_dict['y2'] = anno[num]['y2']
                new_list.append(cell_dict)
            else:
                pass
            '''

        if new_list:
            new_dict.update(labels=new_list)

            save_json(save_path, json_name, new_dict)
            print(json_name)


if __name__ == '__main__':

    json_file_ = '/xxxxxx/'
    save_path_ = '/xxxxxxxxx/'
    # label_list_ = ('XueBiNingMengPET500ML', 'KeKouKeLePET500ML', 'MeiZhiYuanGuoLiChengPET450ML',
    #                'FenDaChengPET500ML', 'ChunYueYinYongShuiPET550ML', 'XueBiNingMengSLEEKCAN330ML',
    #                'KeKouKeLeSLEEKCAN330ML', 'XueBiXianWeiPlusPET500ML')
    label_list_ = ('LingDuKeLePET500ML', 'YiQuanPlusCNingMengPET400ML', 'ChunChaSheYuLuLvChaPET480ML',
                   'ChunChaSheTieGuanYinWuLongChaPET480ML',
                   'ChunChaSheYuMuHongChaPET480ML', 'FenDaPingGuoPET500ML')
    replace_name(json_file_, save_path_, label_list_)



