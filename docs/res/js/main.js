class LogObject{
  constructor(pv_max, bouclier, endurance, arme, bonus, atq_type, capa_type, dist, des_atq, des_def, des_bonus_def, des_esquive, res_deg, pv_reste, date){
    this.pv_max = parseInt(pv_max);
    this.bouclier = parseInt(bouclier);
    this.endurance = parseInt(endurance);
    this.bonus = arme;
    this.val_bonus = parseInt(bonus);
    this.atq_type = parseInt(atq_type);
    this.capa_type = capa_type;
    this.dist = parseInt(dist);
    this.des_atq = parseInt(des_atq);
    this.des_def = parseInt(des_def);
    this.des_bonus_def = des_bonus_def;
    this.des_esquive = parseInt(des_esquive);
    this.res_deg = parseInt(res_deg);
    this.pv_reste = parseInt(pv_reste);
    this.date = date;
  }

  formatDate(date){
    return "jj/mm/aaaa a HHhMM".replace("jj", this.formatNumber(date.getDate())).replace("mm", this.formatNumber(date.getMonth()+1))
      .replace("aaaa", this.formatNumber(date.getFullYear())).replace("HH", this.formatNumber(date.getHours()))
      .replace("MM", this.formatNumber(date.getMinutes()));
  }

  formatNumber(num){
    if(num < 10){
      return "0" + num.toString();
    }
    return num.toString();
  }

  defToStr() {
    var res =
    "Defenseur:\n"+
    "- Pv max: {pv_max}\n"+
    "- Bouclier: {bouclier}\n"+
    "- Endurance: {endurance}\n";
    return res.replace("{pv_max}", this.pv_max)
      .replace("{bouclier}", this.bouclier)
      .replace("{endurance}", this.endurance);
  }

  atqToStr(){
    var res =
    "Attaquant:\n"+
    "- Bonus: {bonus}\n"+
    "- Valeur du bonus: {val_bonus}\n"+
    "- {atq_type}\n"+
    "- {dist}\n";

    if(!this.atq_type){
      res = res.replace("{atq_type}", "Attaque normale");
    }else{
      res = res.replace("{atq_type}", "Capacité: {capa_type}");
    }

    if(!this.dist){
      res = res.replace("{dist}", "Corps-à-corps");
    }else{
      res = res.replace("{dist}", "Distance");
    }

    return res.replace("{bonus}", this.bonus)
      .replace("{val_bonus}", this.val_bonus)
      .replace("{capa_type}", this.capa_type);
  }

  desToStr(){
    var res =
    "Des:\n"+
    "- Atq: {des_atq}\n"+
    "- Def: {des_def}\n"+
    "- Remise: {remise}\n"+
    "- Type de défense: {des_esquive}\n";
    if(this.des_bonus_def){
      res = res.replace("{remise}", "Oui");
    }else{
      res = res.replace("{remise}", "Non");
    }

    if(!this.des_esquive){
      res = res.replace("{des_esquive}", "Endurance");
    }else{
      res = res.replace("{des_esquive}", "Esquive");
    }

    return res.replace("{des_atq}", this.des_atq)
      .replace("{des_def}", this.des_def);
  }

  resToStr(){
    var res =
    "Resultats:\n"+
    "- Degats: {res_deg}\n"+
    "- Pv restants: {pv_reste}\n";

    return res.replace("{res_deg}", this.res_deg)
      .replace("{pv_reste}", this.pv_reste)
  }

  toString(){
    return this.formatDate(this.date)+"\n\n"+
      this.defToStr()+"\n"+this.atqToStr()+"\n"+
      this.desToStr()+"\n"+this.resToStr()
  }
}

function createLogFromActualInput(){
  elem_inputs.refresh();
  return new LogObject(elem_inputs.pv_max.valueAsNumber, elem_inputs.bouclier.valueAsNumber,
    elem_inputs.endurance.valueAsNumber, elem_inputs.arme.selectedOptions[0].innerText,
    elem_inputs.bonus.valueAsNumber, elem_inputs.atq_type.value, elem_inputs.capacite_type.selectedOptions[0].innerText,
    elem_inputs.dist_atq.value, elem_inputs.des_atq.valueAsNumber, elem_inputs.des_def.valueAsNumber,
    elem_inputs.des_bonus_def.checked, elem_inputs.des_esquive.value, parseInt(elem_inputs.res_deg.innerText),
    elem_inputs.pv_reste.valueAsNumber, new Date())
  }

  window.onkeydown = function(evt){
    evt = evt || window.event;
    if(evt.keyCode == 13){
      calculate()
    }
  }

  window.onload = function() {
    elem_inputs.refresh();
    capa_toggle(elem_inputs.atq_type);
    elem_inputs.pv_max["old_value"] = elem_inputs.pv_max.valueAsNumber;

    elem_inputs.pv_max.onchange = function() {

      if(this.old_value > this.valueAsNumber){
        elem_inputs.pv_reste.valueAsNumber -= this.old_value - this.valueAsNumber;
      }else if(this.old_value < this.value){
        elem_inputs.pv_reste.valueAsNumber += this.valueAsNumber - this.old_value;
      }
      this.old_value = this.valueAsNumber;
      elem_inputs.pv_reste.onchange();
    }

    elem_inputs.pv_reste.onchange = function() {
      this.max = elem_inputs.pv_max.valueAsNumber;
      if(this.valueAsNumber >= elem_inputs.pv_max.valueAsNumber){
        this.valueAsNumber = elem_inputs.pv_max.valueAsNumber;
      }
      if(this.valueAsNumber <= 0){
        this.valueAsNumber = 0;
      }
      if(isNaN(this.valueAsNumber)){
        this.valueAsNumber = elem_inputs.pv_max.valueAsNumber;
      }
    }
  }

  function capa_toggle(elem){
    if(parseInt(elem.value)){
      elem_inputs.capacite_type.disabled = false;
    }else{
      elem_inputs.capacite_type.disabled = true;
    }
  }

  function log_ecriture(){

  } //A faire plus tard quand le cadre aura été fait, partie 2 du programme
  //s'efface quand on actualise !

  function clearAll(){} //Ajouter un bouton d'effacer tous les champs mais NE DOIT PAS EFFACER LES LOGS

  function test_none(t){
    lg=t.trim();
    if (((! t) || (lg.length == 0))) {
      return true;
    }
    return false;
  }

   function checkError()
  {
    var pv_max=elem_inputs.pv_max.value;
    var atq = elem_inputs.des_atq.value;
    var shield =elem_inputs.bouclier.value;
    var dice_endurance=elem_inputs.endurance.value;
    var pv_restant=elem_inputs.pv_reste.value;
    var bonus_entry=elem_inputs.bonus.value;
    var defense=elem_inputs.des_def.value;

    var int_pv_max=parseInt(pv_max);
    var int_atq=parseInt(atq);
    var int_shield=parseInt(shield);
    var int_dice_endu=parseInt(dice_endurance);
    var int_pv_restant=parseInt(pv_restant);
    var int_bonus=parseInt(bonus);
    var int_defense=parseInt(defense);


    if ((isNaN(pv_max)) || (isNaN(atq)) || (isNaN(shield)) || (isNaN(dice_endurance)) || (isNaN(pv_restant)) || (isNaN(bonus_entry)) || (isNaN(defense)))
    {
      elem_inputs.pv_max.style.color="#841A15";
      elem_inputs.des_atq.style.color="#841A15";
      elem_inputs.bouclier.style.color="#841A15";
      elem_inputs.endurance.style.color="#841A15";
      elem_inputs.pv_reste.style.color="#841A15";
      elem_inputs.bonus.style.color="#841A15";
      elem_inputs.des_def.style.color="#841A15";
      elem_inputs.res_deg.innerHTML='Erreur, les variables ne sont pas numériques';
    }
    else if (((test_none(pv_max)) || (test_none(atq)) || (test_none(shield)) || (test_none(dice_endurance)) || (test_none(pv_restant)) || (test_none(defense))))
    {
      elem_inputs.pv_max.style.color="#841A15";
      elem_inputs.des_atq.style.color="#841A15";
      elem_inputs.bouclier.style.color="#841A15";
      elem_inputs.endurance.style.color="#841A15";
      elem_inputs.pv_reste.style.color="#841A15";
      elem_inputs.bonus.style.color="#841A15";
      elem_inputs.des_def.style.color="#841A15";
      elem_inputs.res_deg.innerHTML='Erreur, les variables sont vides';
    }
    else if ( (int_atq > 10) || (int_defense > 10) || (int_dice_endu > 10) || (int_bonus > 10))
    {
      elem_inputs.des_atq.style.color="#841A15";
      elem_inputs.des_def.style.color="#841A15";
      elem_inputs.endurance.style.color="#841A15";
      elem_inputs.bonus.style.color="#841A15"
      elem_inputs.res_deg.innerHTML='Erreur, certaines variables sont supérieures à 10.';
    }
    else if ((int_bonus >= 100)||(int_shield >= 100))
    {
      elem_inputs.bonus.style.color="#841A15";
      elem_inputs.bouclier.style.color="#841A15";
      elem_inputs.res_deg.innerHTML='Erreur, certaines variables sont supérieures à 100.';
    }
    else if ((int_pv_max <=0))
    {
      elem_inputs.pv_max.style.color="#841A15";
      elem_inputs.res_deg.innerHTML='Erreur, les pv max sont inférieur ou égal à 0';
      elem_inputs.res_deg.style.color="#841A15";
    }
    else if ((pv_restant > pv_max))
    {
      elem_inputs.pv_reste.style.color="#841A15";
      elem_inputs.res_deg.innerHTML='Erreur, les pv restant sont supérieurs au pv max';
    }
  }
