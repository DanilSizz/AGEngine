# Импорт библиотек и файлов
from draw import *
from ball import *
from anim import *
from engine import *               ### Импорт класса engine

def main():
  
  BB = Ball(0, 0, 100)
  game = Engine(Anim(Draw()), 60)  ### Создаём переменную, в которой хранится экземпляр
                                   ### класса Engine()

  game.addObject(BB)  ### Добавим наш шар в облсть видимости экземпляра Engine (переменаня game)
  game.gameCycle()    ### Вызов функции запуска цикла обновления сцены

main()