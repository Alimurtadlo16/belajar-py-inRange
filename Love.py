import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Love")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

def heart_points(scale):
    points = []
    for angle in range(0, 721):
        rad = math.radians(angle / 2)
        x = scale * 16 * math.sin(rad) ** 3
        y = scale * (
            13 * math.cos(rad)
            - 5 * math.cos(2 * rad)
            - 2 * math.cos(3 * rad)
            - math.cos(4 * rad)
        )
        points.append((x, y))
    return points


def draw_outline(points, color):
    t.color(color)
    t.width(2)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for idx, (x, y) in enumerate(points):
        t.goto(x, y)
        if idx % 6 == 0:
            screen.update()
            time.sleep(0.002)
    t.goto(points[0])
    screen.update()


def blend_color(start_color, end_color, t):
    return tuple(
        int(start + (end - start) * t)
        for start, end in zip(start_color, end_color)
    )


def rgb_to_hex(rgb):
    return "#" + "".join(f"{value:02x}" for value in rgb)


def fill_heart(points, color, steps=200):
    t.width(2)
    ymin = min(y for _, y in points)
    ymax = max(y for _, y in points)
    outline_segments = list(zip(points, points[1:] + points[:1]))
    start_color = (200, 0, 0)
    end_color = (255, 90, 90)

    for step in range(steps + 1):
        y_target = ymax - (ymax - ymin) * step / steps
        intersections = []

        for (x1, y1), (x2, y2) in outline_segments:
            if y1 == y2:
                continue
            if (y_target < min(y1, y2)) or (y_target > max(y1, y2)):
                continue
            x_inter = x1 + (x2 - x1) * (y_target - y1) / (y2 - y1)
            intersections.append(x_inter)

        if len(intersections) < 2:
            continue

        intersections.sort()
        line_color = rgb_to_hex(blend_color(start_color, end_color, step / steps))
        t.color(line_color)

        for i in range(0, len(intersections) - 1, 2):
            left = intersections[i]
            right = intersections[i + 1]
            t.penup()
            t.goto(right, y_target)
            t.pendown()
            t.goto(left, y_target)
        screen.update()
        time.sleep(0.003)
    screen.update()


def draw_animated_heart(scale):
    points = heart_points(scale)
    fill_heart(points, "#ff4d6d", steps=160)
    draw_outline(points, "#ff1a1a")


draw_animated_heart(12)

t.penup()
t.goto(0, -180)
t.color("#ffb3b3")
t.write("I Love You", align="center", font=("Arial", 24, "bold"))
screen.update()
turtle.done()