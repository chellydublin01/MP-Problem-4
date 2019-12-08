# Machine Problem 4

# import math for solving
import math

# defining simulation of the projectile motion
def simulate_projectile_motion(s0,v0,theta0,ax,ay):
   if ay==0:
       print("Error: vertical acceleration cannot be 0")
       return  

   # naming the parameters
   t = 0
   x = 0
   y = s0 # intial height
   delta = 0.0001 # time in seconds

# storing the x and y values
   x_vals = [] 
   y_vals = []
   
# formula
   v0x = v0*math.cos(theta0*(3.141/180))
   v0y = v0*math.sin(theta0*(3.141/180)) 
   
   # storing
   x_vals.append(x)
   y_vals.append(y)

   # applying the  simulation
   while(True):
       # incrementing time
       t = t+delta

       # calculating the time parameters
       x = v0x*t + (0.5)*ax*(t*t)
       y = v0y*t + (0.5)*ay*(t*t) + s0

       # storing x and y values
       x_vals.append(x)
       y_vals.append(y)

       # simulating break condition
       if y < delta:
           break

   # plotting the result of the moting
   plt.plot(x_vals,y_vals)  
   ax = plt.gca()
   ax.set_ylim([0,max(y_vals)])
   plt.xlabel('Distance in meters')
   plt.ylabel('Height in meters')
   plt.title('Graph of the Projectile Motion')
   plt.grid()  
   plt.show()

if __name__ == '__main__':
   s0 = 2 # in meters
   v0 = 5 # in meters per sec
   theta0 = 45 # in degrees
   ax = 0 # in meters per second squared
   ay = -9.81 # in meters per second squared
   simulate_projectile_motion(s0,v0,theta0,ax,ay)  
# end of code