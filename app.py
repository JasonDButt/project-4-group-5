
from flask import Flask, request, render_template
# from read_puzzle import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# ==============================================
# To read the initial file path
@app.route("/read_puzzle", methods=["POST","GET"])
def puzzle():
    if request.method == "POST":
        input_path =request.form.get("url_path")
        # data = export_result(input_path)
    return render_template("modify.html", test=input_path)

# # ==============================================
# # To read user's modification
# @app.route("/modify_puzzle", methods=["POST","GET"])
# def solve():
#     # ==============================================
#     # if the input is none, use the output for Solve Soduku & get list for rendering modify page
#     if request.method == "POST":
#         input_path =request.form.get("url_path")
#         # data = export_result(input_path)
#     return render_template("modify.html", test=input_path)

#     # ==============================================
#     # if the input with values, modify the input and serve for Solve Soduku & get list for rendering modify page
#     return render_template("modify.html", test=input_path)

if __name__ == "__main__":
    app.run(debug=True)