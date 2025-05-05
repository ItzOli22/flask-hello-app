from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Thank you for submitting, {name}! We will contact you at {email}."

# Vercel requires an entry point, not app.run()
if __name__ == '__main__':
    app.run(debug=True)
