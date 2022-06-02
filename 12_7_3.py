
money = float(input('Введите сумму вклада:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
bank1 = round(per_cent.get('ТКБ') / 100 * money)
bank2 = round(per_cent.get('СКБ') / 100 * money)
bank3 = round(per_cent.get('ВТБ') / 100 * money)
bank4 = round(per_cent.get('СБЕР') / 100 * money)
deposit = [bank1,bank2,bank3,bank4]
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ' + str(max(deposit)))