import csv
from convertor.temperature import convert_to_celsius, convert_to_fahrenheit
from convertor.distance import convert_to_meters, convert_to_feet
# from temperature import convert_to_celsius, convert_to_fahrenheit
# from distance import convert_to_meters, convert_to_feet


def process_temperature(temperature_str, target_temperature):
    temperature_str = temperature_str.replace('"', '').strip()
    
    try:
        temperature = float(temperature_str)
    except ValueError:
        return convert_to_celsius(temperature_str) if target_temperature == '°C' else convert_to_fahrenheit(temperature_str)
    else:
        return temperature if target_temperature == '°C' else convert_to_fahrenheit(temperature)


def process_distance(distance_str, target_distance):
    distance_str = distance_str.replace('"', '').strip()
 
    try:
        distance = float(distance_str)
    except ValueError:
        return convert_to_meters(distance_str) if target_distance == 'm' else convert_to_feet(distance_str)
    else:
        return distance if target_distance == 'm' else convert_to_feet(distance)

 
def process_file(input_file, output_file, target_temperature, target_distance):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            data = row[0].split(',')

            date, distance_str, temperature_str = data

            if distance_str:
                converted_distance = process_distance(distance_str, target_distance)
            else:
                converted_distance = None

            if temperature_str:
                converted_temperature = process_temperature(temperature_str, target_temperature)
            else:
                converted_temperature = None

            formatted_row = [date, f"{converted_distance:.1f}{target_distance}", f"{converted_temperature:.1f}{target_temperature}"]
            writer.writerow(formatted_row)

    print("Data has been successfully written to the output file:", output_file)


input_file = 'temperature_data.csv'
output_file = 'converted_data.csv'
target_temperature = '°C'
target_distance = 'm'
process_file(input_file, output_file, target_temperature, target_distance)
