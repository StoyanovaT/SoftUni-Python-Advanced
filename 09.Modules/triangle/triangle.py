from triangle.line import print_line


def print_triangle(n):
    for i in range(n):
        print_line(i + 1)

    for i in range(n - 2, -1, -1):
        print_line(i + 1)