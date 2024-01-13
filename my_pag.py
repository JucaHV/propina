from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_propina', methods=['POST'])
def calcular_propina():
    if request.method == 'POST':
        bill = float(request.form['bill'])
        tip_percentage = float(request.form['tip'])
        people = int(request.form['people'])

        dec_tip = tip_percentage / 100
        total_tip = round(bill * dec_tip)
        total_bill = bill + total_tip
        each_person = round(total_bill / people)

        return render_template('resultado.html', total_tip=total_tip, total_bill=total_bill, each_person=each_person)

if __name__ == '__main__':
    app.run(debug=True)
