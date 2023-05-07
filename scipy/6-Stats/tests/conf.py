import numpy as np
import scipy.stats as stats

# Générer un échantillon de données
sample = np.array([10, 12, 13, 15, 14, 16, 11, 13, 15, 12])

# Calculer la moyenne et l'écart type de l'échantillon
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

#confidence interval
n = len(sample)
alpha = 0.05
t_value = stats.t.ppf(1-alpha/2, n-1)
ci = stats.t.interval(alpha, df=n-1, loc=sample_mean, scale=sample_std/np.sqrt(n))

# Afficher les résultats
print("Moyenne de l'échantillon:", sample_mean)
print("Ecart-type de l'échantillon:", sample_std)
print("Intervalle de confiance pour la moyenne:", ci)


import numpy as np
from scipy import stats

# Générer un échantillon de 100 observations avec une moyenne de 5 et un écart-type de 2
np.random.seed(1234)
sample = np.random.normal(5, 2, 100)

# Calcul de l'intervalle de confiance à 95%
# Calcul du degré de liberté : n - 1
df = len(sample) - 1
# Calcul de la moyenne et de l'erreur standard
mean = np.mean(sample)
sem = stats.sem(sample)
# Calcul de l'intervalle de confiance
ci = stats.t.interval(0.95, df, loc=mean, scale=sem)

print("Moyenne de l'échantillon:", mean)
print("Intervalle de confiance à 95%:", ci)
