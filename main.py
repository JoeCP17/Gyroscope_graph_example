import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Flat.csv')

fig = plt.figure(figsize=(10, 11))
ax = fig.add_subplot(1, 1, 1)

time = data['t (s)']
Tilt_up_value = data['Tilt up/down (deg)']
Tilt_left_value = data['Tilt left/right (deg)']

ax.plot(time, Tilt_up_value, label='Tilt up/down (deg)', marker='o')
ax.plot(time, Tilt_left_value, label='Tilt left/right (deg)', marker='o')

ax.set_title('Flat Graph', fontsize=20)

ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)

ax.legend(fontsize=12, loc='best')

plt.show()
