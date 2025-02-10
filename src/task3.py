#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Представьте, что вы разрабатываете систему для управления складом,
где товары упорядочены в структуре, похожей на двоичное дерево.
Каждый узел дерева представляет место хранения, которое может вести
к другим местам хранения (левому и правому подразделу).
Ваша задача — найти наименее затратный путь к товару,
ограничив поиск заданной глубиной, чтобы гарантировать,
что поиск займет приемлемое время.
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
        return None
    if node.value == goal:
        return node
    if depth >= limit:
        return None

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
    limit = 3

    result = dls(root, goal, limit)
    print("Цель найдена:", result)


if __name__ == "__main__":
    main()
