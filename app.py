from flask import Flask, request, render_template
# from read_puzzle import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# ==============================================
# To read the initial file path
@app.route("/project-4-group-5", methods=["POST","GET"])
def puzzle():
    if request.method == "POST":
        input_path =request.form.get("url_path")
        # data = export_result(input_path)
    return render_template("modify.html", test=input_path)


if __name__ == "__main__":
    app.run(debug=True)