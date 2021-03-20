import os
from collections import defaultdict
from os.path import relpath
from distutils.dir_util import copy_tree

import yaml
from pprint import pprint

import shutil
import django

"""
1. создать шаблоны с папками
"""

def create_dir(patern, list_dir):
    for dir in list_dir:
        dir_path = os.path.join(patern, dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

patern = "my_project"
list_dir = ['setting', 'mainapp', 'adminap', 'authapp']

# create_dir(patern, list_dir)

'''
2* yaml (еще дописываю скрипт)
'''


with open('config.yaml') as f:
    path_yaml = yaml.safe_load(f)

print (path_yaml)

for key, item in path_yaml.items():
    print(key)
    if type(item) == type({}):
        print(key)
        print(item)
        for key_1, item_1 in item.items():
            if type(item_1) == type({}):
                print(key_1)


"""
3. Перенос папок
"""
#
# root_dir = os.path.abspath('my project')
#
# dst_dir = "templates"
# for root, dirs, files in os.walk(root_dir):
#     if dirs == [dst_dir]:
#         scr_path = os.path.join(root, str(*dirs))
#         try:
#             shutil.move(scr_path, root_dir)
#         except shutil.Error:
#             copy_tree(scr_path, os.path.join(root_dir, dst_dir))

"""
4 и 5 . {размер кратный 10: (количество файлов, [разрешения файлов]}
"""

root_dir = django.__path__[0]
size_file_dict = defaultdict(list)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        relative_path = os.path.relpath(os.path.join(file,root),os.getcwd())
        size_file = os.stat(relative_path)
        size_abs = size_file[6]//10*10
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        size_file_dict[size_abs].append(ext)


# сортировка по количеству файлов
# for ext, files in sorted(size_file_dict.items(), key=lambda x: len(x[1]), reverse=True):
    # print(f'{ext}: {len(files), list(set(files))}')


# сортировка по объему файлов
# for ext, files in sorted(size_file_dict.items()):
     # print(f'{ext}: {len(files), list(set(files))}')

