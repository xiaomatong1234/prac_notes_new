from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/user')
def person():
    person_value =[
        {
            "name": "lili",
            "age": 22,
            "gender": "female"
        },
        {
            "name": "json",
            "age": 24,
            "gender": "male"
        },
        {
            "name": "thong",
            "age": 25,
            "gender": "male"
        }
    ]

    param = request.args
    param_name =param.get('name')
    param_age =param.get('age')
    return render_template("person.html",person=person_value,name=param_name,age=param_age)


if __name__ == '__main__':
    app.run(debug=True)