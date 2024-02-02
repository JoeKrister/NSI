let chg_desc = document.getElementById('desc');
chg_desc.addEventListener('click', inversement);

function inversement(){
	boutons = document.getElementsByClassName('bouton_tri');
	for (var i =0; i<boutons.length; i=i+1) {
		if (boutons[i].name.includes("_D")==false){
		boutons[i].name += "_D";}
	}
	
}


 