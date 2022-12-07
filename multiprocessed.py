import ctypes
import sys
from multiprocessing import Process, Value, Array

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

def calc_line(image, line, w:int, h:int, zoom:float, pos_x:float, pos_y:float, max_iter:int):
    while True:
        with line.get_lock():
            line.value += 1
            y = line.value
        if y > h:
            break
        image[y].value = str.encode(' '.join([(f"{mandel(x, y, w, h, pos_x, pos_y, zoom, max_iter)}") for x in range(w)]))

def draw_fractal(w:int, h:int, zoom:float, pos_x:float, pos_y:float, max_iter:int):
    print("P2")
    print(f"{w} {h}")
    print(f"{max_iter}")
    line = Value('i', 0)
    image = [Array(ctypes.c_char, w*3) for _ in range(h+1)]
    processes = [Process(target=calc_line, args=(image, line, w, h, zoom, pos_x, pos_y, max_iter)) for _ in range(0,4)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    [print(l.value.decode()) for l in image]

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
