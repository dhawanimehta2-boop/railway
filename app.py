from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        source = request.form['source']
        destination = request.form['destination']
        date = request.form['date']
        return render_template('success.html', name=name, source=source, destination=destination, date=date)
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)
