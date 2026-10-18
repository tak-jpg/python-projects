import numpy as np 

liste = [1,2,3,4,5]

tab = np.array(liste)

print(tab*2)
print(tab.mean())
print(tab[tab > 2])