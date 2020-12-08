# coding=utf-8
from os import walk, path
import re
import queue


# from urllib.request import urlopen
# import os
# import numpy


def func_check(file_path_):
    with open(file_path_)as f:
        # file_lines = f.readlines()
        # print([i for i in file_lines])
        try:
            for line_ in f.readlines():
                # print(type(line_))

                rs1 = re.findall(r'^(from\s+[\_\.0-9a-zA-Z]+)\s', line_)
                rs2 = re.findall(r'\n(from\s+[\_\.0-9a-zA-Z]+)\s', line_)
                rs3 = re.findall(r'^(import\s+.+)', line_)
                rs4 = re.findall(r'\n(import\s+.+)', line_)

                # rs5 = re.findall(r'^(import\s+[\_\.0-9a-zA-Z]+)\s', line_)
                # rs6 = re.findall(r'\n(import\s+[\_\.0-9a-zA-Z]+)\s', line_)
                # rs7 = re.findall(r'^(import\s+.+)', line_)
                # rs8 = re.findall(r'\n(import\s+.+)', line_)
                # 得到所有包
                rs = rs1 + rs2 + rs3 + rs4
                n_rs = []
                for i_ in rs:
                    i_ = i_.replace('import', '').replace('from', '')
                    if '#' in i_:
                        i_ = i_.strip('#')[0]
                    if 'as' in i_:
                        i_ = i_.strip('as')[0]
                    if len(i_.strip('.')) > 0:
                        i_ = i_.strip('.')
                    else:
                        i_ = ''
                    if len(i_) > 0:
                        n_rs.append(i_[0])
                    # print(i_)
                    # print(type(i_))
                res_list = [file_path_, n_rs]
                if len(rs) > 0:
                    # print(res_list)
                    q.put(res_list)
        except Exception as e:
            pass
            # print('Error Information : ', e)


if __name__ == '__main__':
    q = queue.Queue()
    q1 = queue.Queue()
    list_dir = []
    for root, directory, files in walk('C:/Users/Zank/anaconda3'):
        # print(root, directory, file)
        r_list = []
        for file_name in files:
            # print(files)
            if file_name.endswith('.py'):
                # r_list.append(file_name)
                file_path = path.join(root, file_name)

                # print(file_path)
                r_list.append(file_path)
        list_dir.append(directory)
        for i in r_list:
            # print(i)
            func_check(i)

    while not q.empty():
        q_data = q.get()
        for j_ in q_data[1]:
            print(j_)
            if j_ not in list_dir:
                # print(q_data[0], 'not found', j_)
                pass
        # print(q.get())
