from graphics import Line
from graphics import Point
from graphics import Window


def main():
    win = Window(800, 600)
    for i in range(10, 200, 10):
        win.draw_line(Line(Point(i + 10, i - 5), Point(i - 10, i + 10)), "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()
