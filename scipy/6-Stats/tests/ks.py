from scipy import stats
import numpy as np

np.random.seed(15)
# Générer deux ensembles de données à partir d'une distribution normale
data1 = stats.norm.rvs( size=100)
data2 = stats.norm.rvs(size=100)
print(data1)

print(data2)
# Effectuer un test de Kolmogorov-Smirnov pour comparer les deux ensembles de données
statistic, p_value = stats.ks_2samp(data1, data2)

# Afficher les résultats du test
print("Statistique du test de Kolmogorov-Smirnov:", statistic)
print("Valeur-P du test de Kolmogorov-Smirnov:", p_value)
