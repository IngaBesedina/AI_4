#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вы работаете над разработкой системы навигации для робота-пылесоса.
Робот способен передвигаться по различным комнатам в доме,
но из-за ограниченности ресурсов (например, заряда батареи) и времени
на уборку, важно эффективно выбирать путь. Ваша задача - реализовать алгоритм,
который поможет роботу определить, существует ли путь к целевой комнате,
не превышая заданное ограничение по глубине поиска.
Дано дерево, где каждый узел представляет собой комнату в доме.
Узлы связаны в соответствии с возможностью перемещения робота
из одной комнаты в другую. Необходимо определить, существует ли путь
от начальной комнаты (корень дерева) к целевой комнате
(узел с заданным значением),
так, чтобы робот не превысил лимит по глубине перемещения.
"""


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def dls(node, goal, limit, depth=0):
    if node is None:
        return False
    if node.value == goal:
        return True
    if depth >= limit:
        return False

    left_result = dls(node.left, goal, limit, depth + 1)
    if left_result:
        return left_result
    return dls(node.right, goal, limit, depth + 1)


def main():
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)),
        BinaryTreeNode(
            3, BinaryTreeNode(6, BinaryTreeNode(7), BinaryTreeNode(8)), None
        ),
    )

    goal = 7
    limit = 2

    result = dls(root, goal, limit)
    print("Найден на глубине:", result)


if __name__ == "__main__":
    main()
