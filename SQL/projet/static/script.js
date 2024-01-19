function sorted_button()
{
    if(document.getElementById('nbr_ex').checked)
    {
        document.getElementById('nbr_ex').style.display = 'block';
        document.getElementById('emet').style.display = 'none';
        document.getElementById('tip').style.display = 'none';
        document.getElementById('date').style.display = 'none';
		document.getElementById('dev').style.display = 'none';
        document.getElementById('comp').style.display = 'none';
        document.getElementById('pds').style.display = 'none';
        document.getElementById('diam').style.display = 'none';
		document.getElementById('ep').style.display = 'none';
        document.getElementById('forme').style.display = 'none';
        document.getElementById('demo').style.display = 'none';
		document.getElementById('idr').style.display = 'none';
    }
    else if(document.getElementById('pds').checked)
    {
		'pds'.sort();
        document.getElementById('nbr_ex').style.display = 'none';
        document.getElementById('emet').style.display = 'none';
        document.getElementById('tip').style.display = 'none';
        document.getElementById('date').style.display = 'none';
		document.getElementById('dev').style.display = 'none';
        document.getElementById('comp').style.display = 'none';
        document.getElementById('pds').style.display = 'block';
        document.getElementById('diam').style.display = 'none';
		document.getElementById('ep').style.display = 'none';
        document.getElementById('forme').style.display = 'none';
        document.getElementById('demo').style.display = 'none';
		document.getElementById('idr').style.display = 'none';
    }
    else if(document.getElementById('tip').checked)
    {
        document.getElementById('#nbr_ex').style.display = 'none';
        document.getElementById('#emet').style.display = 'none';
        document.getElementById('#tip').style.display = 'block';
        document.getElementById('date').style.display = 'none';
		document.getElementById('dev').style.display = 'none';
        document.getElementById('comp').style.display = 'none';
        document.getElementById('pds').style.display = 'none';
        document.getElementById('diam').style.display = 'none';
		document.getElementById('ep').style.display = 'none';
        document.getElementById('forme').style.display = 'none';
        document.getElementById('demo').style.display = 'none';
		document.getElementById('idr').style.display = 'none';
        }
    else if(document.getElementById('date').checked)
    {
        document.getElementById('#nbr_ex').style.display = 'none';
        document.getElementById('#emet').style.display = 'none';
        document.getElementById('#tip').style.display = 'none';
        document.getElementById('date').style.display = 'block';
		document.getElementById('dev').style.display = 'none';
        document.getElementById('comp').style.display = 'none';
        document.getElementById('pds').style.display = 'none';
        document.getElementById('diam').style.display = 'none';
		document.getElementById('ep').style.display = 'none';
        document.getElementById('forme').style.display = 'none';
        document.getElementById('demo').style.display = 'none';
		document.getElementById('idr').style.display = 'none';
    }
}

