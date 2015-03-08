import os
from flask import Flask, render_template, redirect, request, send_from_directory, url_for
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug import secure_filename
import config

app = Flask(__name__)
toolbar = DebugToolbarExtension(app)
app.debug = config.DEBUG
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['SECRET_KEY'] = config.SECRET_KEY


@app.route('/')
def main_page():
	return render_template('map.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		uploaded_file = request.files['file']
		if uploaded_file:
			filename = secure_filename(uploaded_file.filename)
			uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('serve_file', filename=filename))
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form action="" method=post enctype=multipart/form-data>
		<p><input type=file name=file>
			<input type=submit value=Upload>
	</form>
	'''

@app.route('/uploads/<filename>')
def serve_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
	app.run()
