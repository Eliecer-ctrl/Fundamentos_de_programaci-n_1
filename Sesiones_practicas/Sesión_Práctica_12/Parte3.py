
def load_car_data(filename):
    cars_by_plate = {}    
    plates_by_brand = {}  
    plates_by_island = {} 
    with open(filename, 'r') as infile, open("errors.log", 'w') as error_file:
        for line in infile:
            original_line = line.strip()
            if not original_line:
                continue
            result = check_car_data(original_line)
            if len(result) == 6:
                plate, brand, model, propulsion, power, island = result
                car_details = [brand, model, propulsion, power, island]
                cars_by_plate[plate] = car_details
                if brand not in plates_by_brand:
                    plates_by_brand[brand] = []
                plates_by_brand[brand].append(plate)
                if island not in plates_by_island:
                    plates_by_island[island] = []
                plates_by_island[island].append(plate)
            else:
                error_file.write(original_line + "\n")
    return (cars_by_plate, plates_by_brand, plates_by_island)

# Nota: Para la ejecución real, las funciones 'norm_mat' y 'check_car_data'
# deben estar definidas o correctamente importadas desde 'parte1' y 'parte2'.