from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home_page():

    return render_template('home_page.html',title='展示人员信息')

@app.route('/person')
def person_page():
    person_info= [{
        "name" :"lily",
        "age":22,
        "gender":"male",
    },
        {
            "name": "Json",
            "age": 23,
            "gender": "female",
        }
    ]
    return render_template('home_page.html',person=person_info)
if __name__ == '__main__':
    app.run(debug=True)