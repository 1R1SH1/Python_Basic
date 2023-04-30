import requests
import json

def planet(data):
    get_planet = requests.get(data)
    read_planet = json.loads(get_planet.text)
    for key, val in read_planet.items():
        if key == 'name':
            return val

def pilots(data):
    pilots = list()
    count = 0
    for keys, values in data.items():
        if keys == 'pilots':
            for _ in range(len(values)):
                get_pilots = {}
                data = requests.get(values[count])
                a_dict = json.loads(data.text)
                for key, val in a_dict.items():
                    if key == 'name' or key == 'height' or key == 'mass':
                        get_pilots[key] = val
                    elif key == 'homeworld':
                        get_pilots['homeworld_url'] = val
                        get_pilots['homeworld'] = planet(val)
                        count += 1
                        pilots.append(get_pilots)
    return pilots

def vehicles():
    vehicle = {}
    get_vehicle = requests.get("https://swapi.dev/api/starships/10/")
    if get_vehicle.status_code == 200:
        read_vehicle = json.loads(get_vehicle.text)
    for key, val in read_vehicle.items():
        if key == 'name' or key == 'max_atmosphering_speed' or key == 'starship_class':
            vehicle[key] = val
        elif key == 'pilots':
            vehicle[key] = pilots(read_vehicle)
    print(json.dumps(vehicle, indent=4))
    with open('Millennium_Falcon.json', 'w') as file:
        json_text = json.dump(vehicle, file, indent=4)


vehicles()
