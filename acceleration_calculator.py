def acceleration(v1, v2, t1, t2):
    
    accel = (v2 - v1) / (t2 - t1)
    
    return accel

print(acceleration(0, 10, 0, 20))