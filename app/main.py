from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
import os

from ocr import read_nik

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/get-nik", methods=["POST"])
def get_nik():
  try:
    if request.method == 'POST':
      if 'file' not in request.files:
        return jsonify({"msg": "No file part"}), 400

      file = request.files['file']
      
      if file.filename == '':
        return jsonify({"msg": "No selected file"}), 400
      
      if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        nik = read_nik(file_path)
        
        return jsonify({"msg": "Success read nik from ktp", 'data': {'nik': nik}}), 200
  except Exception as e:
    print(e)
    return jsonify({"msg": "Something went wrong"}), 500
           
  
if __name__ == "__main__":
  try:
    app.run(host="0.0.0.0", port="3000", debug=True)
  except Exception as e:
    print(e)