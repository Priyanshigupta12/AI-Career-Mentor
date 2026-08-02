from flask import Flask, render_template, request
from resume_parser import (
    extract_text,
    extract_skills,
    calculate_score,
    recommend_career,
    learning_roadmap
)
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# uploads folder automatically create ho jayega
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


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

    if file and file.filename.lower().endswith(".pdf"):

        # Save PDF
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Extract Text
        text = extract_text(file_path)

        # Find Skills
        skills = extract_skills(text)

        # Resume Score
        score, missing = calculate_score(skills)

        # Career Recommendation
        career = recommend_career(skills)

        # Learning Roadmap
        roadmap = learning_roadmap(career)

        return render_template(
            "result.html",
            skills=skills,
            score=score,
            missing=missing,
            career=career,
            roadmap=roadmap
        )

    return "❌ Only PDF files are allowed."


if __name__ == "__main__":
    app.run(debug=True)