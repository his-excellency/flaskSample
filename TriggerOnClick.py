
from flask import Flask, redirect, url_for, request,render_template
import csv
app = Flask(__name__)

Options = []

@app.route('/')
def success():
   global Options
   with open('lce.csv',mode='rU',encoding='utf-8') as ff:
      dcf = csv.DictReader(ff)
      ct=0
      L=[]
      for r in dct:
         L.append(r)
         Options.append(r[])
         ct+=1
         if(ct==2):break

   return render_template('form.html',Options=Options)

@app.route('/<name>')
def showval(name):
	#
	# Do any activity here! It will work on the button click
	#
	return "You clicked a button, %s !"%name

@app.route('/form',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']

      #you get the values in checked boxes through this command here
      print(request.form.getlist('hello'))
      

      return redirect(url_for('showval',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('showval',name = user))


if __name__ == '__main__':
   app.run(debug = True)