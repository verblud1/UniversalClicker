import pyautogui as p
import time

hover_wait=1.5
click_wait=1

a=[]
def start():
    
    strt=p.confirm("""
        Made Verblud1(https://github.com/verblud1)

        Легкий и универсальный кликер для ваших нужд.

    """,buttons=['Поехали!'])

    if strt=='Поехали!':
        choose()
    

def choose():
    point_selection=p.confirm('Выберите точку', buttons=['Выбрать','Запустить'])

    if point_selection=='Запустить':
        if len(a)==0:
            p.alert('Вам нужно выбрать хотя бы одну точку!')
            choose()
        else:
            start_program()

    if point_selection=='Выбрать':  
        point_array()

def start_program():
    circle_point=p.prompt('Сколько кругов?')

    if circle_point == '0':
        p.alert('Число должно быть от 1!') 
        start_program()
    if circle_point == '':
        p.alert('Вы ввели пустую строку!')
        start_program()
   
    try:
        for g in range(int(circle_point)):
            for i in a:
                p.click(i)
                time.sleep(int(click_wait))
        a.clear()
        start()

    except:        
        if p.FAILSAFE:
            p.alert('Программа была экстренно остановлена.')
            a.clear()
            start()   
 
            
def point_array():
    time.sleep(int(hover_wait))    
    a.append(p.position())
    choose()

start()