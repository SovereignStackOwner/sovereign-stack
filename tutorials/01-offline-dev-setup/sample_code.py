def process_data(data_list):
    res = []
    for item in data_list:
        if item != None:
            if 'status' in item:
                if item['status'] == 'active':
                    res.append(item['val'] * 2)
    return res
    