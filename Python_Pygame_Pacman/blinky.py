import character
import numpy as np
import variables as var


class Blinky(character.Character):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.last_vertices = ()
        self.route = []
        self.helper = 0

    def move(self, pac_man_x, pac_man_y, pac_man_vertex_number):

        if self.last_vertices != (self.actual_vertex_number, pac_man_vertex_number):
            self.last_vertices = (self.actual_vertex_number, pac_man_vertex_number)
            if var.check_if_new_vertex_position(self.x, self.y):
                self.route = var.graph.dijkstra(self.actual_vertex_number, pac_man_vertex_number)
        if len(self.route) == 0:
            if self.helper == 4:
                distance_right = var.distance(self.x + var.step, self.y, pac_man_x, pac_man_y)
                distance_left = var.distance(self.x - var.step, self.y, pac_man_x, pac_man_y)
                distance_up = var.distance(self.x, self.y - var.step, pac_man_x, pac_man_y)
                distance_down = var.distance(self.x, self.y + var.step, pac_man_x, pac_man_y)
                self.helper = np.argmin([distance_right, distance_left, distance_up, distance_down])
            else:
                if self.helper == 0:
                    self.move_right()
                elif self.helper == 1:
                    self.move_left()
                elif self.helper == 2:
                    self.move_up()
                elif self.helper == 3:
                    self.move_down()
        else:
            self.helper = 4
            a, b = var.vertex[self.route[0]], var.vertex[self.route[1]]
            x = a[0] - b[0]
            y = a[1] - b[1]
            if y > 0:
                self.move_up()
            if y < 0:
                self.move_down()
            if x > 0:
                self.move_left()
            if x < 0:
                self.move_right()
