from quart import Blueprint, request, jsonify
from db.db_operations import *
import base64
from quart_jwt_extended import jwt_required
from io import BytesIO


images_blueprint = Blueprint('images', __name__)

@images_blueprint.route('/update', methods=['PATCH'])
@jwt_required
async def update_image():
    try:
        data = await request.get_json()
        print(data)
        machine_id =  data.get('machine_id')
        image_data = data.get('imageData')
        binary_data = base64.b64decode(image_data)

        delete_image_from_DB(machine_id)
        upload_image_to_DB(machine_id,binary_data)

        return jsonify({'success': True, 'message': 'Image updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


@images_blueprint.route('/delete/<int:machine_id>', methods=['DELETE'])
@jwt_required
async def delete_image(machine_id):
    try:
        delete_image_from_DB(machine_id)
        return jsonify({'success': True, 'message': 'Image deleted successfully'})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
    

@images_blueprint.route('/get/<int:machine_id>', methods=['GET'])
@jwt_required
async def get_image(machine_id):
    try:
        image_data = get_image_from_DB(machine_id)

        if image_data:
            base64_image = base64.b64encode(image_data).decode('utf-8')
            return jsonify({'image': base64_image})

        else:
            return jsonify({'success': False, 'message': 'Image not found for machine_id'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})