from flask import jsonify

def render_success(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

def render_error(message, status_code=400):
    return jsonify({'status': 'error', 'message': message}), status_code
