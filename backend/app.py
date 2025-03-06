from flask import Flask
from flask_jwt_extended import JWTManager

from config import JWT_CONFIG
from routes.document import document_bp
from routes.auth import auth_bp

app = Flask(__name__)

# Registering the routes using Blueprint
app.register_blueprint(document_bp)
app.register_blueprint(auth_bp)

# JWT Secret key
app.config["JWT_SECRET_KEY"] = JWT_CONFIG["secret"]

# Initialize JWT Manager
jwt = JWTManager(app)

@app.route('/')
def home():
    return {"message": "API is running!"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)