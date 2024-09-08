from flask import Flask, jsonify
from app.config.config import Config
from app.routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_bp)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'message': 'Request was successful.',
        'status': 'success',
        'code': 200
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
