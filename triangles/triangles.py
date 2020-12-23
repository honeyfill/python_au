import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def side_pow(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

    def is_triangle(self):
        side1 = self.side_pow(self.a, self.b)
        side2 = self.side_pow(self.a, self.c)
        side3 = self.side_pow(self.b, self.c)
        if side1 + side2 <= side3:
            return False
        if side2 + side3 <= side1:
            return False
        if side3 + side1 <= side2:
            return False
        return True

    def is_isosceles(self):
        side1 = self.side_pow(self.a, self.b)
        side2 = self.side_pow(self.a, self.c)
        side3 = self.side_pow(self.b, self.c)
        if side1 == side2 or side2 == side3 or side3 == side1:
            return True
        return False

    def square(self):
        square = abs(self.a.x * self.b.y + self.b.x * self.c.y + self.c.x * self.a.y - self.b.x * self.a.y - self.c.x *
                     self.b.y - self.a.x * self.c.y) * 0.5

        return square


class File:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        file = open(self.filename, 'r')
        result = file.readlines()
        file.close()
        return result

    def write_file(self, string):
        file = open(self.filename, 'w')
        file.write(string)
        file.close()


def checks_errors(arr):
    if len(arr) != 6:
        return False
    return True


def make_triangle(arr):
    a = Point(arr[0], arr[1])
    b = Point(arr[2], arr[3])
    c = Point(arr[4], arr[5])
    triangle = Triangle(a, b, c)
    return triangle


def main():
    name_input = sys.argv[1]
    name_output = sys.argv[2]

    ans = ''
    max_square = 0
    input = File(name_input)
    lines = input.read_file()

    if lines:
        for line in lines:
            nodes = line.split(" ")
            if checks_errors(nodes):
                for i in range(6):
                    nodes[i] = int(nodes[i])

                triangle = make_triangle(nodes)
                if triangle.is_triangle() and triangle.is_isosceles():
                    square = triangle.square()
                    if max_square < square:
                        ans = ''
                        max_square = square
                        for i in range(5):
                            ans = ans + str(nodes[i]) + ' '
                        ans = ans + str(nodes[5])

    output = File(name_output)
    if max_square > 0:
        output.write_file(ans)


if __name__ == "__main__":
    main()
