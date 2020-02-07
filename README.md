Ce programme vise à aider les joueurs des chroniques de l'Impérium à calculer leur dégâts. 

Les joueurs n'auront accès qu'à un menu codé avec tkinter.

Pour celles et ceux qui aimerait le faire tourner directement avec python, vous avez besoin de Python3 et de Tktinter.

Sinon, pour build en .exe vous pouvez utiliser cx_freeze, que vous pouvez installer avec pip ! Le setup étant déjà construit, vous n'avez juste qu'à faire : 

```bash
python.exe setup.py build
```

Pour plus d'information à propos de cxfreeze : https://sourceforge.net/projects/cx-freeze/


Le fichier executable ne marche pour l'instant qu'avec windows. Pour l'utiliser avec Linux ou Mac, vous devez installer python 3.x (à noter que tkinter est inclus avec python 3.x). Après, vous n'aurez qu'à lancer, dans le dossier du programme (par exemple) un terminal puis `python3 CDI_dice.py`. 
