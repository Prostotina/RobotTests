import requests

# Второе задание
base_url = "https://nominatim.openstreetmap.org"


# Чтение координат из файла и превращение их в двумерный массив
def read_coordinates_from_file():
    with open('coordinates.txt', 'r') as file:
        coordinates_list = file.readlines()
        return [line.strip().split(',') for line in coordinates_list]


# Чтение адресов из файла и превращение их в двумерный массив
def read_addresses_from_file():
    with open('addresses.txt', 'r', encoding='utf-8') as file:
        addresses_list = file.readlines()
        # Разделяем наш файл на двумерный массив
        return [line.strip() for line in addresses_list]


def get_addresses_from_coodrinates():
    coordinates_list = read_coordinates_from_file()
    addresses_list = ""

    for coordinates in coordinates_list:
        latitude = coordinates[0]
        longitude = coordinates[1]
        url = f"{base_url}/reverse?format=json&lat={latitude}&lon={longitude}"
        response = requests.get(url)
        address_json = response.json()
        address_name = address_json['display_name']
        addresses_list = addresses_list + address_name + '\n'

    addresses_list = addresses_list.rstrip('\n')
    print(addresses_list)

    with open('coordinates_to_addresses.txt', 'w') as file:
        file.write(addresses_list)

    return addresses_list


def get_coordinates_from_adddreses():
    addresses_list = read_addresses_from_file()
    coordinates_list = ""

    for addresses in addresses_list:
        url = f"{base_url}/search?format=json&q={addresses}"
        response = requests.get(url)
        coordinates_json = response.json()
        coordinates_lat = coordinates_json[0]['lat']
        coordinates_lon = coordinates_json[0]['lon']
        coordinates_list = coordinates_list + coordinates_lat + ',' + coordinates_lon + '\n'

    coordinates_list = coordinates_list.rstrip('\n')
    print(coordinates_list)

    with open('addresses_to_coordinates.txt', 'w') as file:
        file.write(coordinates_list)

    return coordinates_list


get_addresses_from_coodrinates()
get_coordinates_from_adddreses()
