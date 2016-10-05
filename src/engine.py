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
    matching = []
    print('')
    print('######### Start training #########')
    for company in companies():
        company_id = company[0]
        r, p = pearsonr(user()[1:-1], company[1:-1])
        print('company id: {}'.format(company_id))
        print('相関係数 r: {}'.format(r))
        print('有意確率 p: {}'.format(p))
        print('')
        matching.append([company_id, r])
    print('######### End training  #########')
    print('')
    matching.sort(key=lambda x:x[1], reverse=True)
    for i, v in enumerate(matching):
        print('{} 企業: {}, 類似度: {}'.format(i+1, v[0], v[1]))

if __name__ == '__main__':
    main()
