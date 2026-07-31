from flask import Flask, render_template, request
import os
app = Flask(__name__)
import os

print("Current Folder:", os.getcwd())
print("Templates Path:", os.path.abspath("templates"))

UPLAOD_FOLDER ="uploads"
app.config['UPLOAD_FOLDER'] = UPLAOD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_resume():
     if "resume" not in request.files:
        return "No file found!"

     file = request.files["resume"]

     if file.filename == "":
        return "No file selected!"
     print(file.filename)

     if file.filename.endswith(".pdf"):
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        return "✅ Resume Uploaded Successfully!"

     return "❌ Only PDF files are allowed."

if __name__ == "__main__":
    app.run(debug=True)
