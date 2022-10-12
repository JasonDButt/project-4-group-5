
import os
from flask import Flask, request, render_template, jsonify
from other_read_puzzle import export_result
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'

@app.route("/")
def index():
    return render_template("index.html")

# ==============================================
# To read the initial puzzle from user & send it to js to visualise
@app.route("/read_puzzle", methods=["POST","GET"])
def read():

    # Read filepath & save it
    if request.method == "POST":
        enquired_file = request.files['file']
        file_name = secure_filename(enquired_file.filename)
        path = os.path.join(app.config['UPLOAD_PATH'], file_name)
        enquired_file.save(path)
        board = export_result(path)

    return render_template("solution.html", data=board.tolist(), path=path)


if __name__ == "__main__":
    app.run(debug=True)