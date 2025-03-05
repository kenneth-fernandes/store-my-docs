from flask import Flask
from routes.document import document_bp

app = Flask(__name__)

# Registering the routes using Blueprint
app.register_blueprint(document_bp)

@app.route('/')
def home():
    return {"message": "API is running!"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)