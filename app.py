from flask import Flask,render_template,jsonify,json,request
import config
from utils import Home_Price_Prediction

app=Flask(__name__)
@app.route("/")
def ind():
    print("welcome to flask")
    return render_template("ind.html")

@app.route("/predict",methods=["POST"])
def get_predicted_charges():
    CRIM=request.form.get("CRIM")
    ZN=request.form.get("ZN")
    INDUS=request.form.get("INDUS")
    NOX=request.form.get("NOX")
    RM=request.form.get("RM")
    AGE=request.form.get("AGE")
    DIS=request.form.get("DIS")
    RAD=request.form.get("RAD")
    TAX=request.form.get("TAX")
    PTRATIO=request.form.get("PTRATIO")
    B=request.form.get("B")
    LSTAT=request.form.get("LSTAT")
    # CRIM=0.04981
    # ZN=21.00000
    # INDUS=5.64000
    # NOX=0.43900
    # RM=5.99800
    # AGE=21.40000
    # DIS=6.81470
    # RAD=4.00000
    # TAX=843.00000
    # PTRATIO=16.80000
    # B=396.90000
    # LSTAT=8.43000
    print("CRIM:",CRIM)
    home_ins=Home_Price_Prediction(CRIM,ZN,INDUS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    result=home_ins.get_predicted_charges()
    print("charges:",result)
    return render_template("ind.html",result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)
    