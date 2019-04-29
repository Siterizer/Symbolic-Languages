import character
import variables as var


class Inky(character.Character):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.route = []
        self.vertices = [self.actual_vertex_number]
        self.helper = 0

    def move(self, pac_man_vertex_number):
        if var.check_if_new_vertex_position(self.x, self.y):
            self.actual_vertex_number = (var.get_vertex_number(self.x, self.y))
            self.route = var.graph.dijkstra(self.actual_vertex_number, self.vertices[0])
        if self.vertices[len(self.vertices) - 1] != pac_man_vertex_number:
            self.vertices.append(pac_man_vertex_number)
        if self.actual_vertex_number == self.vertices[0]:
            self.vertices.pop(0)
            if len(self.vertices) == 0:
                self.vertices.append(pac_man_vertex_number)
                self.route = var.graph.dijkstra(self.actual_vertex_number, 5)
        if len(self.route) < 2:
            self.route = var.graph.dijkstra(self.actual_vertex_number, self.vertices[0])
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




