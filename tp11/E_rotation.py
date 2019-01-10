
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

from tp11.C_decal2d import convolution_rapide_2d

#np.set_printoptions(precision=1,linewidth=5000)



def get_turned_images(choix, centerReduce=True):

    img1=None
    img2=None


    if choix == 0:
        img1 = ndimage.imread("image/king_head_turn.gif")[:, :, 0]
        img2 = ndimage.imread("image/king.gif")[:, :, 0]
        """que fait-t-on subir à nos images ci-dessous ? """
        img1 = 255 - img1  # type:np.ndarray
        img2 = 255 - img2  # type:np.ndarray


    elif choix == 1:
        img1 = ndimage.imread("image/wood.png")[:, :, 0]
        img2 = ndimage.imread("image/wood2.png")[:, :, 0]

        img1 = 255 - img1  # type:np.ndarray
        img2 = 255 - img2  # type:np.ndarray




    img1,img2=img1.astype(np.float32), img2.astype(np.float32)
    if centerReduce:
        img1-=img1.mean()
        img1/=img1.std()
        img2 -= img2.mean()
        img2 /= img2.std()



    return img1,img2



"""observons les transformations géométriques d'images.
Pourquoi est-ce que ce n'est pas trivial de faire une rotation ou une dilatation d'image ?
Renseignez vous sur l'interpolation cachée derrière, et expliquer l'option "order=2"
dans les fonctions de transformations ci-dessous.

"""
def step01():
    img1,img2=get_turned_images(1)
    img1[:,:,1] = img1[:,:,1]*np.imag
    plt.subplot(2,2,1)
    plt.imshow(img1)
    plt.show()

def step0():
    img1,img2=get_turned_images(1)


    rot=ndimage.rotate(img1,80,order=2)
    affine=ndimage.affine_transform(img1,[[2,0],[0,2]],order=2)


    plt.subplot(2,2,1)
    plt.imshow(img1)
    plt.subplot(2,2,2)
    plt.imshow(rot)
    plt.subplot(2, 2, 3)
    plt.imshow(affine)
    plt.subplot(2, 2, 4)
    plt.imshow(img2)
    plt.show()




from scipy.ndimage.filters import gaussian_filter

"""attention, le programma tourne  longtemps :
on teste toutes les rotation et l'on regarde le max de la correlation (ou anti-convolution) """
def step1():
    img1, img2 = get_turned_images(1)


    """ici flouter n'améliore pas la méthode, au contraire, avec trop de blur, et en convolution-circulaire, on ne trouve pas
    le bon angle. Dans quel cas un floutage serait indispensable - si on a bcp une image des textures? """
    blur=None
    if blur is not None:
        gaussian_filter(img1, sigma=blur, output=img1)
        gaussian_filter(img2, sigma=blur, output=img2)


    values=[]
    """si vous ordi est rapide, vous pouvez descendre le pas à 10 ou 5"""
    for angle in np.arange(0,360,20):
        rot = ndimage.rotate(img1, angle, order=2)
        """mettre circular à true accélère la procédure, mais un autre pic apparaît"""
        cor = convolution_rapide_2d(rot, img2, True, True)
        values.append(np.max(cor))
    plt.subplot(1,3,1)
    plt.imshow(img1)
    plt.subplot(1,3,2)
    plt.imshow(img2)
    plt.subplot(1,3,3)
    plt.title('Blur')
    plt.plot(values)
    plt.show()




"""plutôt que de tout essayer, on va coder une petite fonction de minimisation d'une fonction sur [0,360] module 360"""

def find_min_local(loss_function, step, dep, nb_iter):

    place=dep
    val=loss_function(place)
    val_plus = loss_function((place + step) % 360)
    val_moins = loss_function((place - step) % 360)
    places=[];
    values=[];

    for i in range(nb_iter):

        if val_plus<val :
            val_moins = val
            val = val_plus
            place = place + step
            val_plus = loss_function((place + step) % 360)

        elif val_moins<val:
            val_plus=val
            val=val_moins
            place = place - step
            val_moins=loss_function((place - step) % 360)

        else:
            step/=2
            val_plus = loss_function((place + step) % 360)
            val_moins = loss_function((place - step) % 360)

        print("iteration %d, place %.5f, value %.10f"%(i,place,val))

        values.append(val)
        places.append(place)

    plt.plot(values)
    plt.plot(places)
    plt.show()

    return place, val


"""testons la minimisation sur un exemple simple"""
def step2():
    def loss(x):
        return (x/360)**2

    places=[];
    values=[];

    print("en montant")
    arg_mini,mini=find_min_local(loss,122,245,15)
    print("final:",arg_mini,mini)

    print("En descendant")

    arg_mini, mini = find_min_local(loss, 72, 155, 15)
    print("final:", arg_mini, mini)



"""
Travail : faite un sortie graphique de ce programme
"""



""" revenons à la recherche de l'angle optimal"""
def step3():
    img1, img2 = get_turned_images(0)


    def getValue(angle):
        rot = ndimage.rotate(img1, angle, order=2)
        cor = convolution_rapide_2d(rot, img2, False, True)
        return  -np.max(cor)



    arg_mini, mini = find_min_local(getValue, 30, 10, 20)
    print("final:", arg_mini, mini)

    rot2= ndimage.rotate(img1, arg_mini, order=2)

    plt.subplot(1,3,1)
    plt.imshow(img1)
    plt.subplot(1,3,2)
    plt.imshow(img2)
    plt.subplot(1,3,3)
    plt.imshow(rot2)
    plt.title('Back Rotation')
    plt.plot()
    plt.show()


"""
travail :
superposez les images avec l'angle trouvé.


MEGA BONUS:
Maintenant, il vous faut recaler la tête du rois tournée et zoomée (choix==1).

Vous pouvez essayer tous les zooms et toutes les rotations mais c'est un peu lent.
Je vous conseille de faire votre petit algo d'optimisation (inspirez-vous du mien). Même si votre méthode se fait
Piéger par les minimums locaux, pas de problème: relancez la  plusieurs fois avec plusieurs points de départ différents.
Pendez à tracer votre fonction loss en niveau de couleur,
cela vous permettra d'estimer son irrégularité. Illustrez graphiquement le déroulement
de votre algorithme (en superposant un scater plot et le dessin de la fonction loss).
Cela vous permettra de l'améliorer.

Vous pouvez aussi utiliser les méthodes de :
from scipy.optimize import minimize
Mais elles ne sont très difficile à paramétrer.

Beaucoup de méthode d'optimisation réclament qu'on leur donne explicitement un gradient ou une matrice hessienne
 (cf cours d'optmisation).  En fait, pour nos transformation géométriques simples, les gradient et les hessiennes ne sont
 se calculent explicitement. Cela donne des méthodes de Lucas-Kanade décrites dans le chapitre "non rigid image matching"
 dans le dossier biblio.


"""






if __name__=='__main__':
    step0()



