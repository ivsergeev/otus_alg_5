# -*- coding: utf-8 -*-
import time
from sort import bubble_sort, insertion_sort, shell_sort, create_numbers


def sort_performance():
    algs = [bubble_sort, insertion_sort, shell_sort,]
    for idx, alg in enumerate(algs):
        print(alg)
        for n in range(3, 6):            
            numbers = create_numbers(10**n)
            start = time.time()
            alg(numbers[:])
            stop = time.time()
            print('n={} {} ms'.format(10**n, round((stop - start) * 10000) * 0.1))


sort_performance()