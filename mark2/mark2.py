from flask import Flask, render_template
import os

PEOPLE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
@app.route('/general')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'one.png')
    return render_template("mark2.html", user_image = full_filename)

@app.route('/2019')
def show_index2():
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'two.png')
    return render_template("mark2_2.html", user_image2 = full_filename2)

@app.route('/2020')
def show_index3():
    full_filename3 = os.path.join(app.config['UPLOAD_FOLDER'], 'three.png')
    return render_template("mark2_3.html", user_image3 = full_filename3)



if __name__=='__main__':
    app.run(debug=1)

