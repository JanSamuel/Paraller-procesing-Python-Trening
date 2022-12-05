import sys
from threading import Thread, Lock
mutex = Lock()
y = 0

def get_y():
    global y
    global mutex
    with mutex:
        y += 1
        result = y
    return result

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

def calc_line(image, w:int, h:int, zoom:float, pos_x:float, pos_y:float, max_iter:int):
    while True:
        line = get_y()
        if line > h:
            return
        image.insert(line, ' '.join([(f"{mandel(x, line, w, h, pos_x, pos_y, zoom, max_iter)}") for x in range(w)]))

def draw_fractal(w:int, h:int, zoom:float, pos_x:float, pos_y:float, max_iter:int):
    print("P2")
    print(f"{w} {h}")
    print(f"{max_iter}")
    image = []
    threads = [Thread(target=calc_line, args=(image, w, h, zoom, pos_x, pos_y, max_iter)) for _ in range(0,4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(*image)

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
