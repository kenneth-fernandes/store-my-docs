import logging

from flasgger import swag_from
from flask import Flask, jsonify
from config import JWT_CONFIG
from extensions import talisman, cors, limiter, jwt, swagger
from routes.document import document_bp
from routes.auth import auth_bp
from config import SWAGGER_API_CONFIG, SWAGGER, CONTENT_SECURITY_POLICY

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
talisman.init_app(app, content_security_policy=CONTENT_SECURITY_POLICY)
# Enable CORS for frontend access
cors.init_app(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})

# Swagger Configurations
swagger.init_app(app)

@app.errorhandler(404)
def not_found(e):
    logging.warning(f"404 Not Found: {str(e)}")
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    logging.error(f"500 Internal Server Error: {str(e)}")
    return jsonify({"error": "Internal Server Error"}), 500

@app.route("/apidocs/swagger.json")
@swag_from(SWAGGER_API_CONFIG["app"]["swagger_json"])
def swagger_json():
    logging.info("Swagger json called")
    return jsonify(SWAGGER)


@app.route('/')
@limiter.limit("10 per minute")
def home():
    logging.info("API Health Check Called")
    return {"message": "API is running!"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)