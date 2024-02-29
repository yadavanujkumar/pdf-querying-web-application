from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import os
from src import db
from icecream import ic


app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index_bootstrap.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(os.path.dirname(__file__), filename)
        file.save(file_path)
        ic("Creating a new database...")
        db.create(name = "pdf-query")
        collection = db.connect(name = "pdf-query")
        ic(collection)
        db.store("pdf-query", collection, id=filename, file_path=file_path, embedding_type = "langchain")

        # Additional actions with the uploaded PDF file
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            message = f'File "{filename}" uploaded successfully. Number of pages: {num_pages}'

        return jsonify({'message': message, 'filename': filename})

    else:
        return jsonify({'message': 'Invalid file format. Please upload a PDF file.'})



if __name__ == '__main__':
    app.run(debug=True)
