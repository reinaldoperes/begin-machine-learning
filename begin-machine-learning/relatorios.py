import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


df = pd.read_csv("restaurantes_favoritos.csv")

X = np.array(df)

sb.pairplot(df)

##plt.axis('equal')
plt.show()