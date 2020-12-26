dist = float(input('Введите начальную дистанцию (км): '))
end_dist = float(input('Введите конечную дистанцию (км): '))
day = 1

while dist < end_dist:
    dist = dist * 1.1
    day += 1
print(f'На {day}-й день спортсмен достигнет результата {end_dist} км.')






