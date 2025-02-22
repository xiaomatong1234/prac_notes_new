from flask import Flask, render_template, request, redirect, url_for, abort, flash, send_from_directory
app = Flask(__name__)
@app.route('/')
def show_static():
    return render_template("prac_stu.html")


if __name__ == '__main__':
    app.run(debug=True)
