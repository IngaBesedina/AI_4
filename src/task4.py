#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Представьте, что вы разрабатываете систему
для автоматического управления инвестициями, где дерево решений используется
для представления последовательности инвестиционных решений
и их потенциальных исходов. Цель состоит в том, чтобы найти наилучший
исход (максимальную прибыль) на определённой глубине принятия решений,
учитывая ограниченные ресурсы и время на анализ.
"""


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def max_value_depth_limited(node, limit, depth=0):
    if node is None or depth > limit:
        return float("-inf")

    if depth == limit:
        return node.value

    left_max = max_value_depth_limited(node.left, limit, depth + 1)
    right_max = max_value_depth_limited(node.right, limit, depth + 1)

    return max(left_max, right_max)


def main():
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)),
        BinaryTreeNode(
            3, BinaryTreeNode(6, BinaryTreeNode(7), BinaryTreeNode(8)), None
        ),
    )

    limit = 3

    max_profit = max_value_depth_limited(root, limit)

    print(f"Максимальное значение на глубине: {max_profit}")


if __name__ == "__main__":
    main()
