import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import altair as alt
import pandas as pd

df = pd.read_csv('indicadores-mundiales.csv', sep=',', encoding='latin-1')
data = df.groupby('Region').sum()[['Poblacion 0-14', 'Poblacion 15-64', 'Poblacion 65+']]
bars1 = list(data['Poblacion 0-14'])
bars2 = list(data['Poblacion 15-64'])
bars3 = list(data['Poblacion 65+'])
barWidth = 0.25

"First graph"

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, bars1, color='#001dff', width=barWidth, edgecolor='white', label='Poblacion 0-14')
plt.bar(r2, bars2, color='#ff6a00', width=barWidth, edgecolor='white', label='Poblacion 15-64')
plt.bar(r3, bars3, color='#26c143', width=barWidth, edgecolor='white', label='Poblacion 65+')
 
plt.xlabel('Indicators', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Asia', 'Europa', 'Las Americas', 'Oceania', 'Oriente medio', 'Africa'])
plt.legend()
plt.savefig('images_tarea/first_graph.png')
plt.show()



"Second graph"

r1 = np.arange(len(bars1))
fig, (ax, ax_1, ax_2) = plt.subplots(3,1)
ax.bar(r1, bars1, color='#001dff', width=barWidth, edgecolor='white', label='Poblacion 0-14')
ax.set_xticklabels([])
ax.legend()
ax_1.bar(r1, bars2, color='#ff6a00', width=barWidth, edgecolor='white', label='Poblacion 15-64')
ax_1.set_xticklabels([])
ax_1.legend()
ax_2.bar(r1, bars3, color='#26c143', width=barWidth, edgecolor='white', label='Poblacion 65+')
ax_2.legend()
ax_2.set_xticklabels(['','Asia','Europa', 'Las Americas', 'Oceania', 'Oriente medio', 'Africa'])
plt.savefig('images_tarea/second_graph.png')
plt.show()

"Third graph"

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))
values = df['Gasto en salud (per capita)'].fillna(0)
years = list(df['Ano'])

for i in range(len(years)):
    years[i] = years[i][:4]


new_data = [years, values]
new_data = zip(*[i for i in new_data])
df = pd.DataFrame(data=new_data, columns=['year', 'per capita'])
df = df.groupby('year')
data = []
for i in list(df['per capita']):
    data.append(list(i[1]))

# generate some random test data
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]


# plot box plot
axes.boxplot(data, 0 ,'gD')
axes.set_title('Año de Ano')
axes.grid(True)
plt.ylabel('Prom gasto en salud (per capita)')

# adding horizontal grid lines


# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(data))],
         xticklabels=['2000', '2001', '2002', '2003', '2004'])

fig.savefig('images_tarea/third_graph.png')



"""Fourth Graph"""
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(9, 4))
data = [bars1, bars2, bars3]
data = list(zip(*[i for i in data]))

axes[0][0].plot(data[0], 'ro')
axes[0][0].set_title('Asia')
axes[0][0].grid(True)

axes[0][1].plot(data[1], 'ro')
axes[0][1].set_title('Europa')
axes[0][1].grid(True)

axes[0][2].plot(data[2], 'ro')
axes[0][2].set_title('Las Americas')
axes[0][2].grid(True)

axes[1][0].plot(data[3], 'ro')
axes[1][0].set_title('Oceania')
axes[1][0].grid(True)

axes[1][1].plot(data[4], 'ro')
axes[1][1].set_title('Oriente medio')
axes[1][1].grid(True)

axes[1][2].plot(data[5], 'ro')
axes[1][2].set_title('Africa')
axes[1][2].grid(True)

fig.savefig('images_tarea/fourth_graph.png')

fig.suptitle('0.0 -- Poblacion 0-14 \n1.0 -- Poblacion 15-64 \n2.0 -- Poblacion 65+', fontsize=7)
plt.show()

