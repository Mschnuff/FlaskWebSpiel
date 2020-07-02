import os
from flask import request, Flask, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/moritz/kese/projects/gothonweb'
ALLOWED_EXTENSIONS = set(['txt', 'jpg'])

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and  \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/hello', methods=['POST', 'GET'])
def index():

    greeting = "Hello World"
    filename = ""

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        
        if 'datei' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        else:
            file = request.files['datei']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                pfad = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                print(pfad)
                file.save(pfad)
    
            return render_template("index_alt.html", greeting=greeting, filename=filename)
    else:
        return render_template("hello_form_alt.html")


if __name__ == "__main__":
    app.run()
