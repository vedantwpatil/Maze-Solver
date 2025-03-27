from tkinter import Tk, BOTH, Canvas


class Point:
    # x=0 is the left of the screen
    # y=0 is the top of the screen
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y


class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.__point1 = point1
        self.__point2 = point2

    def getPointOne(self) -> Point:
        return self.__point1

    def getPointTwo(self) -> Point:
        return self.__point2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.getPointOne().getX(),
            self.getPointOne().getY(),
            self.getPointTwo().getX(),
            self.getPointTwo().getY(),
            fill=fill_color,
            width=2,
        )


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.getCanvas(), fill_color)

    def getCanvas(self) -> Canvas:
        return self.__canvas

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
