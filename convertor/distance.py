def feet_to_meters(feet):
    return feet * 0.3048


def meters_to_feet(meters):
    return meters / 0.3048


def convert_to_meters(distance_str):
    if 'm' in distance_str:
        return float(distance_str.strip('m'))
    elif 'ft' in distance_str:
        feet = float(distance_str.strip('ft'))
        return feet_to_meters(feet)


# distance = '151ft'
# meters_distance = convert_to_meters(distance)
# print(distance, "converted to meters:", meters_distance)


def convert_to_feet(distance_str):
    if 'm' in distance_str:
        meters = float(distance_str.strip('m'))
        return meters_to_feet(meters)
    elif 'ft' in distance_str:
        return float(distance_str.strip('ft'))


# distance = '41m'
# feet_distance = convert_to_feet(distance)
# print(distance, "converted to feet:", feet_distance)