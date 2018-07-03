# -*- coding: utf-8 -*-
""""
用于数据分析创建散点图
"""

import matplotlib.pyplot as plt
import chapter1_knn.knn
import numpy as np


def viewer():
    """"
    玩游戏所消耗的时间百分比以及每周消费的冰淇淋公升数
    """
    result, label_vector = chapter1_knn.knn.file_matrix('../data/datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(result[:, 1], result[:, 2])
    plt.show()


def viewer1():
    """"
    玩游戏所消耗的时间百分比以及每周消费的冰淇淋公升数（带标签）
    """
    result, label_vector = chapter1_knn.knn.file_matrix('../data/datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    a = np.array(label_vector)
    ax.scatter(result[:, 1], result[:, 2], 15.0 * np.array(label_vector), 15.0 * np.array(label_vector))
    ax.axis([-2, 25, -0.2, 2.0])
    plt.show()


if __name__ == "__main__":
    """函数执行的入法"""
    viewer1()


