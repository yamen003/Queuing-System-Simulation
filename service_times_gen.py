import numpy as np
import random
def deterministic(start , cars):
    times=[]
    time=start
    for i in range(cars):
        time=1.5
        times.append(time);
    return times
#------------------------------------------
def exponential(avg):
    random_numbers = np.random.exponential(scale=avg, size=10000)
    return random_numbers
#------------------------------------------
def hyperexp(avg1,avg2,sizec):
    random_numbers1 = np.random.exponential(scale=avg1, size=sizec//2)
    random_numbers2 = np.random.exponential(scale=avg2, size=sizec//2)
    total_list=list(random_numbers1)+list(random_numbers2)
    random.shuffle(total_list)
    return total_list
#-------------------------------------------
def correxp(avg, corr, size):
    x=np.random.exponential(scale=avg, size=size)
    y=np.random.exponential(scale=avg, size=size)
    corr_exp1=x
    corr_exp2=corr*x+np.sqrt(1-corr**2)*y
    correxpfin=avg+corr_exp1
    return correxpfin
#------------------------------------------
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for number in data:
            file.write(str(number) + '\n')

#Deterministic
output_file_path = 'deterministic.txt'
numbers_det = deterministic(0, 10000)
write_to_file(output_file_path, numbers_det)
#exponential
output_file_path01= 'exponential.txt'
numbers_exp = exponential(1.5)
write_to_file(output_file_path01, numbers_exp)
#hyper-exponential
output_file_path02= 'hyp_exponential.txt'
numbers_hypexp = hyperexp(1.0,2.0,10000)
write_to_file(output_file_path02, numbers_hypexp)
#corr-exponential
output_file_path03= 'corr_exponential.txt'
numbers_correxp = correxp(1.5,0.2,10000)
write_to_file(output_file_path03, numbers_correxp)