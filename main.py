# car = {
#     'BMW' : '10.000$',
#     'Subaru' : '20.000$',
#     'Lada' : '3000$',
#     'Opel' : '2000$',
#     'Haval' : '10.000$'
# }

def car_price(data):
    if car.get(data):
        print(f'Стоимость {data} на вторичном рынке состовляет - {car[data]}')
        all_car = input('Хотите посмотреть весь список машин? ')
        if all_car == 'Да':
            for k, v in car.items():
                print(f'Стоимость {k} на вторичном рынке состовляет - {v}')
    else:
        print('''Проверьте правильность ввода.
Вам доступны марки:''')
        for i in car:
            print(i)



data = input('Введите макрку машины: ')

car_price(data)