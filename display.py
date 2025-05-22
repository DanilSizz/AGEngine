import turtle

class Display:

    def __init__(self, width, height, FPS):

        self.screen = turtle.Screen()

        self.set_screen_size(width, height)     ###
        self.FPS = FPS

    def set_screen_size(self, width, height):   ###
        self.screen.setup(width, height)        ###

    def update_screen(self):                    ###
        self.screen.update()

    def set_screen_bg(self, color):             ###
        self.screen.bgcolor(color)