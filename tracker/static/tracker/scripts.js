function toggleOdds(value){
    
    if (value=="SPT") {
        document.getElementById("odds_field").style.display = "block";
        document.getElementById("odds_input").value = "";
    } else {
        document.getElementById("odds_field").style.display = "none";
        document.getElementById("odds_input").value = "";
        
    }
}

function toggleProfit(value){
    
    if (value=="False") {
        document.getElementById("profit_field").style.display = "none";
        document.getElementById("profit_input").value = "";
    } else {
        document.getElementById("profit_field").style.display = "block";
        document.getElementById("profit_input").value = "";
    }
}

