from flask import Flask
from api.controller.user import user_blueprint
from api.controller.reservation import reservation_blueprint
from api.controller.apartment import apartment_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(reservation_blueprint, url_prefix='/reservation')
app.register_blueprint(apartment_blueprint, url_prefix='/apartment')


if __name__ == "__main__":
    app.run(debug=True)