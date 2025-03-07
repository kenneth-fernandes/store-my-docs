from flask import Flask
from config import JWT_CONFIG
from extensions import talisman, cors, limiter, jwt
from routes.document import document_bp
from routes.auth import auth_bp

app = Flask(__name__)

# Registering the routes using Blueprint
app.register_blueprint(document_bp)
app.register_blueprint(auth_bp)

# JWT Secret key
app.config["JWT_SECRET_KEY"] = JWT_CONFIG["secret"]

# Initialize Extensions
jwt.init_app(app)
# Rate Limiting (Max Requests Per User)
limiter.init_app(app)
# Security Headers (XSS, CSP, Clickjacking Protection)
talisman.init_app(app)
# Enable CORS for frontend access
cors.init_app(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/')
@limiter.limit("10 per minute")
def home():
    return {"message": "API is running!"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)