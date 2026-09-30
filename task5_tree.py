import turtle
import random


def tree(branch_len, t, thickness):
    if branch_len > 5:
        t.pensize(thickness)
       
        if branch_len < 20:
            t.pencolor("green")
        else:
            t.pencolor("brown")

        t.forward(branch_len)

        
        angle = random.uniform(15, 45)
        t.right(angle)
        tree(branch_len - random.uniform(10, 20), t, thickness * 0.7)

        t.left(2 * angle)
        tree(branch_len - random.uniform(10, 20), t, thickness * 0.7)

        t.right(angle)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    win.title("Рекурсивное дерево")
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.speed(0)
    tree(100, t, 10)
    win.exitonclick()


if __name__ == "__main__":
    main()