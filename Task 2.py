rate = float(input('Введите Вашу годовую процентную ставку'))
answer = input('У Вас ежемесячная процентнтая ставка?')
balance = float(input('Введите остаток задолженности'))

balance = float(balance)
rate = float(rate)

data = {}

def Calculation (rate, answer, balance):
    if (answer == 'yes' or answer == 'да'):
        percent = ((1/12) * (rate) / 100)
        sumPercent = balance * percent
    else:
        percent = (rate) / 100
        sumPercent = balance * (percent / 365 * 31)
    data['sumPercent'] = sumPercent

Calculation(rate, answer, balance)

print(data)

data['sumPercent']
