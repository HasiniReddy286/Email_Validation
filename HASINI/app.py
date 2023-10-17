from flask import Flask, render_template, request, jsonify
from validate_email import is_valid_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def email_validator():
    if request.method == 'POST':
        email = request.form['email']
        is_valid = is_valid_email(email)
        return jsonify({'is_valid': is_valid})

    return render_template('email_validator.html')

if __name__ == '__main__':
    app.run(debug=True)
