from flask import Flask, render_template, request, redirect, url_for

# Assuming app.py is in the ASSIGNMENT1 directory, and templates are in web_form/templates
serve = Flask(__name__, template_folder='web_form/templates')

# Route to display the form
@serve.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route to handle form submission
@serve.route('/submit', methods=['POST'])
def submit():
    # Process form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    total_records = 1  # Placeholder for actual count logic
    
    # Redirect to the success page with total_records variable
    return render_template('success.html', total_records=total_records)

if __name__ == '__main__':
    serve.run(debug=True)
