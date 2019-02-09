from lib import distance_approximation

fuel_consumption_100km = float(input('Введите расход (в литрах) топлива нв 100 км: '))
actual_fuel_value = int(input('Введите объем имеющегося топлива: '))


print('Топлива осталось на ', distance_approximation(fuel_consumption_100km, actual_fuel_value), 'км')