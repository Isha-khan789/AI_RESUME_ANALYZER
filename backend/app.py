from flask import Flask,request

app = Flask(__name__)

@app.route("/test",methods=["POST"])
def test():
    return "Resume Analyzer Backend is running!"
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