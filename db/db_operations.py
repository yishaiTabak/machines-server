from db.db_connection import connection
from utils.convert_data import *

def get_manufacturers_from_DB():
    with connection.cursor() as crsr:
        crsr.callproc('get_manufacturers')
        result = crsr.fetchall()
    return convert_manufacturers_to_objects(result)

def add_machine_to_DB(data):
    with connection.cursor() as crsr:
        crsr.callproc('add_machine',[data['name'], data['manufacturer_id'],data['purchased_at'],data['manufacture_year'], data['status'],data['capacity']])
        connection.commit()

def update_machine_in_DB(machine_id, data):
    with connection.cursor() as crsr:
        crsr.callproc('update_machine', [
            machine_id,
            data.get('name', None),
            data.get('manufacturer_id', None),
            data.get('purchased_at', None),
            data.get('manufacture_year', None),
            data.get('status', None),
            data.get('capacity', None)
        ])
        connection.commit()

def delete_machine_from_DB(machine_id):
    with connection.cursor() as crsr:
        crsr.callproc('delete_machine', [machine_id])
        connection.commit()

def get_user_from_DB(username, password):
    with connection.cursor() as crsr:
        crsr.callproc('get_user', [username,password])
        result = crsr.fetchone()
    return convert_user_to_obj(result)

def get_machines_from_DB(filters):
    with connection.cursor() as crsr:
        crsr.callproc('get_machines', [
            filters.get('sort_by', 'id'),
            filters.get('is_asc', True),
            filters.get('limit', 100),
            filters.get('skip', 0),
            filters.get('searched_id', None),  # Provide a default value if needed
            filters.get('searched_name', '')or '',
            filters.get('filter_manufacturer', None),
            filters.get('filter_status', None)])
        result = crsr.fetchall()
    return convert_machines_to_objects(result)


def upload_image_to_DB(machine_id, image_data):
    with connection.cursor() as crsr:
        crsr.callproc('upload_image', [machine_id, image_data])
        connection.commit()

def delete_image_from_DB(machine_id):
    with connection.cursor() as crsr:
        crsr.callproc('delete_image', [machine_id])
        connection.commit()

def get_image_from_DB(machine_id):
    with connection.cursor() as crsr:
        crsr.callproc('get_image',[machine_id])
        result = crsr.fetchone()[0]
    return result
