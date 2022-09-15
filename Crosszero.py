
import emoji

def REZ():
    print(emoji.emojize(f'       A      B      C\n 1    {CZ.get("A1")}     {CZ.get("B1")}     {CZ.get("C1")}\n 2    {CZ.get("A2")}     {CZ.get("B2")}     {CZ.get("C2")}\n 3    {CZ.get("A3")}     {CZ.get("B3")}     {CZ.get("C3")}'))


def WIN(D):
    W = False
    win = (('A1','A2','A3'),('B1','B2','B3'),('C1','C2','C3'),('A1','B1','C1'),('A2','B2','C2'),('A3','B3','C3'),('A1','B2','C3'),('A3','B2','C1'))
    for i in win:
        if D.get(i[0]) == D.get(i[1]) == D.get(i[2])!='':
            W = True
    return W


def FALL (T):
    Fl = True
    win = ('A1','A2','A3','B1','B2','B3','C1','C2','C3')
    for i in win:
        if T.get(i) =='':
            Fl= False
    return Fl
    

CZ = {'A1':'','B1':'','C1':'','A2':'','B2':'','C2':'','A3':'','B3':'','C3':''}

print(emoji.emojize('Приветствуем Вас в игре :cross_mark::red_circle: Здесь всего лишь пара простых правил:\n 1. Наименования клеток надо вводить в формате "буква верхнего регистра - цифра" без пробелов - А1.\n 2. Выход из игры доступен после второго хода по слову "выход".\n Удачи!'))

Ava = input(emoji.emojize('Игрок 1, выберете себе аватарку: 1. :hamster: 2. :honeybee: '))
while Ava.isdigit() == False or (int(Ava) != 1 and int(Ava) != 2):
    Ava = input(emoji.emojize('Повторить выбор аватарки: 1. :hamster: 2. :honeybee: '))


F = input (emoji.emojize(':hamster:, укажите координаты клетки, где хотите поставить :cross_mark:: ' if int(Ava)== 1 else ':honeybee:, укажите координаты клетки, где хотите поставить :cross_mark:: '))
while F not in CZ.keys():
    F = input (emoji.emojize(':hamster:, вы внесли неверные координаты клетки. Укажите координаты клетки, где хотите поставить :cross_mark:, в допустимом формате: ' if int(Ava)== 1 else ':honeybee:, вы внесли неверные координаты клетки. Укажите координаты клетки, где хотите поставить :cross_mark:, в допустимом формате: '))
CZ[F] = ':cross_mark:'
REZ()

while WIN (CZ) == False and FALL (CZ) == False:
    S = input(emoji.emojize(':honeybee:, укажите координаты клетки, где хотите поставить :red_circle:: ' if int(Ava)== 1 else ':hamster:, укажите координаты клетки, где хотите поставить :red_circle:: '))
    while (S not in CZ.keys() or CZ.get(S) !='') and S !='выход':
        S = input(emoji.emojize(':honeybee:, вы внесли неверные координаты клетки либо в данной клетке имеется значение. Укажите координаты ПУСТОЙ клетки, где хотите поставить :red_circle:, в допустимом формате: 'if int(Ava)== 1 else ':hamster:, вы внесли неверные координаты клетки либо в данной клетке имеется значение. Укажите координаты ПУСТОЙ клетки, где хотите поставить :red_circle:, в допустимом формате: '))
    if S == 'выход':
        print(emoji.emojize(':honeybee: закончил игру. Аривидерчи.'if int(Ava)== 1 else ':hamster: закончил игру. Аривидерчи.'))
        break
    CZ[S] = ':red_circle:'
    REZ()
    if WIN (CZ) == False and FALL (CZ) == False:
        F = input (emoji.emojize(':hamster:, укажите координаты клетки, где хотите поставить :cross_mark:: ' if int(Ava)== 1 else ':honeybee:, укажите координаты клетки, где хотите поставить :cross_mark:: '))
        while (F not in CZ.keys() or CZ.get(F) !='') and F !='выход':
            F = input(emoji.emojize(':hamster:, вы внесли неверные координаты клетки либо в данной клетке имеется значение. Укажите координаты ПУСТОЙ клетки, где хотите поставить :red_circle:, в допустимом формате: 'if int(Ava)== 1 else ':honeybee:, вы внесли неверные координаты клетки либо в данной клетке имеется значение. Укажите координаты ПУСТОЙ клетки, где хотите поставить :red_circle:, в допустимом формате: '))
        CZ[F] = ':cross_mark:'
        REZ()
        if WIN (CZ) == True:
            print(emoji.emojize(':hamster:, вы выйграли!!! Игра окончена!!!' if int(Ava)== 1 else ':honeybee:, вы выйграли!!! Игра окончена!!!'))
        elif FALL (CZ) == True:
            print (emoji.emojize('Свободных ходов больше не осталось :handshake:'))
        elif F == 'выход':
            print(emoji.emojize(':hamster: закончил игру. Аривидерчи.'if int(Ava)== 1 else ':honeybee: закончил игру. Аривидерчи.'))
            break
    elif WIN (CZ) == True:
        print(emoji.emojize(':honeybee:, вы выйграли!!! Игра окончена!!!' if int(Ava)== 1 else ':hamster:, вы выйграли!!! Игра окончена!!!'))
    elif FALL (CZ) == True:
        print (emoji.emojize('Свободных ходов больше не осталось :handshake:'))