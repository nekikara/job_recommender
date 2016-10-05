#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.stats import pearsonr
import numpy as np

def companies():
    return np.array([
                [ 1, 2, 2, 1, 1],
                [ 2, 2, 2, 5, 2],
                [ 3, 2, 3, 5, 27],
                [ 4, 3, 4, 5, 27],
                [ 5, 2, 3, 2, 20]])

def user():
    return np.array([1, 2, 2, 1, 1])

def main():
    for company in companies():
        r, p = pearsonr(user()[1:-1], company[1:-1])
        print('company id: {}'.format(company[0]))
        print('相関係数 r: {}'.format(r))
        print('有意確率 p: {}'.format(p))
        print('')

if __name__ == '__main__':
    main()