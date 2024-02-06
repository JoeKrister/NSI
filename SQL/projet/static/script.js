let chg_desc = document.getElementById('desc');
chg_desc.addEventListener('click', inversement1);
let chg_asc = document.getElementById('asc');
chg_asc.addEventListener('click', inversement2);


function inversement1(){
	boutons = document.getElementsByClassName('bouton_tri');
	for (var i =0; i<boutons.length; i=i+1) {
		if (boutons[i].name.includes("_D")==false){
		boutons[i].name += "_D";}
	}
}

function inversement2(){
	boutons = document.getElementsByClassName('bouton_tri');
	for (var i =0; i<boutons.length; i=i+1) {
		if (boutons[i].name.includes("_D")==true){
		boutons[i].name = boutons[i].name.replace("_D", "");}
	}
}

