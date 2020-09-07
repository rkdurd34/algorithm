
fp, integer, save, junction = 56*(10**6), 110*(10**6), 80*(10**6), 16*(10**6)

cpi1, cpi2, cpi3, cpi4 = 1, 1, 4, 2
cpi1_1, cpi2_1, cpi3_1, cpi4_1 = 1*0.6, 1*0.6, 4*0.7, 2*0.7

cycletime = 2*(10**9)

time = (fp*cpi1/cycletime) + (integer*cpi2/cycletime) + (save*cpi3/cycletime) + (junction*cpi4/cycletime)
time_1 = (fp*cpi1_1/cycletime) + (integer*cpi2_1/cycletime) + (save*cpi3_1/cycletime) + (junction*cpi4_1/cycletime)


print(time,time_1)
print(time/time_1)


b=259000000000
c=86000000000.0

print(b/c)