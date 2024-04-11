from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # Use send_file to send the HTML file directly
    return send_file('myResumeHtml.html')

if __name__ == '__main__':
    app.run(debug=True)