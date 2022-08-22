# -*- coding: utf-8 -*-

from multiprocessing.dummy import Array

from typing import Container, Tuple
from random import random


def create_numbers(count: int) -> Container[int]:
    numbers = []
    for i in range(count):
        numbers.append(round(random() * 100))
    return numbers


def bubble_sort(numbers: Container[int]) -> None:
    for i in range(1, len(numbers)): 
        for j in range(i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    
def insertion_sort(numbers: Container[int]) -> None:
    for i in range(1, len(numbers)):
        j = i - 1
        while j >= 0 and numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            j -= 1


def shell_sort(numbers: Container[int]) -> None:
    gap = len(numbers)
    while gap > 0:
        gap //= 2
        for i in range(gap, len(numbers)):
            j = i
            while(j >= gap and numbers[j - gap] > numbers[j]):
                numbers[j], numbers[j - gap] = numbers[j - gap], numbers[j]
                j -= gap
