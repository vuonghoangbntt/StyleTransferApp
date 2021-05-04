from flask import Flask, render_template, request, redirect, url_for, abort
from model import test
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static/uploads'


@app.route('/')
def index():
    return render_template('index.html', apply=False)


@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['content']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    content_path = filename
    uploaded_file = request.files['style']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    style_path = filename
    result_file = test(os.path.join(app.config['UPLOAD_PATH'], content_path), os.path.join(
        app.config['UPLOAD_PATH'], style_path))
    # return redirect(url_for('show_result'))
    return render_template('index.html', apply=True, content_file=content_path, style_file=style_path, result_file=result_file)


if __name__ == "__main__":
    app.run(debug=True)
