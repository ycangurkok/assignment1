from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='web_form/templates')

# Route to display the form
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # You could process or save form data here
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    total_records = 1  # Example variable, should be dynamic based on your data
    
    # Redirect to the success page with total_records variable
    return render_template('success.html', total_records=total_records)

if __name__ == '__main__':
    app.run(debug=True)
