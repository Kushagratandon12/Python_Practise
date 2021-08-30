from PIL import Image
import json
from flask import Flask, request

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "store_images/"


@app.route('/image', methods=['POST', 'GET'])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)

    return 'Image_Received {}'.format(img.size),200


if __name__ == "__main__":
    app.run(debug=True)
