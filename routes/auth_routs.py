from quart import Blueprint, request, jsonify,abort
from db.db_operations import *
from datetime import timedelta
from quart_jwt_extended import create_access_token


auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
async def login():
    try:
        data = await request.get_json()
        username = data.get('username')
        password = data.get('password')

        expiration_time = timedelta(hours=6)
        user = get_user_from_DB(username,password)
        if user:
            access_token = create_access_token(identity=username, expires_delta=expiration_time)

            return jsonify(token=access_token,username=user.get('full_name'))
        else:
            abort(401, description="Invalid credentials")
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

