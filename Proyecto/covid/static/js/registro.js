$("#registro .1-1 .siguiente").click(function(){
    $("#registro .1-1").addClass('noDisplay');
    $("#registro .1-2").removeClass('noDisplay');
})

$("#registro .1-2 .volver").click(function(){
    $("#registro .1-2").addClass('noDisplay');
    $("#registro .1-1").removeClass('noDisplay');
})

$("#registro .1-2 .siguiente").click(function(){
    alert("Registro")
})