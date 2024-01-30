var btn1 = document.querySelector(".btn1");
btn1.addEventListener("click", inversement);

//function inversement1(){
	//document.getElementById("desc").click()
	//document.location.href="pieceotheque_D"
//}

function inversement(){
	document.getElementById("desc").click()
	var elt = document.querySelector('input');
	elt.name += '_D';
}

