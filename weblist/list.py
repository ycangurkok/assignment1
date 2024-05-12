from flask import Flask, jsonify, request, render_template # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from dataclasses import dataclass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@db/example'
db = SQLAlchemy(app)

@dataclass
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/records')
def get_records():
    records = Name.query.all()
    return jsonify([{'id': record.id, 'first_name': record.first_name, 'last_name': record.last_name} for record in records])

@app.route('/<int:id>', methods=['DELETE'])
def delete_record(id):
    record = Name.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({'message': 'Record deleted'})

if __name__ == '__main__':
    app.run(debug=True)
