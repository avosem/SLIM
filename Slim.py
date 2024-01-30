import time
import webbrowser
import random
vol = mix.getvolume()
otvet = 0
print('ПРИВЕТ СЭР')
name = input('ВАШЕ ИМЯ СЭР: ')
print('СЕГОДНЯ МОИ ЗАДАЧИ', name,'?')
while True:
    zadacha = input('Помоги список задач. Введи задачу: ')
    if zadacha == '2+2':
        print('4')
    if zadacha == 'помоги':
        print('1.2+2 - решает пример 2+2')
        print('2.игра - начинает игру')
        print('3.кино - открывает кинопоиск')
        print('4.ют - открывает ютуб')
        print('5.калькулятор - открывает вщитый калькулятор')
        print('6.фонк - врубает фонк на ютубе')
        print('7.звук - настраевает звук')
    if zadacha == 'игра':
        random1 = (random.randint(1,3))
        if random1 == 1:
            print('давай')
        if random1 == 2:
            print('играем')
        if random1 == 3:
            print('да', name)
        print('Правила: я загадываю число, а ты должен угадать')
        chislo = random.randint(1,10)
        otvet = input('Напиши число: ')
        if otvet == chislo:
            print('Угадал!')
        else:
            print('Не угадал!')
    if zadacha == 'кино':
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('https://www.kinopoisk.ru/')
    if zadacha == 'ют':
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('https://www.youtube.com/channel/UCjJdT78djXMWnutYOKDGlfw')
    if zadacha == 'калькулятор':
        one = int(input('первое число: '))
        two = int(input('второе число: '))
        deistv = input('вид действия(плюс,минус,умножить,делить): ')
        if deistv == 'плюс':
            otvet = one + two
            print(otvet)
        if deistv == 'минус':
            otvet = one - two
            print(otvet)
        if deistv == 'умножить':
            otvet = one * two
            print(otvet)
        if deistv == 'делить':
            otvet = one / two
            print(otvet)
    if zadacha == 'фонк':
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('https://www.youtube.com/watch?v=8WtRKHwVROs&ab_channel=Kurumi')
    
        

        
