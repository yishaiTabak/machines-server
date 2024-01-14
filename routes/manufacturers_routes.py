from quart import Blueprint, request, jsonify
from db.db_operations import *
from quart_jwt_extended import jwt_required


manufacturers_blueprint = Blueprint('manufacturers', __name__)

@manufacturers_blueprint.route('/get', methods=['GET'])
@jwt_required
async def get_manufacturers_names():
    try:
        manufacturers = get_manufacturers_from_DB()
        return manufacturers

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
    
