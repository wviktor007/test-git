car = {
    'BMW' : '10.000$',
    'Subaru' : '20.000$',
    'Lada' : '3000$',
    'Opel' : '2000$',
    'Haval' : '10.000$'
}

def car_price(data):
    if car.get(data):
        print(f'Стоимость {data} на вторичном рынке состовляет - {car[data]}')
    else:
        print('''Проверьте правильность ввода.
Вам доступны марки:''')
        for i in car:
            print(i)



data = input('Введите макрку машины: ')

car_price(data)