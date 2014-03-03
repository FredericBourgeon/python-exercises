"""
Data statistics
"""

import numpy as np

data = np.loadtxt('populations.txt')
year, hares, lynxes, carrots = data.T
populations = data[:, 1:]

# Mean and std of the population over the 20-year period
means = populations.mean(axis=0)
stds = populations.std(axis=0)

print 'Mean values:', means
print 'Standard deviations:', stds
print '\n'

# Which year a each species as the largest population

filter_1 = populations.argsort(axis=0)[0, :]
print 'Max pop. reached year for:'
print 'Hares', 'Lynxes', 'Carrots'
print year[filter_1]
print '\n'

# Which species has the largest population each year

max_species = populations.argsort(axis=1)[:, -1]
print 'Max pop. each year'
print np.array(['Hares', 'Lynxes', 'Carrots'])[max_species[:, np.newaxis]]
print '\n'

# Which year any population goes above 50000

above_50000 = populations > 50000
print 'Any pop. > 50000 on year(s):'
print year[above_50000.any(axis=1)]
print '\n'

# Top 2 years of lowest populations for each species

lower_2 = populations.argsort(axis=0)[:2]
print 'Two lowest pop. years for each species'
print year[lower_2]
print '\n'

# Compare change in hare population and to population of lynxes

hare_grad = np.gradient(hares)
print "(Hares) vs. Lynxes correlation", np.corrcoef(hare_grad, lynxes)[0, 1]

import matplotlib.pyplot as plt
plt.axes([0.1, 0.1, 0.6, 0.8])
plt.plot(year, hare_grad, label='Hare gradient')
plt.plot(year, lynxes, label='Lynx pop.')
plt.legend(('Hare gradient', 'Lynx pop.'), loc=(1.05, 0.5))
plt.show()
