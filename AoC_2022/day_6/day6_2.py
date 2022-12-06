from day6_data import datastream

signal_size = 14
count = signal_size

for i in range(len(datastream)):
    if len(set(datastream[i:i + signal_size])) != signal_size:
        count += 1
    else:
        break

print(count)  # 2145
