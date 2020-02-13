Ce programme vise à aider les joueurs des chroniques de l'Impérium à calculer leur dégâts.  Il peut cependant être utilisé par d'autres RP en utilisant les règles ci-après. A noté que nous utilisons donc un système avec un dé de 10, et des caractéristiques. Les titres et descriptions de ses caractéristiques importent peu, tant que vous gardez un système d'endurance et d'esquive. 

Cependant, il n'est pas possible de changer le système hors du dés 10 sans toucher au code. Cela dit, je pense que les calculs devraient être valable avec tous les autres types de dés si on modifie ce dernier, en modifiant les différences pour y faire correspondre.

# Build :

Les joueurs n'auront accès qu'à un menu codé avec tkinter.

Pour celles et ceux qui aimerait le faire tourner directement avec python, vous avez besoin de Python3 et de Tktinter.

Sinon, pour build en .exe vous pouvez utiliser cx_freeze, que vous pouvez installer avec pip ! Le setup étant déjà construit, vous n'avez juste qu'à faire : 

```bash
python.exe setup.py build
```

Pour plus d'information à propos de cxfreeze : https://sourceforge.net/projects/cx-freeze/

Le fichier executable ne marche pour l'instant qu'avec windows. Pour l'utiliser avec Linux ou Mac, vous devez installer python 3.x (à noter que tkinter est inclus avec python 3.x). Après, vous n'aurez qu'à lancer, dans le dossier du programme (par exemple) un terminal puis `python3 CDI_dice.py`. 

-----

# SYSTEME DE COMBAT

Le système de combat du RP est très simple : il se déroule au tour par tour, avec un lancé de dé d'attaque et de défense, qui s'échange après chaque "tour". La réussite des actions est donc déterminé à la fois par votre score et la caractéristique liée mais aussi par le dé de défense de votre adversaire. 

La caractéristique que vous lancez pour votre défense est soit un dé d'endurance ou d'agilité. 
- L'endurance permet d'encaisser le coup, le défenseur recevra donc moins de dégâts.
- L'agilité permet d'esquiver le coup (et donc de ne pas prendre de dégâts), cependant le défenseur ne pourra pas attaquer au tour suivant, sauf dans le cas d'un coup critique (score de 1 ou moins), où votre personnage peut contre-attaquer.

Choisissez donc bien en fonction de vos caractéristiques !

Vous devez OBLIGATOIREMENT lancé votre dé avant de déterminer votre action. Mais vous n'êtes pas obligé d'attendre le dé de défense de votre adversaire. Dans tous les cas, l'action finale avec les dégâts sera après le lancé des protagonistes de l'action. 

Dans le cas où il y aurait un 1 VS plusieurs, la personne en sous nombre doit lancé un dé de défense pour chaque attaque reçu mais ne peut attaquer qu'une seule personne à la fois.

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
- Burst correspond à un simple bonus de 30% mais ses capacités traversent très mal les boucliers. 
- Autre : Tout ce qui ne rentrerait pas dans les deux schémas précédents, mais dont vous souhaitez quand même qu'ils bénéficient de la prime d'un ultra coup-critique ou d'un coup-critique.

### Les primes

Dans le cas où votre personnage fait : 

- Un coup critique : Son bonus sera multiplié par 1,5. 
- Un Ultra critique : Son bonus sera multiplié par 2.

:warning: Lorsque l'on multiplie, on ne prend pas en compte le "pourcent" (la division par 100).

## Exception

Il existe TROIS exceptions aux systèmes de dégâts : 

- Les Ultra coup-critiques *d'attaque* :  Lorsqu'un PJ a un score de dés égal à 0, il obtient automatiquement le bonus de 50% et outrepasse la défense par endurance de son adversaire. 

- Les Ultra coup-critiques *de défense* : Lorsqu'un combattant a un score de dés d'endurance égal à 0, il annule automatiquement l'attaque de son adversaire, quelque soit la valeur de son dé. 

- Les coup-critiques d'attaque :  Lorsqu'un combattant a un score de dés égal à 1, il annule la défense par endurance de son adversaire.

A noté où dans le cas où les deux combattant font des UCC d'attaque et de défense (La probabilité est mince), c'est l'attaquant qui aura l'avantage.

# Utilisation

* A droite, vous remplissez vos caractéristiques, à gauche, les dés qui ont été lancé. Vous n'avez pas besoin de faire de calcul : le programme est là pour ça. Ainsi, pour le bouclier et les bonus, vous avez juste à marquer le pourcentage qui correspond (sans évidemment, diviser par 100, le programme s'en occupe aussi). 
* Lorsque vous avez une esquive raté, il n'est pas nécessaire de remplir la partie "Endurance" : vous pouvez laisser à 0. Vous devez tout de même remplir la partie **DEF** qui correspond à la valeur que vous avez. 
* Dans le cas où c'est l'endurance qui est utilisé pour la défense, vous devez remplir tous les champs et **les champs DEF et END ont alors les mêmes valeurs**.
* De manière évidente, vous n'avez pas besoin de calculer les dégâts lorsque le défenseur a esquivé. 
* Vous devez choisir si votre personnages attaque avec une capacité ou non. Par défaut, ce sont les attaques normales. En effet, un coup critique avec une capacité a un bonus différent qu'un coup critique avec une attaque normale. Pour changer cela, il suffit de cliquer sur le bouton radio. 
* Le bouton radio permet d'activer un champ qui vous permet de choisir entre les capacités 'Burst', 'perforant' ou 'Autre'. Autre, sans aucun bonus, aura le même résultat qu'une attaque normale.
*  Il n'est malheureusement pas possible de calculer les actions de soutiens ou de malus avec le programme, vous devez donc multiplier vos bonus par vous même en suivant la table.
* Vous n'avez pas besoin de prendre en compte les capacités particulières d'une attaque perforante, d'un UCC et d'un CC, ainsi que les bonus associés aux capacités : le programme s'en charge aussi. Remplissez donc tous les champs sans vous souciez de cela.

## Screenshot

![Imgur](https://imgur.com/vzi0fB2.png)

![imgur](https://imgur.com/KOdvL4b.png)

![Imgur](https://imgur.com/Gd8G98c.png)

![Imgur](https://imgur.com/ScwLNwS.png)

