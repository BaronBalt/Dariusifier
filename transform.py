import cv2

def brightness(p):
    return 0.299*p[2] + 0.587*p[1] + 0.114*p[0]

def compute_pixel_moves(source, target):

    source = cv2.resize(source, (512,512))
    target = cv2.resize(target, (512,512))

    h,w,_ = source.shape

    source_pixels = []
    target_pixels = []

    for y in range(h):
        for x in range(w):
            source_pixels.append({
                "x":x,
                "y":y,
                "color":source[y,x]
            })

            target_pixels.append({
                "x":x,
                "y":y,
                "brightness":brightness(target[y,x])
            })

    source_sorted = sorted(source_pixels, key=lambda p: brightness(p["color"]))
    target_sorted = sorted(target_pixels, key=lambda p: p["brightness"])

    pixels = []

    for s,t in zip(source_sorted,target_sorted):

        pixels.append({
            "x0":s["x"],
            "y0":s["y"],
            "x1":t["x"],
            "y1":t["y"],
            "color":s["color"].tolist()
        })

    return pixels