import csv

def calculate_energy_consumed(data, start_time, end_time):
    result = {}

    for row in data:
        day, month, year, hour, minute, current = map(float, row[1:])
        timestamp = (day, month, hour, minute)

        if start_time <= timestamp <= end_time:
            if year not in result:
                result[year] = 0

            # Calculate the energy consumed (in AH)
            time_interval = 1  # Assuming time interval is 1 minute for simplicity
            energy_consumed = current * time_interval / 60  # Convert minutes to hours
            result[year] += energy_consumed

    return result

def get_user_input():
    start_day = int(input('Enter start day: '))
    start_month = int(input('Enter start month: '))
    start_hour = int(input('Enter start hour: '))
    start_minute = int(input('Enter start minute: '))

    end_day = int(input('Enter end day: '))
    end_month = int(input('Enter end month: '))
    end_hour = int(input('Enter end hour: '))
    end_minute = int(input('Enter end minute: '))

    start_time = (start_day, start_month, start_hour, start_minute)
    end_time = (end_day, end_month, end_hour, end_minute)

    return start_time, end_time

def main():
    file_path = 'data.txt'
    
    start_time, end_time = get_user_input()

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)  # Skip the header row
        data = list(reader)

    energy_consumed = calculate_energy_consumed(data, start_time, end_time)
    average = 0

    for year, energy in energy_consumed.items():
        average += energy

    average = average / len(energy_consumed.keys())
    print(f'Energy Consumption: {average:.3f} AH')

if __name__ == "__main__":
    main()
