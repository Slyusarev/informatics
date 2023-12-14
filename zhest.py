delta_m = 0.005
delta_l = 0.0005
delta_d = 10**(-5)
l = 0.33
t = 1.887
delta_t = 2.302
l = 0.3
m = 0.236
g = 10
d0 = 0.01

z1 = (delta_m/m)**2
z2 = 4*(delta_d/d0)**2
z3 = 4*((delta_t/t)*(1/(1-((2*l)/(g*t**2)))))
z4 = 4*((delta_l/l)*(1/(1-((2*l)/(g*t**2)))))

x = (z1+z2+z3+z4)**0.5
print(x)