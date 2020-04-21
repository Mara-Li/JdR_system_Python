const elemIDs = [
    "pv_max",
    "pv_reste",
    "bouclier",
    "endurance",
    "des_atk",
    "des_def",
    "arme",
    "bonus",
    "capacite_type",
    "des_bonus_def"
];

const radioGroupsName = [
    "des_esquive",
    "atk_type",
    "dist_atk"
]

class Elements_getter{
    constructor(lstID, lstRadio){
        this._idLst = lstID;
        this._radioLst = lstRadio;
        lstID.forEach(id => {
            this[id] = document.getElementById(id);
        });
        lstRadio.forEach(name => {
            this[name] = this.getValueFromRadio(name);
        });
    }
    
    getValueFromRadio(group_name){
        var lst_radio = document.getElementsByName(group_name)
        for(var i = 0; i < lst_radio.length; i++){
            if(lst_radio[i].checked){
                return lst_radio[i];
            };
        };
        return undefined;
    }
    
    refresh(){
        this._idLst.forEach(id => {
            this[id] = document.getElementById(id);
        });
        this._radioLst.forEach(name => {
            this[name] = this.getValueFromRadio(name);
        });
        return this;
    }
}

var elem_inputs = new Elements_getter(elemIDs, radioGroupsName);

function choix_bonus()
{
    let b;
    elem_inputs.refresh();
    bonus=elem_inputs.arme.value;
    bonus_val=elem_inputs.bonus.value;
    dist=elem_inputs.dist.value;
    cac=elem_inputs.cac.value;
    if (bonus=='Pouvoir')
    {
        b = 10+bonus_val;
    }
    else if (bonus === 'Fusil')
    {
        b = 10 + bonus_val;
    }
    else if (bonus === 'Projectile')
    {
        b = 0;
    }
    return b;
}

function reussite_endurance(endu_de, endu_val, PV, d, shield)
{}

function vie_restante(finaux){}

function capacite_bonus(bonus){}

function calculate_degat(bonus, atq, defe){}

function degat_burst(bonus, atq, defe, endu_val){}

function degat_burst_bouclier(bonus, atq, defe, endu_val){}

function degat_perforant(bonus, atq, defe, endu_val){}

function degat_autre(bonus, atq, defe, endu_val){}

function degat_type(){}

function degat_normaux(){}

function log_ecriture(){}

function calculate(){}

function clearAll(){}

function clear_log(){}

function checkError(){}