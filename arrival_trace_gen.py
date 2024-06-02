import math
import random
def poisson_distribution(lambdav, cars):
    arrival_times = []
    time = 0
    for _ in range(cars):
        inter_arrival_time = -math.log(1 - random.uniform(0, 1)) / lambdav
        time += inter_arrival_time
        arrival_times.append(time)
    return arrival_times
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for number in data:
            file.write(str(number) + '\n')
#lambda=0.50
output_file_path = '0.50_lambda.txt'
poisson_numbers = poisson_distribution(0.50, 10000)
write_to_file(output_file_path, poisson_numbers)
#lambda=0.55
output_file_path01 = '0.55_lambda.txt'
poisson_numbers = poisson_distribution(0.55, 10000)
write_to_file(output_file_path01, poisson_numbers)
#lambda=0.60
output_file_path02 = '0.60_lambda.txt'
poisson_numbers = poisson_distribution(0.60, 10000)
write_to_file(output_file_path02, poisson_numbers)
#lambda=0.65
output_file_path03 = '0.65_lambda.txt'
poisson_numbers = poisson_distribution(0.65, 10000)
write_to_file(output_file_path03, poisson_numbers)

