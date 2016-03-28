from flask import Flask, url_for, request, render_template
from app import app
from dmath import *

Hours = 0
@app.route('/',methods=['GET', 'POST'])
def hello():
    
    if request.method == 'GET':
        
        return render_template('SelectOption.html' );
    
    elif request.method == 'POST':
        if request.form['submit'] == 'Submit Option1':
            GuranteedRate = request.form['GuranteedRate'];
            Hours = request.form['GuranteedHours'];
            Hours =int(Hours)
            GuranteedRate = int(GuranteedRate)
            HourlyRate = GuranteedRate / (RegularHours(Hours) + (1.5*(OverTimeHours(Hours))))
        
            Hours = request.form['HoursWorked'];
            Hours =int(Hours)
        elif request.form['submit'] == 'Submit Option2':
            HourlyRate = request.form['HourlyRate'];
            HourlyRate =int(HourlyRate)
            Hours = 4
            print Hours
        
        
        Reg_Hours = RegularHours(Hours)
        Reg_Pay = RegularPay(Hours,HourlyRate)
        Over_Time_Hours = OverTimeHours(Hours)
        Over_Time_Pay = OverTimePay(Hours,HourlyRate)
        Double_Time_Hours = DoubleTimeHours(Hours)
        Double_Time_Pay = DoubleTimePay(Hours,HourlyRate)
        #
        Total_Pay = Reg_Pay + Over_Time_Pay + Double_Time_Pay
        Total_Hours = Reg_Hours + Over_Time_Hours + Double_Time_Hours
        Over_Time_Rate = HourlyRate * 1.5
        Double_Time_Rate = HourlyRate * 2
        #return render_template('test2.html');
        return render_template('test2.html',
                                   HourlyRate = HourlyRate,
                                   Reg_Hours = Reg_Hours,
                                   Reg_Pay = Reg_Pay,
                                   Over_Time_Hours = Over_Time_Hours,
                                   Over_Time_Pay = Over_Time_Pay,
                                   Double_Time_Hours = Double_Time_Hours,
                                   Double_Time_Pay = Double_Time_Pay,
                                   Total_Pay = Total_Pay,
                                   Total_Hours = Total_Hours,
                                   Over_Time_Rate = Over_Time_Rate,
                                   Double_Time_Rate = Double_Time_Rate);