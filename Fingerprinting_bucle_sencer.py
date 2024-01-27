import pandas as pd
import math

#En aquest arxiu, es recorren tots els vectors de test i es comparen amb tots els vectors d'entrenament obtenint una distància mitjana d'error. Per això es diu bucle sencer.
#A mode d'exemple, s'usa la primera estratègia, substituir els valors de 100 per 0.

#S'usa la base de dades MAN2 degut a que és més petita que la MAN1 (menys temps per calcular la distància mitjana total) i conté menys nombre de valors no vàlids (100).

#Llegeix l'arxiu MAN2 entrenament rss i ho guarda en una variable estil dataframe. Header=none vol dir que no hi ha capsalera, son les dades directament
MAN1_trnrss = 'MAN2_trnrss.csv'
data_frame_entrenament = pd.read_csv(MAN1_trnrss, header=None)

# Llegeix l'arxiu MAN2 entrenament coordenades i ho guarda en una variable estil dataframe. Header=none vol dir que no hi ha capsalera, son les dades directament
MAN1_trncrd = 'MAN2_trncrd.csv'
data_frame_entrenament_coordenades = pd.read_csv(MAN1_trncrd, header=None)


#llegeix la primera fila de l'arxiu MAN2 tests rss i ho guarda en una variable tipus data frame
MAN1_tstrss = 'MAN2_tstrss.csv'
data_frame_tests_rss = pd.read_csv(MAN1_tstrss, header=None)

#llegeix la primera fila de l'arxiu MAN2 tests rss i ho guarda en una variable tipus data frame
MAN1_tstcrd = 'MAN2_tstcrd.csv'
data_frame_tests_crd = pd.read_csv(MAN1_tstcrd, header=None)


#posicio_test=455
#primera_fila_tests = data_frame_tests_rss.iloc[posicio_test]

# Obtenir el número de filas que té la base de dades d'entrenament
num_filas = data_frame_entrenament.shape[0]


#Obtenir el número de columnes que té la base de dades d'entrenament
num_columnes = data_frame_entrenament.shape[1]


array_numero_posicions_entrenament_suma = [0] * num_filas

# Es guarda el número de filas que té la base de dades de tests
num_filas_test = data_frame_tests_rss.shape[0]
array_distancies_absolutes = [0] * num_filas_test

# En el següent bucle es recorren tots els test i es compara cada vector de test amb tots els d'entrenament.
# En aquest cas s'usa la primera estratègia. Substituir els valors de 100 per 0.

for k in range(num_filas_test):
    posicio_test=k
    primera_fila_tests = data_frame_tests_rss.iloc[posicio_test]

    #Es recorre tot els vectors d'entrenament i es compara amb el vector de test determinat
    for i in range(num_filas) :
            diferencia_intensitat_suma = 0
            
            #Dins de cada vector d'entrenament es busca la diferència per obtenir la diferència d'intensitat
            #Si algun valor, tant el vector d'entrenament com el de test és 100, la diferencia s'estableix a 0. És com si no es tingués en compte.
            for j in range(num_columnes):
                intensitat = data_frame_entrenament.iloc[i][j]
                
                diferencia_intensitat = abs(primera_fila_tests[j]-intensitat)
                if primera_fila_tests[j] == 100 or data_frame_entrenament.iloc[i][j] == 100:
                    diferencia_intensitat = 0
                    
                   
                diferencia_intensitat_suma = diferencia_intensitat_suma + diferencia_intensitat

            
            #Aqui es guarda en un array del tamany de les files totes les diferents intensitats
            array_numero_posicions_entrenament_suma[i] = diferencia_intensitat_suma
                
    #Es tria el valor mínim o la distancia mínima entre tots els vectors d'entrenament. El que tingui la menor distància és el vector d'entrenament més semblant.
    valor_minim = min(array_numero_posicions_entrenament_suma)
    print("La posició de test és " + str(posicio_test)) 
    print("El valor mínim d'entrenament (distancia entre vectors) és" + " " + str(valor_minim))


    #A continuació es poden usar tres formes diferents de seleccionar el vector en el cas que el valor mínim sigui el mateix.
    # En aquest codi s'opta per triar només el primer vector d'aquesta llista. Si es vol probar les altres formes només cal descomentar-les.
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
    print ("La distancia entre els dos vectors és "+str(distancia))

    print ("-------------------------------------")

    #Es guarda en un array totes les distancies per després poder calcular la distància d'error mitjana
    array_distancies_absolutes[k]=distancia

#Un cop s'ha acabat de recórrer tots els vectors de test amb tots els d'entrenament, es calcula la distància d'error mitjana.    
distancia_acumulada=0
for d in range(num_filas_test):
    distancia_acumulada=distancia_acumulada+array_distancies_absolutes[d]

distancia_mitjana=distancia_acumulada/num_filas_test

print("La distancia mitjana és, "+ str(distancia_mitjana))


#Com s'ha dit anteriorment, a partir d'aquí es pot descomentar el següent codi per provar diferents estratègies en el cas de que hi hagi diferents vectors que tinguin el valor mínim.
'''
#--------------------------------------------------------------

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

print("---------------------------------------------------------------------------------")

#S'ha de tenir en compte en el resultat que al google drive és una posició més
print("La posició d'entrenament amb més posicions correctes és (TERCER)" + " "+ str(posicio_amb_mes_correctes))

print("Valors coordenades finals (TERCER)"+" "+ str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][0]) + ", " + str(data_frame_entrenament_coordenades.iloc[posicio_amb_mes_correctes][1]))

print("Les coordenades reals (test) son"+" "+ str(data_frame_tests_crd.iloc[posicio_test][0]) + ", " + str(data_frame_tests_crd.iloc[posicio_test][1]))
'''
 







