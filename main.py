#Импорт библиотек и файлов
from draw import *
from ball import *
from anim import *

#Функция Main с единой ответственностью - вызывать другую функцию
#где и происходит выполнение кода
def main():
  
  #Запись в переменную объекта класса Шар (x, y, Radius)
  BB = Ball(0, 0, 100)
  
  #Создание объекта класса Аним (FPS, Draw, Ball)
  #и вызов функции anim(Объект шара)
  Anim(60, Draw()).anim(BB)

#Вызов Main
main()