import pandas as pd
import math

#En aquest arxiu es mostra la comparació de només un vector de test amb tots els d'entrenament. S'usa la millor estratègia (substitució dels valors nuls (100) per el valor mínim (-100)).

#Llegeix l'arxiu MAN2 entrenament rss i ho guarda en una variable estil dataframe. Header=none vol dir que no hi ha capsalera, son les dades directament
MAN2_trnrss = 'MAN2_trnrss.csv'
data_frame_entrenament = pd.read_csv(MAN2_trnrss, header=None)

#Llegeix l'arxiu MAN2 entrenament coordenades i ho guarda en una variable estil dataframe. Header=none vol dir que no hi ha capsalera, son les dades directament
MAN2_trncrd = 'MAN2_trncrd.csv'
data_frame_entrenament_coordenades = pd.read_csv(MAN2_trncrd, header=None)


#llegeix la primera fila de l'arxiu MAN2 tests rss i ho guarda en una variable tipus data frame
MAN2_tstrss = 'MAN2_tstrss.csv'
data_frame_tests_rss = pd.read_csv(MAN2_tstrss, header=None)

#llegeix la primera fila de l'arxiu MAN2 tests rss i ho guarda en una variable tipus data frame
MAN2_tstcrd = 'MAN2_tstcrd.csv'
data_frame_tests_crd = pd.read_csv(MAN2_tstcrd, header=None)

#Per provar guardo la primera fila del tests 
#primera_fila_tests_p = [-53,-59,-80,-60,-74,100,-71,-80,-88,100,-92,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,-90]
#primera_fila_tests_t = [-88,-89,-83,-82,100,100,100,100,-49,100,100,-72,-52,100,-80,-64,-84,100,100,-70,100,-95,100,100,100,100,100,100]

num_filas_test = data_frame_tests_rss.shape[0]
array_distancies_absolutes = [0] * num_filas_test

#Es prova la posició de test número 425. Canviant aquesta variable es poden provar els diferents vectors de test. 
posicio_test=425
primera_fila_tests = data_frame_tests_rss.iloc[posicio_test]

# Obtenir el número de filas que té la base de dades d'entrenament
num_filas = data_frame_entrenament.shape[0]


#Obtenir el número de columnes que té la base de dades d'entrenament
num_columnes = data_frame_entrenament.shape[1]


array_numero_posicions_entrenament_suma = [0] * num_filas

#La següent variable (factor) és el valor de prendran els valors nuls (100). S'usa la segona estratègia, substituir pel valor més petit de la base de dades (-100).
factor = -100

#En el següent bucle es recorren tots els vectors d'entrenament amb la posició de test establerta anteriorment.
for i in range(num_filas) :

        diferencia_intensitat_suma = 0
        
        for j in range(num_columnes):
            intensitat_entrenament = data_frame_entrenament.iloc[i][j]
            intensitat_test = primera_fila_tests[j]

            #Es substitueix per -100 en el cas que sigui un valor nul.
            if intensitat_entrenament==100:
                intensitat_entrenament=factor
            
            if intensitat_test==100:
                intensitat_test=factor
                            
            #Es calcula la diferència entre la columna corresponent dels dos vectors.
            diferencia_intensitat = abs(intensitat_test-intensitat_entrenament)
                
            #S'acumula les diferents diferències que hi ha en totes les columnes. Aquesta suma de diferències total per al vector determinat s'usa després per veure quin dels vectors té menys distància.
            diferencia_intensitat_suma = diferencia_intensitat_suma + diferencia_intensitat
            

        
        #Aqui es guarda en un array del tamany de les files d'entrenament totes les distàncies dels diferents vectors d'entrenament amb el de test.
        array_numero_posicions_entrenament_suma[i] = diferencia_intensitat_suma

'''
#Bucle per veure la intensitat mínima entre totes
intensitat_mes_petita=10000000
for i in range(num_filas) :
        if array_numero_posicions_entrenament_suma[i]< intensitat_mes_petita: 
            intensitat_mes_petita = array_numero_posicions_entrenament_suma[i]


print("La intensitat més petita és",+ intensitat_mes_petita)
'''


#Es tria el valor mínim o la distancia mínima entre tots els vectors d'entrenament. El que tingui la menor distància és el vector d'entrenament més semblant.
valor_minim = min(array_numero_posicions_entrenament_suma)
print("La posició de test és " + str(posicio_test))
print("El valor mínim d'entrenament (distància entre vectors) és" + " " + str(valor_minim))


#A continuació es poden usar tres formes diferents de seleccionar el vector en el cas que el valor mínim sigui el mateix.
#En aquest codi s'opta per triar només el primer vector d'aquesta llista. Si es vol probar les altres formes només cal descomentar-les.
#--------------------------------------------------------------

#CAS_1: Es busca la primera posició que conté el valor mínim

for i in range(num_filas) :
    
    if array_numero_posicions_entrenament_suma[i] == valor_minim:

        posicio_amb_mes_correctes=i
        break

print("La posició d'entrenament amb més posicions correctes és (PRIMER)" + " "+ str(posicio_amb_mes_correctes))

#Es printen les coordenades del vector d'entrenament seleccionat
print("Valors coordenades finals (PRIMER)"+" "+ str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][0]) + ", " + str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][1]))

#Es printen les coordenades que haurien de ser. Són les associades al vector de test usat.
print("Les coordenades reals (test) son"+" "+ str(data_frame_tests_crd.iloc[posicio_test][0]) + ", " + str(data_frame_tests_crd.iloc[posicio_test][1]))

#Es calcula i es printa la distància entre les dues coordenades. És a dir, l'error de posicionament.
distancia = math.sqrt((data_frame_tests_crd.iloc[posicio_test][0] - data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][0])**2 + (data_frame_tests_crd.iloc[posicio_test][1] - data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][1])**2)
print ("La distància absoluta entre les dues coordenades és, " + str(distancia))

print("----------------------------------------------------------------------")


#--------------------------------------------------------------
'''
#CAS_2: Es busca la última posició que conté el valor mínim

for i in range(num_filas) :
    
    if array_numero_posicions_entrenament_suma[i] == valor_minim:

        posicio_amb_mes_correctes=i

print("---------------------------------------------------------------------------------")
        
print("La posició d'entrenament amb més posicions correctes és (SEGON)" + " "+ str(posicio_amb_mes_correctes))

print("Valors coordenades finals (SEGON)"+" "+ str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][0]) + ", " + str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][1]))

print("Les coordenades reals (test) son"+" "+ str(data_frame_tests_crd.iloc[posicio_test][0]) + ", " + str(data_frame_tests_crd.iloc[posicio_test][1]))

        
#---------------------------------------------------------------

#CAS_3: Es busca quina posició que conté el valor mínim té més posicions vàlides (diferents de 100)

numero_posicions_correctes_1 = 0
numero_posicions_correctes_2 = 0
posicio_amb_mes_correctes = 0


for i in range(num_filas) :
    
    if array_numero_posicions_entrenament_suma[i] == valor_minim:
        
        #print(i)
        
        #posicio_amb_mes_correctes=i
        
        for j in range(num_columnes) :
            if data_frame_entrenament.iloc[i][j] != 100 :
                numero_posicions_correctes_1 = numero_posicions_correctes_1 + 1
        
        #print(numero_posicions_correctes_1)
        if numero_posicions_correctes_1 > numero_posicions_correctes_2:
            numero_posicions_correctes_2 = numero_posicions_correctes_1
            posicio_amb_mes_correctes = i
        numero_posicions_correctes_1=0

#------------------------------------------------------------------

'''
#Es pot usar el següent codi per fer un bucle sencer on s'usin tots els vectors de test. En el fitxer Fingerprinting_bucle_sencer.py ja es fa això.
'''
print("----------------------------------------------------------------------")

#S'ha de tenir en compte en el resultat que al google drive és una posició més
print("La posició d'entrenament amb més posicions correctes és" + " "+ str(posicio_amb_mes_correctes))

print("Valors coordenades finals estimades"+" "+ str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][0]) + ", " + str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][1]))

print("Les coordenades reals (test) són"+" "+ str(data_frame_tests_crd.iloc[posicio_test][0]) + ", " + str(data_frame_tests_crd.iloc[posicio_test][1]))

distancia = math.sqrt((data_frame_tests_crd.iloc[posicio_test][0] - data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][0])**2 + (data_frame_tests_crd.iloc[posicio_test][1] - data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][1])**2)


print ("La distància absoluta entre les dues coordenades és, " + str(distancia))

#array_distancies_absolutes[k]=distancia

distancia_acumulada=0
for d in range(num_filas_test):
     distancia_acumulada=distancia_acumulada+array_distancies_absolutes[d]


distancia_mitjana=distancia_acumulada/num_filas_test

print("----------------------------------------------------------------------")

print("La distancia mitjana és, "+ str(distancia_mitjana))
'''
  



                

