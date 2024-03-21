from flask import Flask, request, render_template, flash, jsonify
import pickle


app = Flask(__name__)
app.secret_key = "apkofriowjfkf"

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/output",methods=["POST","GET"])

#user-input
def output():
    # print("hELLO")
    if request.method == 'POST':
        
        a = request.form['age']
        a = int(a)
        # a = ((a-0.08)/(82-0.08))

        cpt = request.form['cpt']
        if cpt == "ATA":
            cpt = 1
        if cpt == "NAP":
            cpt = 2
        if cpt == "ASY":
            cpt = 3
        if cpt == "TA":
            cpt = 4

        #gender
        g = request.form['gender']
        if g == "Male":
            g = 1
        elif g == "Female":
            g = 0
        else:
            g = 2

        restingbp = request.form['restingbp']
        restingbp = int(restingbp)

        c = request.form['Cholesterol']
        c = int(c)

        f = request.form['fastingBS']
        f = int(f)
        
        restingECG = request.form['RestingECG']
        restingECG = int(restingECG)
        
        m = request.form['MaxHR']
        m =  int(m)
        
        ea = request.form['ExerciseAngina']
        ea = int(ea)
        op = request.form['Oldpeak']
        op = int(op)

        st = request.form['ST_Slope']
        if st == "Up":
            st = 0
        else:
            st = 1

        print(a,g,cpt,restingbp,c,f,restingECG,m,ea,op,st)
       
        try:
            prediction = heart_pred(a,g,cpt,restingbp,c,f,restingECG,m,ea,op,st)
            return render_template('output.html',prediction=prediction)

        except ValueError:
            return "Please Enter Valid Values"
        

#prediction-model
def heart_pred(a,g,cpt,restingbp,c,f,restingECG,m,ea,op,st):
    
    #load model
    model = pickle.load(open('model.pkl','rb'))

    #predictions
    result = model.predict([[a,g,cpt,restingbp,c,f,restingECG,m,ea,op,st]])
    print(a,g,cpt,restingbp,c,f,restingECG,m,ea,op,st)
    #output
    if result[0] == 1:
        pred = 'You have a high risk of heart disease'
    else:
        pred = 'You have low risk of heart disease'

    return pred
