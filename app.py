from quart import Quart
from routes.auth_routs import auth_blueprint
from routes.images_routes import images_blueprint
from routes.machines_routes import machines_blueprint
from routes.manufacturers_routes import manufacturers_blueprint
from quart_cors import cors
from quart_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()

app = Quart(__name__)
app.config["JWT_SECRET_KEY"] = "secret_key" 
jwt = JWTManager(app)
app = cors(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(images_blueprint, url_prefix='/images')
app.register_blueprint(machines_blueprint, url_prefix='/machines')
app.register_blueprint(manufacturers_blueprint, url_prefix='/manufacturers')

if __name__ == '__main__':
    app.run()