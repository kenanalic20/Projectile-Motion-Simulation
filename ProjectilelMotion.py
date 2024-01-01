import numpy as np
import matplotlib.pyplot as plt


def save_results_to_file(max_height, max_height_time, horizontal_distance,total_time, filename='results.txt'):
    with open(filename, 'a') as file:
       
        file.write(f"Max Height: {max_height:.2f} meters at time {max_height_time:.2f} seconds\n")
        file.write(f"Horizontal Distance: {horizontal_distance:.2f} meters\n")
        file.write(f"Total Time of Flight : {total_time:.2f} seconds\n")
        file.write("----------\n")

        
def save_parameters_to_file(parameters, values, filename='simulation_parameters.txt'):
    with open(filename, 'w') as file:
        for param, value in zip(parameters, values):
            file.write(f"{param}: {value}\n")

 
def projectile_motion(v, theta, y0, dt, g, randomness_factor):
    x, y = [0], [y0]
    vx = v * np.cos(np.radians(theta))
    vy = v * np.sin(np.radians(theta))
  
    max_height = y0  
    max_height_time = 0

    while y[-1] >= initial_height:
        
        random_factor = np.random.normal(1, randomness_factor)
        vx *= random_factor
        vy *= random_factor

        x.append(x[-1] + vx * dt)
        vy -= g * dt
        y_val = y[-1] + vy * dt
        y.append(y_val)

        if y_val > max_height:
            max_height = y_val
            max_height_time = len(y) * dt

    horizontal_distance = x[-1]
    total_time=abs(2*vy/g) 

    
    save_results_to_file(max_height, max_height_time, horizontal_distance,total_time, filename='results.txt')
    
    return np.array(x), np.array(y),total_time

    

initial_velocity = 30.0  
launch_angle = 30.0  
initial_height = 0.0
time_step = 0.1
gravity = 9.8
randomness_factor = 0.01  
num_simulations = 5  

distances=[]
time=[]


parameters = ['Initial Velocity (m/s)', 'Launch Angle (degrees)', 'Initial Height (m)', 'Time Step (s)', 'Gravity (m/s^2)', 'Randomness Factor']
values = [initial_velocity, launch_angle, initial_height, time_step, gravity, randomness_factor]


save_parameters_to_file(parameters, values, filename='simulation_parameters.txt')


for simulation_index in range(num_simulations):
    x, y ,t= projectile_motion(initial_velocity, launch_angle, initial_height, time_step, gravity, randomness_factor)
    distances.append(x[-1])
    time.append(t)
    plt.plot(x, y)

average_distance = np.mean(distances)
with open('results.txt', 'a') as file:
    file.write(f"Average distance: {average_distance:.2f} meters\n")

average_time=np.mean(time)
with open('results.txt', 'a') as file:
    file.write(f"Average time: {average_time:.2f} seconds\n")



plt.title('Projectile Motion with Unpredictability')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.savefig('trajectory_plot.png')
plt.show()
