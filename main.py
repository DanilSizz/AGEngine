# Импорт библиотек и файлов
from draw import *
from ball import *
from anim import *
from engine import *  ### Импорт класса engine

def main():
  
  BB = [Ball(0, 0, 50), Ball(10, 10, 50)]
  DR = Draw()
  DR.setColor("Black")
  DR.setPenSize(2)

  AN = Anim(DR, BB)
  
  game = Engine(AN, 60)   ### Создаём переменную, в которой хранится экземпляр класса Engine()
  game.gameCycle()        ### Вызов функции запуска цикла обновления сцены

main()