import turtle


def sierpinski(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order - 1, size / 2)
        t.forward(size / 2)
        sierpinski(t, order - 1, size / 2)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        sierpinski(t, order - 1, size / 2)
        t.left(60)
        t.backward(size / 2)
        t.right(60)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    win.title("Треугольник Серпинского")
    t.speed(0)
    t.up()
    t.goto(-200, -150)
    t.down()
    sierpinski(t, 4, 400)
    win.exitonclick()


if __name__ == "__main__":
    main()