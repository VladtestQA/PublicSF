# 1. запрашивается количество билетов.
#
# 2. Для каждого билета запрашивается возраст
# от которого выбирается стоимость:
# Если менее 18 лет, то бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате выводится сумма к оплате.
# Если больше 3 человек, то скидка 10% на полную стоимость заказа.

ticket = int(input('Введите количество билетов на мероприятие:  '))
money = 0
person = ticket

while person != 0:
    age = int(input(f'Введите возраст посетителя № {person}:  '))
    if age < 18:
        money += 0
        print("Стоимость 0 рублей, билет бесплатный")
    elif 18 <= age < 25:
        money += 990
        print("Стоимость билета 990 рублей")
    else:
        money += 1390
        print("Стоимость билета 1390 рублей, полная стоимость")
    person -= 1

if ticket > 3:
    print("Скидка 10% при покупке более 3 билетов")
    discount = money * 0.1
    print(f"Сумма покупки {ticket} билетов со скидкой составляет {money - discount} рублей")
else:
    print(f"Сумма покупки {ticket} билетов составляет {money} рублей")
