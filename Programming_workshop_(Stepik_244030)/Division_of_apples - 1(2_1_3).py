"""
Дележ яблок - 1
N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
Входные данные
Программа получает на вход числа N и K.
Выходные данные
Программа должна вывести искомое количество яблок.

Sample Input:
5
21
Sample Output:
4
"""


N, K = int(input()), int(input())
res = K // N
print(res)
