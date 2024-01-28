import pandas as pd
import math

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# Llegeix l'arxiu MAN1 entrenament rss i ho guarda en una variable estil dataframe. Header=none vol dir que no hi ha capsalera, son les dades directament
MAN1_trnrss = 'MAN1_trnrss.csv'
data_frame_entrenament = pd.read_csv(MAN1_trnrss, header=None)

# Llegeix l'arxiu MAN1 entrenament coordenades i ho guarda en una variable estil dataframe. Header=none vol dir que no hi ha capsalera, son les dades directament
MAN1_trncrd = 'MAN1_trncrd.csv'
data_frame_entrenament_coordenades = pd.read_csv(MAN1_trncrd, header=None)


#Es guarden el número de files del fitxer d'entrenament
num_filas = data_frame_entrenament.shape[0]

#Es guarden el número de columnes del fitxer d'entrenament
num_columnes = data_frame_entrenament.shape[1]

#Serà un vector amb totes les intensitats d'un AP en concret
array_intensitats_AP_1 = [0] * num_filas

#Serà un vector amb totes les distàncies reals corresponents a cada intensitat d'un AP en concret
array_distancies_AP_1 = [0] * num_filas


#Es poden comentar o descomentar el següent codi en funció de triar un WAP o altre. Per defecte està descomentat l'últim WAP, el número 25.
#El que es fa és obtenir un array amb totes les intensitats del WAP en questió i també un altre array amb la distància real associada a cada intensitat.
'''
#Router número 1
#Coordenades AP1
coordenades_AP1=[-23.626,-18.596]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][0]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)


#Router número 3
#Coordenades AP1
coordenades_AP1=[8.538,-9.298]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][2]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)


#Router número 4
#Coordenades AP1
coordenades_AP1=[-10.702,-18.596]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][3]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)

#Router número 6
#Coordenades AP1
coordenades_AP1=[-1.93,-2.749]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][5]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)

#Router número 8
#Coordenades AP1
coordenades_AP1=[8.596,-14.62]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][7]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)

#Router número 9
#Coordenades AP1
coordenades_AP1=[7.135,6.023]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][8]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)

#Router número 15
#Coordenades AP1
coordenades_AP1=[21.17,-2.69]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][14]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)

#Router número 16
#Coordenades AP1
coordenades_AP1=[13.333,-2.69]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][15]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)

#Router número 17
#Coordenades AP1
coordenades_AP1=[32.398,-2.69]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][16]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)
'''
#Router número 25
#Coordenades AP1
coordenades_AP1=[32.573,13.86]

for i in range(num_filas):
        array_intensitats_AP_1[i]=data_frame_entrenament.iloc[i][24]
        array_distancies_AP_1[i]= math.sqrt((coordenades_AP1[0] - data_frame_entrenament_coordenades.iloc[i][0])**2 + (coordenades_AP1[1] - data_frame_entrenament_coordenades.iloc[i][1])**2)


#A partir d'aquí es calcula la recta resultant d'aquest model de regressió que s'usarà en el fitxer principal de la multilateració per calcular la distància.

#Dades d'entrada
intensitats = np.array(array_intensitats_AP_1)
distancies = np.array(array_distancies_AP_1)

#S'exclouen els valors nuls (100).
indexs_no_nuls = intensitats != 100
intensitats = intensitats[indexs_no_nuls]
distancies = distancies[indexs_no_nuls]

#Divisió de les dades en entrenament i prova.
X_train, X_test, y_train, y_test = train_test_split(intensitats.reshape(-1, 1), distancies, test_size=0.2, random_state=42)

#Creació i entrenament del model de regressió lineal
model = LinearRegression()
model.fit(X_train, y_train)
pendent = model.coef_[0]
ordenada_al_origen = model.intercept_

#Ecuació del model. És la que es farà servir per calcular la distància.
ecuacio_model = f"Distància = {pendent:.5f} * RSSI + {ordenada_al_origen:.5f}"
print(ecuacio_model)


prediccions = model.predict(X_test)

#Càlcul de l'error cuadràtic mig
mse = mean_squared_error(y_test, prediccions)
print(f"Error cuadràtic mig (MSE): {mse}")


#Visualització dels resultats en un gràfic
plt.scatter(X_test, y_test, color='black', label='Dades reals')
plt.plot(X_test, prediccions, color='blue', linewidth=3, label='Prediccions')
plt.xlabel('Intensitat RSSI')
plt.ylabel('Distància Real')
plt.legend()
plt.show()


