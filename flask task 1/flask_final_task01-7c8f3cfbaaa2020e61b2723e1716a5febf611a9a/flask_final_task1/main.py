from flask import Flask, render_template, request, redirect, url_for
from model import connectToDB, insertDB, viewData, updateData, deleteData, clearAll

app = Flask(__name__)

@app.route('/')
def index():
    connectToDB()
    test = viewData()
    return render_template('home.html', test=test)

@app.route('/add', methods =["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        connectToDB()
        insertDB(title)
        return redirect(url_for("index"))
    elif request.method == "GET":
        return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    connectToDB()
    updateData(id)
    return redirect(url_for("index"))

@app.route('/delete/<int:id>')
def delete(id):
    connectToDB()
    deleteData(id)
    return redirect(url_for("index"))

@app.route('/clear')
def clear():
    # connectToDB()
    clearAll()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)