from quart import Blueprint, request, jsonify
from db.db_operations import *
from quart_jwt_extended import jwt_required


machines_blueprint = Blueprint('machines', __name__)

@machines_blueprint.route('/add', methods=['POST'])
@jwt_required
async def add_machine():
    try:
        data = await request.get_json()
        add_machine_to_DB(data)
        return jsonify({'success': True, 'message': 'machine added successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@machines_blueprint.route('/update/<int:machine_id>', methods=['PATCH'])
@jwt_required
async def update_machine(machine_id):
    try:
        data = await request.get_json()
        update_machine_in_DB(machine_id,data)
        return jsonify({'success': True, 'message': 'machine updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@machines_blueprint.route('/delete/<int:machine_id>', methods=['DELETE'])
@jwt_required
async def delete_machine(machine_id):
    try:
        delete_machine_from_DB(machine_id)
        return jsonify({'success': True, 'message': 'machine deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@machines_blueprint.route('/get', methods=['POST'])
@jwt_required
async def get_machines():
    try:
        data = await request.get_json()
        machines = get_machines_from_DB(data)
        return machines
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
