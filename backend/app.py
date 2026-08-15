from flask import Flask,request
from resume_parser import extract_text_from_pdf
app = Flask(__name__)

@app.route("/test")
def test():
    return "Resume Analyzer Backend is running!"
@app.route("/analyze",methods=["POST"])
def analyze():
        file = request.files["file"]
        file.save("uploaded_resume.pdf")
        text = extract_text_from_pdf("uploaded_resume.pdf")
        return text
@app.route("/about")
def about():
    return"this is about"
@app.route("/contact")

def contact():
    return "this is contact"
@app.route("/hello", methods=["POST"])
def hello():
    data=request.json
    name=data["name"]
    return f"hello{name}"
if __name__ == "__main__":
    app.run(debug=True)