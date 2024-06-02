import simpy
def simulate(arrivalfile,servicefile):
    def readfich(file):
        with open(file, 'r') as file:
            times = [float(line.strip()) for line in file]
        return times
    #---------------------------------------------------------------
    def car(env, car_id, service_time, car_info):
        arrival_time = env.now
        car_info.append({
            'car_id': car_id,
            'arrival_time': arrival_time,
            'start_service_time': None
        })
        with museum.request() as req:
            yield req
            start_service_time = env.now
            car_info[-1]['start_service_time'] = start_service_time
            yield env.timeout(service_time)
    #-----------------------------------------------------------
    arrival = readfich(arrivalfile)
    service = readfich(servicefile)
    env = simpy.Environment()
    museum = simpy.Resource(env, capacity=1)
    #-----------------------------------------------------------
    car_info = [] 
    #------------------------------------------------------------
    for i, (arrival_time, service_time) in enumerate(zip(arrival, service)):
        env.process(car(env, car_id=i, service_time=service_time, car_info=car_info))
        env.run(until=arrival_time)
    #-------------------------------------------------------------
    differences = [car['start_service_time'] - car['arrival_time'] for car in car_info if car['start_service_time'] is not None]
    average_difference = sum(differences) / len(differences) if differences else 0
    result="Average queuing time"+str(round(average_difference,3))
    return result
#-------------------------------------------------
def simulate_and_format(arrival_file, service_file, description):
    result = simulate(arrival_file, service_file)
    return f"{description:<70}: {result}"
lambdas = ['0.50', '0.55', '0.60', '0.65']
for l in lambdas:
    print(simulate_and_format(f'{l}_lambda.txt', 'deterministic.txt', f'Deterministic service time and {l} lambda arrival trace'))
    print(simulate_and_format(f'{l}_lambda.txt', 'exponential.txt', f'Exponential service time and {l} lambda arrival trace'))
    print(simulate_and_format(f'{l}_lambda.txt', 'hyp_exponential.txt', f'Hyper exponential service time and {l} lambda arrival trace'))
    print(simulate_and_format(f'{l}_lambda.txt', 'corr_exponential.txt', f'Correlated exponential service time and {l} lambda arrival trace'))
    print("//////////////////////////////////////////////////////////////")
