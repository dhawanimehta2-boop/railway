from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Dummy train data
trains = [
    {"no": "12345", "name": "Rajdhani Express", "from": "Delhi", "to": "Kolkata", "time": "10:00 AM"},
    {"no": "22334", "name": "Shatabdi Express", "from": "Delhi", "to": "Lucknow", "time": "06:00 AM"},
    {"no": "99887", "name": "Duronto Express", "from": "Mumbai", "to": "Delhi", "time": "08:30 PM"}
]

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Search trains route
@app.route('/search', methods=['POST'])
def search():
    return render_template('search_results.html', trains=trains)

# Booking form route
@app.route('/book/<train_no>', methods=['GET', 'POST'])
def book(train_no):
    train = next((t for t in trains if t["no"] == train_no), None)
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('ticket', name=name, train=train["name"]))
    return render_template('booking.html', train=train)

# Ticket confirmation route
@app.route('/ticket')
def ticket():
    pnr = random.randint(1000000000, 9999999999)
    name = request.args.get('name')
    train = request.args.get('train')
    return render_template('ticket.html', pnr=pnr, name=name, train=train)

if __name__ == '__main__':
    app.run(debug=True)
