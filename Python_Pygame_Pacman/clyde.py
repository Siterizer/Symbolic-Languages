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
        self.last_vertices = (self.actual_vertex_number, self.actual_vertex_number)
        self.route = []
        self.helper = 0

    def move(self):

        if var.check_if_new_vertex_position(self.x, self.y):
            self.last_vertices = (var.get_vertex_number(self.x, self.y), self.last_vertices[1])
            self.route = var.graph.dijkstra(self.last_vertices[0], self.last_vertices[1])
        if len(self.route) == 0:
            rd = random.randint(1, 67)
            self.route = var.graph.dijkstra(self.actual_vertex_number, rd)
            self.last_vertices = (self.actual_vertex_number, rd)
        print(self.route)
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




