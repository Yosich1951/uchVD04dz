from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Текущее время и дата</title>
        </head>
        <body>
            <h1>Текущее время и дата</h1>
            <p>{{ current_time }}</p>
        </body>
        </html>
    ''', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)