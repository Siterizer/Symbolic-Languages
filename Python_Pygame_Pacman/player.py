import character
import variables as var


class Player(character.Character):

    def move_right(self):
        self.inactivity = 5
        if var.check_if_can_move(self.x+var.step, self.y):
            self.look_at = 0
            if self.x > var.screenWidth:
                self.x = -11
            else:
                self.x += var.step
            if var.check_if_new_vertex_position(self.x, self.y):
                self.actual_vertex_number = var.get_vertex_number(self.x, self.y)
            var.check_if_coin(self.x, self.y)

    def move_left(self):
        self.inactivity = 5
        if var.check_if_can_move(self.x - var.step, self.y):
            self.look_at = 1
            if self.x < -5:
                self.x = var.screenWidth - 1
            else:
                self.x -= var.step
            if var.check_if_new_vertex_position(self.x, self.y):
                self.actual_vertex_number = var.get_vertex_number(self.x, self.y)
            var.check_if_coin(self.x, self.y)

    def move_up(self):
        self.inactivity = 5
        if var.check_if_can_move(self.x, self.y - var.step):
            self.look_at = 2
            self.y -= var.step
            if var.check_if_new_vertex_position(self.x, self.y):
                self.actual_vertex_number = var.get_vertex_number(self.x, self.y)
            var.check_if_coin(self.x, self.y)

    def move_down(self):
        self.inactivity = 5
        if var.check_if_can_move(self.x, self.y + var.step):
            self.look_at = 3
            self.y += var.step
            if var.check_if_new_vertex_position(self.x, self.y):
                self.actual_vertex_number = var.get_vertex_number(self.x, self.y)
            var.check_if_coin(self.x, self.y)
