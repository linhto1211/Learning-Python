weight = 41.5
cost_ground=20
cost_ground_premium=120
cost_drone=0

#Ground shipping
if (weight<=2):
  cost_ground+=weight*1.50
elif(weight>=2) and (weight<=6):
  cost_ground+=weight*3.00
elif(weight>=6) and (weight<=10):
  cost_ground+=weight*4.00
elif(weight>=10):
  cost_ground+=weight*4.75
print ("Ground Shipping: " + str (cost_ground))

#Ground Premium shipping
print ("Ground Premium Shipping: " + str (cost_ground_premium))

#Drone shipping
if (weight<=2):
  cost_drone+=weight*4.50
elif(weight>=2) and (weight<=6):
  cost_drone+=weight*9.00
elif(weight>=6) and (weight<=10):
  cost_drone+=weight*12.00
elif(weight>=10):
  cost_drone+=weight*14.25
print ("Drone Shipping: " + str (cost_drone))
