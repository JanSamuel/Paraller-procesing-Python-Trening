import sys

def mandel(x:float, y:float, w:float, h:float, pos_x:float, pos_y:float, zoom:float, max:int):
    xd = (((x / w) - 0.5) * (w / h)) / (zoom / 4.0) + pos_x
    yd = ((y / h) - 0.5) / (zoom / 4.0) - pos_y
    c = complex(xd, yd)
    z = complex(c)
    iteration = 0
    while abs(z) < 2 and iteration < max:
        z = z * z + c;
        iteration += 1
    return iteration;

def calc_line(x:int, y:int, w:int, h:int, zoom:float, pos_x:float, pos_y:float, max_iter:int):
    print(f"{mandel(x, y, w, h, pos_x, pos_y, zoom, max_iter)} ")

def draw_fractal(w:int, h:int, zoom:float, pos_x:float, pos_y:float, max_iter:int):
    print("P2\n")
    print(f"{w} {h}\n")
    print(f"{max_iter}\n")
    [[calc_line(x, y, w, h, zoom, pos_x, pos_y, max_iter) for x in range(w)] for y in range(h)]

def main():
    w = 800;
    h = 600;
    zoom = 1.0;
    pos_x = -0.0;
    pos_y = -0.0;
    max_iter = 24;
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print(f"usage:\n{sys.argv[0]} w h max_iter zoom x y")
            return
        w = int(sys.argv[1])
    if len(sys.argv) >= 3:
        h = int(sys.argv[2])
    if len(sys.argv) >= 4:
        max_iter = int(sys.argv[3])
    if len(sys.argv) >= 5:
        zoom = int(sys.argv[4])
    if len(sys.argv) >= 6:
        pos_x = int(sys.argv[5])
    if len(sys.argv) >= 7:
        pos_y = int(sys.argv[6])
    draw_fractal(w, h, zoom, pos_x, pos_y, max_iter);

if __name__ == "__main__":
    main()
