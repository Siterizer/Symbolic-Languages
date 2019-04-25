import pygame
import player as pl
import clyde as cl
import variables as var
import blinky as bl

pygame.init()
window = pygame.display.set_mode((var.screenWidth + 60, var.screenHight))
pygame.display.set_caption("Pacman")
pac_man = pl.Player(105, 181)
clyde = cl.Clyde(90, 106)
blinky = bl.Blinky(105, 113)
blinky2 = bl.Blinky(105, 85)
blinky3 = bl.Blinky(117, 85)
show = (pac_man, clyde, blinky, blinky2, blinky3)
var.initate_tab()


def redraw():
    window.fill(var.BLACK)
    window.blit(var.board, (0, 0), (228, 0, 224, 248))
    for i in var.coin:
        if var.coin[i][2] == 1:
            window.blit(var.board, (var.coin[i][0], var.coin[i][1]), (11, 11, 2, 2))
        elif var.coin[i][2] == 2:
            window.blit(var.board, (var.coin[i][0], var.coin[i][1]), (8, 184, 8, 8))
    for i in var.vertex:
        pygame.draw.rect(window, (255, 0, 0), (var.vertex[i][0], var.vertex[i][1], 2, 2))
    for i in range(0, var.number_of_characters):
        if show[i].animation_mode:
            if show[i].inactivity:
                if i == 1:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (457 + 32 * show[i].look_at, 113, var.pacmanWidth, var.pacmanHight))
                elif i == 2:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (457 + 32 * show[i].look_at, 65, var.pacmanWidth, var.pacmanHight))
                elif i == 3:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (457 + 32 * show[i].look_at, 81, var.pacmanWidth, var.pacmanHight))
                elif i == 4:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (457 + 32 * show[i].look_at, 97, var.pacmanWidth, var.pacmanHight))
                elif i == 0:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (473, 1 + 16 * show[i].look_at, var.pacmanWidth, var.pacmanHight))
                show[i].inactivity -= 1
            else:
                if i == 0:
                    window.blit(var.board, (show[i].x, show[i].y), (489, 1, var.pacmanWidth, var.pacmanHight))
            show[i].animation_mode = False
        else:
            if show[i].inactivity:
                if i == 1:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (473 + 32 * show[i].look_at, 113, var.pacmanWidth, var.pacmanHight))
                elif i == 2:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (473 + 32 * show[i].look_at, 65, var.pacmanWidth, var.pacmanHight))
                elif i == 3:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (473 + 32 * show[i].look_at, 81, var.pacmanWidth, var.pacmanHight))
                elif i == 4:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (473 + 32 * show[i].look_at, 97, var.pacmanWidth, var.pacmanHight))
                elif i == 0:
                    window.blit(var.board, (show[i].x, show[i].y),
                                (457, 1 + 16 * show[i].look_at, var.pacmanWidth, var.pacmanHight))
                show[i].inactivity -= 1
            else:
                if i == 0:
                    window.blit(var.board, (show[i].x, show[i].y), (489, 1, var.pacmanWidth, var.pacmanHight))
            show[i].animation_mode = True
    pygame.display.update()


run = True
while run:
    pygame.time.delay(var.delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        pac_man.move_right()
    if keys[pygame.K_LEFT]:
        pac_man.move_left()
    if keys[pygame.K_UP]:
        pac_man.move_up()
    if keys[pygame.K_DOWN]:
        pac_man.move_down()
    clyde.move()
    for i in range(2, var.number_of_characters):
        show[i].move(pac_man.x, pac_man.y, pac_man.actual_vertex_number)
    redraw()
    if var.check_if_colide(show):
        run = False

pygame.quit()
