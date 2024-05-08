from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@db/example'
db = SQLAlchemy(app)

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    # Check if name pair already exists
    if Name.query.filter_by(first_name=first_name, last_name=last_name).first():
        return redirect(url_for('name_exists'))

    new_name = Name(first_name=first_name, last_name=last_name)
    db.session.add(new_name)
    db.session.commit()
    return redirect(url_for('success'))

@app.route('/success')
def success():
    total_records = Name.query.count()
    return render_template('success.html', total_records=total_records)

@app.route('/name_exists')
def name_exists():
    return render_template('name_exists.html')

if __name__ == '__main__':
    app.run(debug=True)
