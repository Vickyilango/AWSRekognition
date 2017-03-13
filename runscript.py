import os
import boto3
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import detectfaces_function
import detectlabels_function

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('frontindex.html')		   

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        username = request.form['name']
        gendertype = request.form['gender']
        file = request.files['file']
        name = file.filename
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            s3 = boto3.client('s3')
            
            s3.upload_fileobj(file,'rekbucket',name)
    	    detect_group, detect_noface, detect_male = detectfaces_function.detectfaces(name)
            text_found , person_found = detectlabels_function.detectlabels(name)
            
            return render_template('backindex.html', group = detect_group, noface = detect_noface ,male = detect_male ,text = text_found , person = person_found , username = username , gendertype = gendertype)
		
            
    		
            
    return render_template('frontindex.html')


	
if __name__ == '__main__':
   #app.run(debug = True)
   app.run(host='0.0.0.0')
   app.run(debug = True)
