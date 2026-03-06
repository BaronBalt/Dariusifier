import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify

from transform import compute_pixel_moves

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():

    file = request.files["image"]
    file_bytes = np.frombuffer(file.read(), np.uint8)
    source = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    target = cv2.imread("darius.jpg")

    pixels = compute_pixel_moves(source,target)

    return jsonify(pixels)

app.run(debug=True)