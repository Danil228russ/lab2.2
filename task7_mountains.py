import turtle
import random


def mountain(t, x1, y1, x2, y2, displacement, depth):
    if depth == 0:
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
        return

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2 + random.uniform(-displacement, displacement)

    mountain(t, x1, y1, mid_x, mid_y, displacement / 2, depth - 1)
    mountain(t, mid_x, mid_y, x2, y2, displacement / 2, depth - 1)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    win.title("Фрактальные горы")
    t.speed(0)
    t.pencolor("dark blue")

    mountain(t, -300, -100, 300, -100, 120, 8)
    win.exitonclick()


if __name__ == "__main__":
    main()