import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Funció que se li passen les diferents coordenades i les pinta en la imatge corresponent a la base de dades (Mannheim)
def dibuixar_mapa(coordenades_real, coordenades_estimades_fingerprinting, coordenades_estimades_trilateracio, ruta_imatge, dimensions_imatge):
    #Desempaqueta les coordenades
    x, y = coordenades_real

    z, k = coordenades_estimades_fingerprinting

    t, w = coordenades_estimades_trilateracio

    print(x)
    #Carrega la imatge de fons
    mapa = mpimg.imread(ruta_imatge)

    #Converteix els metres en píxels per a poder-ho representar en aquesta imatge
    #Tot i que les divisions son diferents però és la mateixa relació píxels metre. 10.5117 píxels per metre.
    x = (x * (583.4/55.5))-47.6 #El valor de -47.6 se li resta ja que l'eix de coordenades no coincideix amb el 0 de la imatge.
    y = (y * (323.4/30.75))+27.9 #Aquí el mateix però amb l'eix Y

    z = (z * (583.4/55.5))-47.6
    k = (k * (323.4/30.75))+27.9

    t = (t * (583.4/55.5))-47.6
    w = (w * (323.4/30.75))+27.9

    #Crea la figura i els eixos
    fig, ax = plt.subplots()

    #Mostra la imatge de fons ocupant tot l'espai
    ax.imshow(mapa, extent=[-dimensions_imatge[0]/2, dimensions_imatge[0]/2, -dimensions_imatge[1]/2, dimensions_imatge[1]/2], origin='upper')

    #Configura els límits dels eixos per a que coincideixin amb les dimensions de la imatge
    ax.set_xlim([-dimensions_imatge[0]/2, dimensions_imatge[0]/2])
    ax.set_ylim([-dimensions_imatge[1]/2, dimensions_imatge[1]/2])

    #Oculta els números als eixos X i Y.
    ax.set_xticks([])
    ax.set_yticks([])


    ax.plot(x, y, 'o', markersize=12, markerfacecolor='none', markeredgecolor='orange')
    ax.plot(z, k, 'o', markersize=12, markerfacecolor='none', markeredgecolor='blue')
    ax.plot(t, w, 'rx', markersize=12)


    #Etiqueta els eixos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    #Mostra el mapa
    plt.show()

#Aqui es poden modificar les diferents coordenades de les dues tècniques per pintar-les al mapa.
coordenades_real = (32.16, 7.08)  
coordenades_estimades_fingerprinting = (32.0, 5.0)
coordenades_estimades_trilateracio = (27.35796432, 5.22098447)
#Ruta de la imatge
ruta_imatge = 'floorplan-fingerprint.png'
#Dimensions de la imatge del mapa (Mannheim)
dimensions_imatge = (694, 422) 
dibuixar_mapa(coordenades_real, coordenades_estimades_fingerprinting, coordenades_estimades_trilateracio, ruta_imatge, dimensions_imatge)

