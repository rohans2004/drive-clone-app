from flask import Flask, render_template, request, redirect
from db import init_db, insert_file, get_all_files, delete_file as delete_from_db
from s3_handler import upload_to_s3, delete_from_s3, set_bucket_name

app = Flask(__name__)

# ✅ Set your bucket name here
set_bucket_name('ec2-drive-clone-rohan')  # <- yahan apna bucket naam daal

# ✅ Initialize SQLite DB
init_db()

@app.route('/')
def home():
    files = get_all_files()
    return render_template("index.html", files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    filename = file.filename
    if filename == '':
        return "No selected file", 400

    try:
        s3_url = upload_to_s3(file, filename)
        insert_file(filename, s3_url)
        return redirect('/')
    except Exception as e:
        return f"Upload failed: {str(e)}", 500

@app.route('/delete/<filename>')
def delete(filename):
    try:
        delete_from_s3(filename)
        delete_from_db(filename)
        return redirect('/')
    except Exception as e:
        return f"Delete failed: {str(e)}", 500

# ✅ Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)


