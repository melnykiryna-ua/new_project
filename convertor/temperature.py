def fahrenheit_to_celsius(fahrenheit):
    return 5/9 * (fahrenheit - 32)


def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def convert_to_celsius(temperature_str):
    if '°C' in temperature_str:
        return float(temperature_str.strip('°C'))
    elif '°F' in temperature_str:
        fahrenheit = float(temperature_str.strip('°F'))
        return fahrenheit_to_celsius(fahrenheit)
    else:
        raise ValueError("Invalid temperature format")

  
# fahrenheit_temperature = "70°F"
# celsius_temperature = convert_to_celsius(fahrenheit_temperature)
# print(fahrenheit_temperature, "converted to Celsius:", celsius_temperature)


def convert_to_fahrenheit(temperature_str):
    if '°C' in temperature_str:
        celsius = float(temperature_str.strip('°C'))
        return celsius_to_fahrenheit(celsius)
    elif '°F' in temperature_str:
        return float(temperature_str.strip('°F'))
    else:
        raise ValueError("Invalid temperature format")


# celsius_temperature = "20°C"
# fahrenheit_temperature = convert_to_fahrenheit(celsius_temperature)
# print(celsius_temperature, "converted to Fahrenheit:", fahrenheit_temperature)