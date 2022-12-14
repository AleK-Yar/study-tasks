"""
Электронные часы - 2
Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов,
потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
С начала суток прошло n секунд. Выведите, что покажут часы.
Входные данные
Вводится целое число n.
Выходные данные
Выведите ответ на задачу, соблюдая требуемый формат.

Sample Input:
3602
Sample Output:
1:00:02
"""


n = int(input())
secunds = n % 60
minutes = (n // 60) % 60
hours = ((n // 60) // 60) % 24

print(f'{hours}:{minutes:02}:{secunds:02}')
