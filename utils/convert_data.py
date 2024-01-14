def convert_user_to_obj(user):
    if not user:
        return None
    return {'username': user[0], 'full_name':user[1], 'password':user[2]}

def convert_machines_to_objects(unorganized_data):
    total = unorganized_data[-1][0]
    unorganized_data = unorganized_data[:-1]
    data = []
    for machine in unorganized_data:
        machine_object = {
        'id':machine[0],
       'name':machine[1],
       'manufacturer_name':machine[6],
       'purchased_at':machine[2],
       'manufacture_year':machine[3],
       'status':machine[4],
       'capacity':machine[5]}
        data.append(machine_object)
    return {'data':data, 'total':total}

def convert_manufacturers_to_objects(data):
    new_data = []
    for manufacturer in data:
        new_data.append({
            'id':manufacturer[0],
            'name':manufacturer[1],
        })
    return new_data