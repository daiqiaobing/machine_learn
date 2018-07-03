# -*- coding: utf-8 -*-

"""
使用k临近算法改进网站约会效果
@author mango
"""

from numpy import *
import operator


def create_data_set():
    """ 创建数据集"""
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(int_x, data_set, labels, k):
    """ k 临近算法"""
    data_set_size = data_set.shape[0]
    diff_mat = tile(int_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distance = sq_diff_mat.sum(axis=1)
    distances = sq_distance ** 5
    sorted_distances = distances.sort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_distances[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def file_matrix(filename):
    """
    将文本文件转换为Numpy的解析程序
    :param filename:
    :return:
    """
    fr = open(filename)
    lines = fr.readlines()
    result = zeros((len(lines), 3))
    label_vector = []
    index = 0
    for line in lines:
        line = line.strip()
        line_list = line.split("\t")
        result[index, :] = line_list[0: 3]
        label_vector.append(int(line_list[-1]))
        index += 1
    return result, label_vector


