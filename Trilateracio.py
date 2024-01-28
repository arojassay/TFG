import numpy as np
from scipy.optimize import minimize
import math
import pandas as pd
import matplotlib.pyplot as plt


#Funció que calcula la posició en base a un vector amb les posicions dels routers i un altre vector amb les distàncies entre els routers i l'usuari.
def multilaterate(routers, distances):
    def objective_function(coordinates):
        error = 0
        for router, distance in zip(routers, distances):
            error += (np.linalg.norm(coordinates - router) - distance)**2
        return error

    initial_guess = np.zeros(2)

    # Optimització per trobar les coordenades que minimitzen l'error
    result = minimize(objective_function, initial_guess, method='L-BFGS-B')

    if result.success:
        return result.x
    else:
        raise ValueError("No s'ha pogut trobar la posició.")


#Funció que calcula la distància en funció de la potència i el número del router en concret. Cada router té un model de regressió diferent calculat en l'altre arxiu.
def calcular_distancia(RSSI, numero_router):
    # Defineixo una equació per cada router calculada amb el model de regressió
    if(numero_router==0):
        distancia = -0.81733 * RSSI + -29.44215
    if(numero_router==2):
        distancia = -0.25270 * RSSI + -3.23676
    if(numero_router==3):
        distancia = -0.76240 * RSSI + -33.12207
    if(numero_router==5):
        distancia = -0.32829 * RSSI + -13.08652
    if(numero_router==7):
        distancia = -0.52139 * RSSI + -20.94488
    if(numero_router==8):
        distancia = -0.57345 * RSSI + -22.58972
    if(numero_router==14):
        distancia = -0.44367 * RSSI + -16.95539
    if(numero_router==15):
        distancia = -0.22670 * RSSI + -3.34618
    if(numero_router==16):
        distancia = -0.84172 * RSSI + -44.75840
    if(numero_router==24):
        distancia = -0.78633 * RSSI + -45.57907

    return distancia

#llegeix la primera fila de l'arxiu MAN1 tests rss i ho guarda en una variable tipus data frame
MAN1_tstrss = 'MAN1_tstrss.csv'
data_frame_tests_rss = pd.read_csv(MAN1_tstrss, header=None)

#llegeix la primera fila de l'arxiu MAN1 tests rss i ho guarda en una variable tipus data frame
MAN1_tstcrd = 'MAN1_tstcrd.csv'
data_frame_tests_crd = pd.read_csv(MAN1_tstcrd, header=None)

#Aqui es pot provar amb els diferents vectors de test.
vector=300


#fila_tests = data_frame_tests_rss.iloc[vector]


#fila_tests=[-53,-59,-80,-60,-74,100,-71,-80,-88,100,-92,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,-90]


num_filas_test = data_frame_tests_rss.shape[0]
num_columnes_test = data_frame_tests_rss.shape[1]
array_distancies_absolutes = [0] * num_filas_test


#Aqui es guarden les diferents intensitats del vector de test seleccionat anteriorment. És a dir, tota la fila.
fila_tests = data_frame_tests_rss.iloc[vector]
numero_posicions_valides=0

#Aqui es busca quants routers valids existeixen en aquest vector ja que no es disposa de tota la informació de tots els routers, sino només de 10.
for s in range(num_columnes_test):
    if fila_tests[s] != 100 and s in [0, 2, 3, 5, 7, 8, 14, 15, 16, 24]:
        numero_posicions_valides=numero_posicions_valides+1

print ("El número de WAP's a utilitzar és " +str(numero_posicions_valides))


#Es crea el vector de distàncies amb el numero de posicions vàlides
array_distancies=[0] * numero_posicions_valides


posicio=0
array_posicions_routers=[0]* numero_posicions_valides

array_intensitat_routers_valids=[0]* numero_posicions_valides

#Es recorre les columnes del vector determinat, si el valor no és nul i és un dels disponibles es calcula la distància a partir d'una intensitat i del router que sigui.
for i in range(num_columnes_test):
    if fila_tests[i] != 100 and i in [0, 2, 3, 5, 7, 8, 14, 15, 16, 24]:
        #fila_tests[i] és la intensitat d'una columna. i és el número de router.
        distancia_calculada = calcular_distancia(fila_tests[i],i)
        #Es guarda la distància en un array per després utilitzar-lo.
        array_distancies[posicio]=distancia_calculada
        #Es guarda el número de router en un array per després utilitzar-lo.
        array_posicions_routers[posicio]=i
        array_intensitat_routers_valids[posicio]=fila_tests[i]
        posicio=posicio+1



#Coordenades de tots els routers presents en l'espai (10).
routers = [(-23.626,-18.596), (-4, 3), (8.538,-9.298), (-10.702,-18.596), (9, -9), (-1.93,-2.749), (3, -5), (8.596,-14.62), (7.135,6.023), (8, -3), (4, 4), (2, 2), (5, 1), (7, 7), (21.17,-2.69), (13.333,-2.69), (32.398,-2.69), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (32.573,13.86), (9, -9), (9, -9), (9, -9)]

print(array_posicions_routers)

#Es guarda en aquest array les coordenades dels routers disponibles per al vector en concret.
llista_coordenades_routers = [routers[i] for i in array_posicions_routers]

print(llista_coordenades_routers)

print(array_intensitat_routers_valids)

print(array_distancies)

#Es crida a la funció multilaterate, se li passen les coordenades dels routers i les distàncies dels routers a la coordenada que es vol trobar.
#Retorna la coordenada resultant.
posicio = multilaterate(llista_coordenades_routers, array_distancies)

print(f"La teva posició estimada és: {posicio}")

print("--------------------------------")


#----------------------------------------------------------------------------- A parti d'aquí es crea el gràfic -----------------------------------------------

#Es guarda la informació de les coordenades dels routers dividida en dos. El primer (latituds) i el segon valor (longituds).
latituds, longituds = zip(*llista_coordenades_routers)

#Es crea el gràfic de dispersió amb cercles corresponents als routers disponibles per el vector determinat.
plt.scatter(latituds, longituds, color='blue', marker='o', s=10)

#Es creen els cercles de color vermell amb el vector de distàncies.
for i, (lat, lon) in enumerate(llista_coordenades_routers):
    radi = array_distancies[i]
    cercle = plt.Circle((lat, lon), radius=radi, color='red', alpha=0.5)
    plt.gca().add_patch(cercle)

#Afegeix un punt de color taronja (resultat de la multilateració)
taronja_lat, taronja_lon = posicio
plt.scatter(taronja_lat, taronja_lon, color='orange', marker='o')


#Pinta un punt verd amb la posició real
verd_lat = data_frame_tests_crd.iloc[vector][0]
verd_lon = data_frame_tests_crd.iloc[vector][1]
plt.scatter(verd_lat, verd_lon, color='green', marker='o')
print("La posició real és " + str(data_frame_tests_crd.iloc[vector][0]) + " , " + str(data_frame_tests_crd.iloc[vector][1]))


#Etiquetes i títol del gràfic
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Representació trilateració')

#Assegurar que els cercles es vegin com cercles i que els eixos tinguin la mateixa escala.
plt.axis('equal')
plt.tight_layout()

#Mostrar la llegenda
plt.legend()

#Mostrar el gràfic
plt.grid(True)
plt.show()

