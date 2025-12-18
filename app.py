import os
from flask import Flask, render_template, request
from fileReader import extractText
from plagiarismEngine import checkPlagiarismMultiple

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None

    if request.method == "POST":
        uploadedFiles = request.files.getlist("files[]")

        # REMOVE empty selections
        uploadedFiles = [f for f in uploadedFiles if f.filename != ""]

        # VALIDATION: 2–100 files only
        if len(uploadedFiles) < 2:
            error = "Please upload at least 2 files."
        elif len(uploadedFiles) > 100:
            error = "You can upload maximum 100 files."
        else:
            fileTexts = []
            fileNames = []

            for file in uploadedFiles:
                filePath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filePath)

                text = extractText(filePath)
                if text.strip():
                    fileTexts.append(text)
                    fileNames.append(file.filename)

            if len(fileTexts) >= 2:
                results = checkPlagiarismMultiple(fileTexts, fileNames)

    return render_template("index.html", results=results, error=error)

if __name__ == "__main__":
    app.run(debug=True)
