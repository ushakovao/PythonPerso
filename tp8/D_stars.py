import imageio
import  matplotlib.pyplot as plt
import numpy as np



from tp8.C_zone import add_neighbours_in_stack




"""voir l'effet d'un seuillage sur les étoiles"""
def step0():
    img = imageio.imread("../assets/img/chess.png")
    image = img[:, :, 0]
    print(image.shape)

    thresholded=np.zeros(image.shape)
    thresholded[image>240]=255

    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.imshow(thresholded,cmap="gray")

    plt.show()

"""la même fonction que précédemment, mais qui renvoie en plus le barycentre
et le nombre de pixel de la composante connexe (=tache blanche)"""
def connected_component_baryCenter(image:np.ndarray, seuil:int, i0:int, j0:int, inComponent:np.ndarray)->tuple:
    stack = [(i0,j0)]
    bary_i=0
    bary_j=0
    nb=0
    while len(stack)>0:
        """ pop() est une méthode qui renvoie le dernier élément d'une liste, tout en le supprimant de la liste"""
        (i,j) = stack.pop()
        bary_i+=i
        bary_j+=j
        nb+=1
        add_neighbours_in_stack(image, seuil, stack, i, j, inComponent)

    return bary_i/nb,bary_j/nb,nb


def all_connected_components(image:np.ndarray, seuil:int)->list:

    inComponent = np.empty(image.shape, dtype=np.bool)
    inComponent[:, :] = False

    baryAndSizes=[]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j]>seuil and not inComponent[i,j]:
                baryAndSizes.append( connected_component_baryCenter(image,seuil,i,j,inComponent))

    return baryAndSizes



""" apprenons à superposer une image et un scatter plot  """
def step1():

    img = imageio.imread("../assets/img/cosmos_petit.jpg")
    image =  img[:, :, 0]*0.9 #type:np.ndarray



    """Attention bizarrerie : le fait d'appeler imshow  va déterminer le système des coordonnée avec l'origine
      en haut à gauche !  Le scatter   reste alors dans ce même système de coordonnée. Essayez un scatter tout seul,
      vous verrez, l'origine est alors en bas.

       Encore plus bizarre : si on rajoute l'option extent= ... (qui précise les bornes) ,
        l'origine repasse en bas pour le scatter, mais pas pour le imshow.

       Si une jour vous croisez les créateurs de matplotlib ..."""


    plt.imshow(image,
               #aspect='auto',# avec aspect='auto' le repére n'est plus orthonormé
               #extent=[0,image.shape[1],0,image.shape[0]], #pour préciser les bornes
               cmap='gray',
               norm=plt.Normalize(vmin=0, vmax=255)
               )
    sx=img.shape[0]//10*10;
    sy = img.shape[1] // 10 * 10;
    xs=np.arange(0, sx,sx/10 )
    ys=np.arange(0,  sy,sy/10 )



    plt.scatter(
        xs,#abscisse
        ys,#ordonnées
        marker='o', #forme
        s=np.arange(0, 100, 10),#rayon

        c=np.arange(0, 100, 10),  # valeur numérique pour la couleur
        #cmap='gray', #color map
        norm=plt.Normalize(vmin=0, vmax=100) #l'echelle des couleurs va de 0 à 100
    )

    labels=[]
    for i in range(len(xs)):
        labels.append(str(i))


    for label, x, y in zip(labels, xs, ys):
        plt.annotate(
            label,
            xy=(x, y),
            xytext=(-2, 2),
            textcoords='offset points', ha='right', va='bottom'
        )

    plt.show()





""" détection des components  """
def step2():
    img = imageio.imread("../assets/img/cells.jpg")
    image = img[:, :, 0]
    print(image.shape)
    baryAndSizes = all_connected_components(image, 130)
    print(baryAndSizes)


step0()

"""
Travail à effectuer :
Facile : Utiliser un scatter plot pour améliorer la présentation de all_connected_components


Utiliser un scatter pour montrer les all_connected_components des composante R et B.
Puis, pour chaque tache, faites une comparaison en l'intensité des R et des B.
C'est difficile car les barycentre des tache de R et des taches de B peuvent différer de quelque pixels.
Vous devez donc trouvez un algorithme pour associer des points proches. Vous pouvez faire une double boucle
en calculant toutes les distance entre paires de barycentre. Mais si le nombre de barycentre est grand, ce n'est pas
le bon algorithme.
AIDE : souvenez-vous des dictionnaires. Arrondissez les positions.


Plus une galaxie/étoile est éloignée de nous, et plus elle est rouge.
 Plus elle est proche de nous et plus elle est bleue. Savez-vous pourquoi ?
Estimez les distances relatives des différentes galaxie/étoiles apparaissant sur la photo.
 AIDE : vous pouvez bien sur utilisez l'étape précédente, mais il y a une autre technique plus simple ...
 souvenez-vous du TP précédent sur les couleurs.
"""




