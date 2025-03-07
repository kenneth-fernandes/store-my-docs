from flask_limiter import Limiter
from flask_jwt_extended import JWTManager
from flask_talisman import Talisman
from flask_cors import CORS
from flask_limiter.util import get_remote_address

# Uses in-memory storage for tracking rate limits as default
limiter = Limiter(get_remote_address, default_limits=["200 per day", "50 per hour"])

jwt = JWTManager()
talisman = Talisman()
cors = CORS()
