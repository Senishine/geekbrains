time = int(input('Введите время в секундах: '))
hours = int((time / 3600) % 24)
minutes = int((time / 60) % 60)
seconds = int(time % 60)

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

