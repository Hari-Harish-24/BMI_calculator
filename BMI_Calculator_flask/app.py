from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def rootpage():
    bmi=""
    if request.method == "POST" and "uweight" in request.form:
        weight = float(request.form.get("uweight"))
        height = float(request.form.get("uheight"))
        bmi = cal_bmi(weight,height)
    return render_template('calculator.html',bmi=bmi) 


def cal_bmi(weight,height):
    return round((weight/(height/100)**2),2)

app.run()