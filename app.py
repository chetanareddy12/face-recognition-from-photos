from flask import Flask, request, jsonify
from flask_cors import CORS
import face_recognition
import os

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes
# IMAGE_DIR = "images_directory"  # Set this to the path of your image directory
IMAGE_DIR = "/Users/dyerragunta/Desktop/images_directory"  # Replace 'your_username' with your actual username

@app.route("/compare", methods=["POST"])
def compare_faces():
    # Get the uploaded image file
    file = request.files["image"]
    target_image = face_recognition.load_image_file(file)
    target_encoding = face_recognition.face_encodings(target_image)

    if not target_encoding:
        return jsonify({"error": "No face detected in target image."}), 400

    target_encoding = target_encoding[0]
    matches = []

    # Compare target encoding with each image in the directory
    for filename in os.listdir(IMAGE_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(IMAGE_DIR, filename)
            comparison_image = face_recognition.load_image_file(image_path)
            comparison_encodings = face_recognition.face_encodings(comparison_image)

            # Compare with each face encoding found in the image
            for encoding in comparison_encodings:
                match = face_recognition.compare_faces([target_encoding], encoding)
                if match[0]:  # If there's a match
                    matches.append(filename)

    return jsonify({"matches": matches})

if __name__ == "__main__":
    app.run(debug=True)
