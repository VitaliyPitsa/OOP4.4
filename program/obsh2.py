#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите программу, которая будет генерировать матрицу из случайных целых чисел. 
Пользователь может указать число строк и столбцов, а также диапазон целых чисел. 
Произведите обработку ошибок ввода пользователя.
"""

from dataclasses import dataclass
import random


@dataclass(frozen=True)
class MatrixParams:
    """
    n - Ширина матрицы
    m - Высота матрицы
    a и b - Диапазоны случайных чисел для матрицы
    """

    n: int
    m: int
    a: int
    b: int


class Matrix:
    def __init__(self, params: MatrixParams):
        self._matrix = []

        for i in range(0, params.n):
            r = []
            for j in range(0, params.m):
                r.append(random.randint(params.a, params.b))
            self._matrix.append(r)

    def __str__(self):
        return str(self._matrix)


if __name__ == "__main__":
    try:
        n = int(input("Введите высоту матрицы: "))
        m = int(input("Введите ширину матрицы: "))
        a = int(input("Введите левый диапазон чисел: "))
        b = int(input("Введите правый диапазон чисел: "))
        params = MatrixParams(n, m, a, b)
    except Exception as e:
        print("Ошибка: Необходимо ввести числа")
        exit(1)

    matrix = Matrix(params)

    print(matrix)
