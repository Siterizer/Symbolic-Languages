import character
import random
import variables as var


class Clyde(character.Character):

    def __init__(self, x, y):
        var.number_of_characters += 1
        self.x = x
        self.y = y
        self.look_at = 0
        self.animation_mode = 0
        self.inactivity = 0
        self.actual_vertex_number = var.get_vertex_number(x, y)
        self.last_vertices = ()
        self.route = []
        self.helper = 0

    def move(self):
        rd = random.randint(0, 3)
        if rd == 0:
            self.move_right()
        elif rd == 1:
            self.move_left()
        elif rd == 2:
            self.move_up()
        elif rd == 3:
            self.move_down()




