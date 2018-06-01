from flask import Flask, render_template, request, url_for
import numpy as np
import pickle

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def predict():
    knn = pickle.load(open("knn.pkl", "rb"))
    if request.method == 'POST':
        comment = request.form['comment']
        print comment
        data = comment.split(',')
        pre_req = np.asarray(data)
        my_prediction = knn.predict([pre_req])
        print my_prediction
    return render_template('results.html', prediction=my_prediction, comment=comment)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
