A noter que nous utilisons donc un système avec un dé de 10, et des caractéristiques. Les titres et descriptions de ses caractéristiques importent peu, tant que vous gardez un système d'endurance et d'esquive. 

Cependant, il n'est pas possible de changer le système hors du dés 10 !

:warning: Il est possible que votre antivirus signale le programme. Je peux vous assurer qu'il n'y a AUCUN virus dans ce code. Ce sont des faux positifs qui sont causé par les paramètres de build de pyinstaller, et je ne peux donc pas y faire grand chose. Le mieux c'est d'utiliser le fichier zip dans un dossier qui aura été mis en liste blanche auparavant, sinon, votre antivirus mettra en quarantaine (ou supprimera) le programme. 

# Build :

## Windows

Les joueurs n'auront accès qu'à un menu codé avec tkinter.

Pour celles et ceux qui aimerait le faire tourner directement avec python, vous avez besoin de Python3 et de Tktinter.

Sinon, pour build en .exe vous pouvez utiliser pyinstaller, que vous pouvez installer avec pip! Ensuite, vous n'aurez qu'à lancer le script qui permettra de build les programmes.



Pour plus d'information à propos de pyInstaller : https://www.pyinstaller.org/



Note : IL EST TRES IMPORTANT DE MODIFIER LA LIGNE `gui.iconbitmap(r"D:\\Documents\\GitHub\\CDI_Dice_Help\\data\\logo.ico")` avec le chemin du logo si vous voulez le build. 

## Mac / Linux :

Le fichier executable ne marche pour l'instant qu'avec windows. Pour l'utiliser avec Linux ou Mac, vous devez installer python 3.x (à noter que tkinter est inclus avec python 3.x). Après, vous n'aurez qu'à lancer, dans le dossier du programme (par exemple) un terminal puis `python3 CDI_dice.py`. 

Attention, pour mac, il semblerait qu'il y ait des problèmes :

- D'affichage
- De lancement, car le programmes utilisent des liens de fichier qui ont une écriture différente sous mac.

Actuellement, je cherche à build sous mac ou éditer le code pour permettre le lancement du programme en fonction de l'OS utilisé. 

-----

# SYSTEME DE COMBAT


La caractéristique que vous lancez pour votre défense est soit un dé d'endurance ou d'agilité. 
- L'endurance vous permet d'encaisser le coup, il recevra donc moins de dégâts.

- L'agilité vous permet d'esquiver le coup (et donc de ne pas prendre de dégâts). De plus, pour réussir votre esquive, vous devez faire moitié moins que l'adversaire. Ainsi, s'il fait une attaque de 8, vous devez faire 4 ou moins. Certaines attaques deviennent donc impossible à esquiver à partir d'un certains scores (1 et 0).


Il existe cependant des attaques qui ne rentrent dans cette catégorie : les altérations d'état.

:white_small_square: Les attaques mentales (parleur, liseur) : Elles nécessitent une défense avec un dé d'intelligence.

:white_small_square: Les attaques liés aux poisons et maladies (cheval pâle) : Elles nécessitent un dé de karma.




Choisissez donc bien en fonction de vos caractéristiques !



Vous devez OBLIGATOIREMENT lancer votre dé avant de déterminer votre action. Mais vous n'êtes pas obligé d'attendre le dé de défense de votre adversaire. Dans tous les cas, l'action finale avec les dégâts sera après le lancé des protagonistes de l'action. 



Dans le cas où il y aurait un 1 VS plusieurs, la personne en sous nombre doit lancé un dé de défense pour chaque attaque reçu et peut attaquer un certain nombre de personne en fonction de son rang.

## Dégâts

Les dégâts sont déterminés en fonction de l'écart de dé entre l'attaquant et le défenseur dans le cas où le défenseur n'a pas réussi à esquiver l'attaque. Ainsi :

-  Ecart de 9 (voire+): Coup critique : L'adversaire perd 50% de ses PV 

- De 8 à 7 : Très Bon dégât : Le défenseur perd 40% de ses pv. 

- De 6 à 5 : Bon dégât : Le défenseur perd 30% de ses pv. 

- De 4 à 3 : Dégât moyen: Le défenseur perd 20% de ses pv. 

- 2 : Dégât faible : Le défenseur perd 10% de ses pv. 

- 1 : Dégât très faible : Le défenseur perd 5% de ses pv. 

- 0 : Le défenseur ne prend aucun dégât. 

Dans le cas où le défenseur aurait encaissé le coup (dé d'endurance), il perd moins de pv. 

En général, sa défense diminue de 10% les dégâts en fonction de la valeur de son dé et donc, de sa caractéristique d'endurance. Ainsi, avec 8 d'endurance, il diminuerait les dégât de 80% dans le cas d'un coup critique (score de 0), et cela diminuerait jusqu'à la valeur seuil de son dé. 



:warning: Attention, dans le cas où la personne posséderait une "remise"(diminution du dé), la valeur seuil n'est plus la même que la caractéristique : le dé doit avoir une valeur strictement inférieure pour que l'endurance soit validé. 


## Cas des duels amicaux

Lors d'un combat entre PJ "amicaux", vous ne perdez pas de pv et vous devez lancer un dé 10 pour déterminer celui qui a l'initiative. La personne avec le plus grand score commence.


## Bouclier

Les boucliers protègent des dégâts. Dans les faits, cela fonctionne exactement comme un encaissement avec un dé d'endurance. Cependant, les résistances sont fixes et liés soit à votre équipement, soit au rang de votre adversaire. En général, il existe :

- Armure légère : Diminution de 10%
- Armure moyenne : Diminution de 25%
- Armure lourde : Diminution de 50%.

## CAPACITE

Avec la mise à jour 1.4, vous pouvez maintenant introduire directement les capacités aux calculs du programme.

Ainsi :

- Perforant correspond à un bonus de 15%, mais la capacité traversa toute les défense de l'ennemi.
- Burst correspond à un simple bonus de 25% mais ses capacités traversent très mal les boucliers (Le bonus descendra à 12% à ce moment)
- Autre : Tout ce qui ne rentrerait pas dans les deux schémas précédents, mais dont vous souhaitez quand même qu'ils bénéficient de la prime d'un ultra coup-critique ou d'un coup-critique. 

Il est à noté qu'il y a de nombreux équilibrage vis à vis des dégâts qui ne sont pas détaillés ici. Vous les retrouverez dans le code dans les fonctions `degat_burst`, `degat_burst_bouclier`, `degat_perforant` et `degat_autre`.

### Bonus

Certaines attaques ont des bonus très légers, ainsi :

- Pouvoir : 10%
- Pistolet : 8%
- Fusil : 10%
- Artillerie : 15%
- Couteau: 5%
- Projectile : 5%
- Epée : 10%
- Contondant : 15%
- Autre : 0% - Mais vous pouvez choisir le bonus que vous voulez entrer
- Aucun : Absence de bonus - c'est la valeur par défaut du programme.

Evidemment, pour toutes les attaques, vous pouvez rajouter des bonus extérieur avec le champ correspondant. 

### Les primes

Dans le cas où votre personnage fait : 

- Un coup critique : Son bonus sera multiplié par 1,4.
- Un Ultra critique : Son bonus sera multiplié par 1.8.

De plus, les deux ont un bonus d'attaque très léger, afin d'équilibré par rapport aux attaques normales. 

:warning: Lorsque l'on multiplie, on ne prend pas en compte le "pourcent" (la division par 100).

## Exceptions

Il existe TROIS exceptions aux systèmes de dégâts : 

- Les Ultra coup-critiques *d'attaque* :  Lorsqu'un PJ a un score de dés égal à 0, il obtient automatiquement le bonus de 50% et outrepasse la défense par endurance de son adversaire. 

- Les Ultra coup-critiques *de défense* : Lorsqu'un combattant a un score de dés d'endurance égal à 0, il annule automatiquement l'attaque de son adversaire, quelque soit la valeur de son dé. 

- Les coup-critiques d'attaque :  Lorsqu'un combattant a un score de dés égal à 1, il annule la défense par endurance de son adversaire.

A noté où dans le cas où les deux combattant font des UCC d'attaque et de défense (La probabilité est mince), c'est l'attaquant qui aura l'avantage.

# Résumé

* Lancé de dés d'attaque et de défense
>* L'endurance permet d'encaisser les dégâts. 
>* L'esquive permet de ne pas prendre de dégât. Elle est réussit si le dé est moitié moins du dé d'attaque de l'adversaire.

* Dés de 10 lié à votre caractéristiques
>* Remise : Valeur seuil = strictement inférieure à votre caractéristique (7 pour 8, 6 pour 7, etc).
>* Pas de remise : Seuil = caractéristique
* Meilleur jet : 0, pire jet : 10
>Un 0 correspond à un "Ultra coup critique" et un 1 à un "coup critique". 

* Quand vous utilisez votre capacité ou quand vous attaquez avec votre pouvoir, vous devez lancer le dé lié à votre pouvoir.
* De même, si vous attaquez en utilisant une arme, vous devez lancé la caractéristique liée.


# Utilisation

* **Défenseur** : Les caractéristiques qui correspondent à la personne attaquée. Notons que la partie des PV restant se rempli automatiquement avec les PV max, puis se mettra à jour au fur et à mesure
* **Attaquant** : Le type d'attaque, si elle est lancé par une personne ou un monstre, et si c'est ou non une capacité. 
* **Dés** : Simplement le type de défense et les dés qui correspondent à l'attaque et la défense. De plus, vous pouvez cocher ou non si la personne possède un bonus pour sa défense (endurance, surtout)
* **Remise** : Un bonus de départ sur les personnages, qui diminue la valeur des dés lancés. Voir plus haut pour l'impact de ce bouton. 
* Vous pouvez lancer le programme en appuyant sur le bouton mais aussi avec enter.
* **Résultat** : Les PV restant (et le champ correspondant ce met à jour) ainsi que les dégâts infligés. Vous pouvez donc enchainé sur plusieurs attaques sans avoir à reset entièrement le programme, si le défenseur est le même. 
* Le bouton avec la flèche correspond à un reset du programme : les PV reviennent à leur maximum, et les autres champs à leurs valeurs par défauts. 
* Le bouton avec le fichier permet de vider le fichier des logs.
* De manière évidente, vous n'avez pas besoin de calculer les dégâts lorsque le défenseur a réussi son esquive. 
* Vous devez choisir si votre personnages attaque avec une capacité ou non. Par défaut, ce sont les attaques normales. En effet, un coup critique avec une capacité a un bonus différent qu'un coup critique avec une attaque normale. Pour changer cela, il suffit de cliquer sur le bouton radio. 
* Le bouton radio permet d'activer un champ qui vous permet de choisir entre les capacités 'Burst', 'perforant' ou 'Autre'. 
*  Il n'est malheureusement pas possible de calculer les actions de soutiens ou de malus avec le programme, vous devez donc multiplier vos bonus par vous même en suivant la table.
* Vous n'avez pas besoin de prendre en compte les capacités particulières d'une attaque perforante, d'un UCC et d'un CC, ainsi que les bonus associés aux capacités : le programme s'en charge aussi. Remplissez donc tous les champs sans vous souciez de cela.
