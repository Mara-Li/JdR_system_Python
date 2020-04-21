function button_check(name_groupe){
  var lst_elem = document.getElementsByName(name_groupe);


}



function choix_bonus()
{
  let b;
  bonus=document.getElementByID('arme').value;
  bonus_val=document.getElementByID('bonus').value;
  dist=button_check() ; //récupération du bouton distance sur la boite bonus
  if (bonus=='Pouvoir')
  {
    b = 10+bonus_val;
  }
  else if (bonus === 'Fusil')
  {
    b = 10 + bonus_val;
    if (dist) { //est checked
      b=b+5;
    }
  }
else if (bonus === 'Projectile')
{
    b = 5+bonus_val;
  }
  else if (bonus=='Epée') {
    b=10+bonus_val;
  }
  else if (bonus=='Contondant'){
        b=15+bonus_val;
      }
    else if (bonus=='Couteau')
      {
        b=5+bonus_val;
      }
    else if (bonus=='Pistolet') {
        b=8+bonus_val;
      }
    else if (bonus=='Artillerie') {
        b=15+bonus_val;
        if (dist) { //est check
            b=b+10;
          }}
    else if (bonus=='Autre') {
        b=bonus_val;
      }
    else if (bonus=='Aucun')
    {
        b=0;
      }
  return b;
}


function reussite_endurance(endu_de, endu_val, PV, d, shield)
{
  let d;
  d=Math.abs(d*PV);
  var bouclier=Math.abs(d*(1-shield)); //au besoin, placé des int pour convertir les valeurs
  remise=//checkbox "bonus"
  var finaux=0;
  if (remise) //est check
  {
    if (endu_de > endu_val) || (endu_de==endu_val)
    {
      finaux=bouclier;
    }
    else if (endu_val == 0)
    {
      finaux=bouclier;
    }
    else {
      finaux=bouclier*(1-(10*Math.abs((endu_val - endu_de)+1))/100);
    }
  }
  else {
    if (endu_de > endu_val)
    {
      finaux=bouclier;
    }
    else if (endu_val==0)
    {
      finaux=bouclier
    }
    else
    {
      finaux= bouclier*(1-(10*Math.abs((endu_val - endu_de)+1))/100)
    }
  }
  if (finaux >= PV)
  {
    finaux=PV
  }
  else {
    finaux=finaux //je sais pas s'il faut mettre un int ?
  }
}

fonction vie_restante(finaux)
{
  vie = //champ pv restant
  vie = vie - finaux;
  msg_pv=vie;
  if (vie <= 0)
  {
    vie=0; //au besoin, mettre en caractère
    msg_pv='X';
  }
  //vider le champ "PV_restant"
  //inserer la valeur de vie restante
  //inserer msg_pv
}

fonction capacite_bonus(bonus)
{
  atq = //valeur dé champ Attaque
  if (atq==0){
    bonus=bonus*1.8;
  }
  else if (atq==1){
    bonus=bonus*1.4;
  }
  return bonus;
}

fonction calculate_degat(bonus, atq, defe){
  var d;
  d = Math.abs((ATQ - DEFE));
  if ((d === 0)) {
      d = (0 + bonus);
  } else if ((d === 1)) {
          d = (0.05 + bonus);
      }
      else if ((d === 2)) {
              d = (0.1 + bonus);
          }
          else if (((d === 4) || (d === 3))) {
                  d = (0.2 + bonus);
              }
              else if (((d === 5) || (d === 6))) {
                      d = (0.3 + bonus);
                  }
                  else if (((d === 7) || (d === 8))) {
                          d = (0.4 + bonus);
                      }
                      else if ((d >= 9)) {
                              d = (0.5 + bonus)
                            }
  return d;

}

fonction degat_burst(bonus, atq, defe, endu_val)
{
  var d;
  if ((ATQ === 0)) {
      d = (0.25 + bonus);
      endu_val = 0;
  } else if ((DEFE === 0)) {
          d = 0;
      }
      else if ((ATQ === 1))
      {
        d = calculate_degat(bonus, ATQ, DEFE)
      }
          else
          {
              d = calculate_degat(bonus, ATQ, DEFE);
          }
  return [d, endu_val];
}

fonction degat_burst_bouclier(bonus, atq, defe, endu_val)
{
  var d;
  if ((ATQ === 0)) {
      d = (0.38 + bonus);
      endu_val = 0;
  }
  else if ((DEFE === 0)) {
          d = 0;
      } else if ((ATQ === 1)) {
              d = calculate_degat(bonus, ATQ, DEFE);
          }
          else {
              d = calculate_degat(bonus, ATQ, DEFE);
          }
  return [d, endu_val];
}

fonction degat_perforant(bonus, atq, defe, endu_val)
{
  var d;
  if ((ATQ === 0))
  {
      d = (0.4 + bonus);
      endu_val = 0;
    }
  else if ((DEFE === 0))
  {
    d = 0;
  }
  else if ((ATQ === 1))
  {
    d = calculate_degat(bonus, ATQ, DEFE);
  }
  else
    {
      d = calculate_degat(bonus, ATQ, DEFE);
    }
  return [d, endu_val];
}

fonction degat_autre(bonus, atq, defe, endu_val)
{
  var d;
  if ((ATQ === 0))
  {
      d = (0.5 + bonus);
      endu_val = 0;
  }
  else if ((DEFE === 0))
  {
    d = 0;
  } else if ((ATQ === 1))
  {
    d = calculate_degat(bonus, ATQ, DEFE);
  }
  else
  {
    d = calculate_degat(bonus, ATQ, DEFE);
  }
  return [d, endu_val];
}

fonction degat_type()
{
    var atq, defe, pv, shield, bonus, bonus_attaque, bonus_type, d, endu_de, endu_val, finaux, max;
    bonus=//valeur du champ "bonus"
    pv=//valeur du champ PV au départ
    atq=//valeur du dés d'Attaque
    defe=//valeur du dé de défense
    sel_defe=//type de défense - valeur dans dés [Endurance ou Esquive raté]
    type_capa=//Valeur de la spinbox dans capacité ["Burst", "Autre", "Perforante"]
    if (sel_defe == 'Endurance')
      {
        endu_de=defe;
      }
      else {
        endu_val=0;
        endu_de=10;
      }
      shield=//valeur du champ "Bouclier"
      shield=shield/100;
      if (type_capa=='Burst')
      {
        endu_val=//valeur champ "endurance" dans stats
        if (shield !==0)
        {
          bonus_type = capacite_bonus(15);
          bonus = ((bonus_type + bonus) / 100);
          [d, endu_val] = degat_burst_bouclier(bonus, atq, defe, endu_val); //est ce qu'on peut faire ça en JS ?
        }
        else {
          bonus_type = capacite_bonus(25);
          bonus = ((bonus + bonus_type) / 100);
          [d, endu_val] = degat_burst(bonus, atq, defe, endu_val);
        }
      }
      else if (type_capa=='Autre')
      {
        bonus_attaque = choix_bonus();
        bonus = capacite_bonus(bonus);
        bonus = ((bonus_attaque + bonus) / 100);
        endu_val = //récupérer la valeur du champ d'endurance
        [d, endu_val] = degat_autre(bonus, atq, defe, endu_val);
        shield = //
      }
      else if (type_capa=='Perforante')
      {
        bonus_type = capacite_bonus(15);
        bonus = ((bonus_type + bonus) / 100);
        endu_val = 0;
        shield=0;
        [d, endu_val] = degat_perforant(bonus, ATQ, DEFE, endu_val);
      }
      finaux=reussite_endurance(endu_de, endu_val, pv, d, shield);
      finaux=(finaux/1.4) //Au besoin, convertir en int
      max=finaux;
      if (pv >= 1000))
      {
        max=200
      }
      else if ( (pv > 100) && (pv < 1000))
      {
        max=100;
      }
      else if (pv <= 100))
      {
        max=80
      }
      if (finaux > max))
      {
        finaux=max;
      }
      //inserer la valeur "finaux" dans le champ concerné dans résultat
      vie_restante(finaux);
}

fonction degat_normaux()
{
  var atq, defe, pv, shield, bonus, d, endu_de, endu_val, finaux, max;
  bonus = choix_bonus();
  pv= //champ pv du programme
  atq=//champ attaque dans dé
  defe=//champ défense dans dé
  bonus=(bonus/100);
  endu_val=//valeur de l'endurance dans les stats
  shield=//valeur du champ "bouclier"
  shield=shield/1000;
  d=calculate_degat(bonus, atq, defe);
  sel_def=button_check()//insérer le nom qui correspond
  if (sel_def) //est 1 ; checké ?
  {
    endu_de=defe;
  }
  else
  {
    endu_val=0;
    endu_de=10;
  }
  if (atq==0)
  {
    d=(0.5+bonus);
    endu_val=0
  }
  else if (defe==0)
  {
    d=0;
  }
  else if (atq==1)
  {
    endu_val=0;
  }
  finaux=reussite_endurance(endu_de, endu_val, pv, d, shield);
  finaux=finaux/1.4;
  max=finaux;
  if (pv >=1000){
    max=200;
  }
  else if (pv >100) && (pv <1000)
  {
    max=100;
  }
  else if (pv <100)
  {
    max=80;
  }
  if (finaux > max)
  {
    finaux=max;
  }
  //insérer la valeur final
  vie_restante(finaux);
}

fonction log_ecriture()
{} //A faire plus tard quand le cadre aura été fait, partie 2 du programme
//s'efface quand on actualise !

fonction clearAll(){} //Ajouter un bouton d'effacer tous les champs mais NE DOIT PAS EFFACER LES LOGS

fonction checkError(){} //truc en rouge qui indique quand y'a des erreurs


fonction calculate()
{
  //test check des erreurs
  selection=//valeur si on choisit une attaque normale ou une Capacité
  if (selection //est checké ? egale à 1 ?  égale à "Attaque normale" ?)
    {
      degat_normaux();
    }
    else {
      degat_type();
    }
    log_ecriture();
}

fonction grisage_capacité (){
  // En gros, quand le radiobutton "attaque normale" est sélectionné, le spinbox "capacité" est grisé et non utilisable !!
}

/*
A faire :
- Ajouter un bouton pour clear les champs
- Permettre de lancer le programme avec "ENTER"
- Faire que le champ pv restant change automatiquement quand on change les pv totaux/max
- Mettre la boite pour les LOGS
- aligner les boutons
- Lock les spinbox de nombre entre 0 et 10
*/
