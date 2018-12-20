from flask import Flask, render_template,request
import Database
from send_mail import send_email\

app=Flask(__name__)

@app.route('/mainPage',methods=['POST'])
def mainPage():
    return render_template("index.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/flush',methods=['POST'])
def flush():
    Database.flush_Db()
    Database.connect()
    return render_template("index.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        records=Database.display_all()
        email=request.form["email"]
        height=request.form['height']
        weight=request.form['weight']
        status=check_email(records,email)
        if status==0:
            Database.insert_record(email,height,weight)
            records=Database.display_all()
            weight_values=0
            height_values=0
            count=0               
            result=calc_average(records,height_values,weight_values,count)
            bmi_result=calc_bmi(int(height),int(weight))
            send_email(email, height,weight,result[2], result[1], result[0],bmi_result[0],bmi_result[1])
            return render_template("success.html")
        else:
            return render_template("error.html")


def calc_average(records,height_values,weight_values,count):
    for record in records:
            height_values=height_values+record[2]
            count=count+1
            weight_values=weight_values+record[3]           
    average_height=(height_values/count)
    average_weight=(weight_values/count)
    result=[count,average_height,average_weight]
    return result

def check_email(records,email):
    status=0
    for record in records:
            if email == record[1]:
                status=1
                break
    
    return status

def calc_bmi(h,w):
    bmi=(w*100*100)/(h*h)
    bmi_cat=""
    if bmi<18.5:
        bmi_cat="Underweight"
    elif (bmi >=18.5) and (bmi<24.9):
        bmi_cat="Normal weight"
    elif (bmi >=24.9) and (bmi<29.9):
        bmi_cat="Overweight"
    elif (bmi >29.9):
        bmi_cat="Obesity"
    bmi_result=[bmi,bmi_cat]
    return bmi_result



if __name__=="__main__":
    app.run(debug=True)
