from flask import Flask, send_file
from flask import render_template_string

app = Flask(__name__)

# Define your API routes here
# ...

# Fallback route to serve React app's index page
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def fallback(path):
    # React app index page (public/index.html)
    return send_file('public/index.html')

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
