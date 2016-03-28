from flask import Flask, url_for, request, render_template
from app import app
from dmath import *

class FreelanceEntry:
	def __init__(self,**kwargs):
		def regular_pay():
		    if self.hours <= 8:
		        return self.hours * self.hourly_rate
		    elif self.hours > 8:
		        return (self.hourly_rate * 8)
		    else: return 0

		def regular_hours():
		    if self.hours <= 8:
		        return self.hours
		    elif self.hours > 8:
		        return abs((self.hours-8)-self.hours) 
		    else: return 0

		def overtime_pay():
			if self.hours > 8 and self.hours <= 12:
				return (self.hours - 8) * (self.hourly_rate * 1.5)
			elif self.hours > 12:
			    return (4 * self.hourly_rate) * 1.5
			else: return 0

		def overtime_hours():
		    if self.hours > 8 and self.hours <= 12:
		        return (self.hours - 8)
		    elif self.hours > 12:
		        return 4
		    else: return 0

		def doubletime_pay():
		        if self.hours > 12:
		            return (self.hours - 12) * (self.hourly_rate * 2)
		        else: return 0

		def doubletime_hours():
		        if self.hours > 12:
		            return (self.hours - 12)
		        else: return 0
		if kwargs.get('guaranteed_rate',None) and kwargs.get('guaranteed_hours',None) and kwargs.get('hours_worked',None):
			gh = int(kwargs['guaranteed_hours'])
			self.hourly_rate = int(kwargs['guaranteed_rate']) / (RegularHours(gh) + (1.5*(OverTimeHours(gh))))
			self.hours = int(kwargs['hours_worked'])
		elif kwargs.get('hourly_rate',None):
			self.hourly_rate = int(kwargs['hourly_rate'])
			self.hours = 4
		else:
			raise ValueError(kwargs)
		self.regular   =   {'hours':regular_hours()   , 'pay':regular_pay(), 'rate': self.hourly_rate}
		self.overtime   =  {'hours':overtime_hours()  , 'pay':overtime_pay(), 'rate': self.hourly_rate * 1.5}
		self.doubletime =  {'hours':doubletime_hours(), 'pay':doubletime_pay(), 'rate': self.hourly_rate * 2}
		self.total = {
			'hours': self.regular['hours'] + self.overtime['hours'] + self.doubletime['hours'],
			'pay': self.regular['pay'] + self.overtime['pay'] + self.doubletime['pay']
		}

@app.route('/',methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return render_template('SelectOption.html' );
		
	elif request.method == 'POST':
		if request.form['submit'] == 'Submit Option1':
			entry = FreelanceEntry(
				guaranteed_rate = request.form['GuranteedRate'],
				guaranteed_hours = request.form['GuranteedHours'],
				hours_worked = request.form['HoursWorked']
				)
		elif request.form['submit'] == 'Submit Option2':
			entry = FreelanceEntry(hourly_rate = request.form['HourlyRate'])
	return render_template('test2.html',entry=entry);