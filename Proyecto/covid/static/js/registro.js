$("#registro .1-1 .siguiente").click(function(){

    var nombre = $("#registro #nombre").val();
    var apellido = $("#registro #apellido").val();
    var email = $("#registro #email").val();
    var numero = $("#registro #numero").val();

    if(nombre != "" && apellido != "" && email != "" && numero != ""){
        $("#registro .1-1").addClass('noDisplay');
        $("#registro .1-2").removeClass('noDisplay');
    }else{
        alert("Por favor, rellenar todos los campos");
    }

})

$("#registro .1-2 .volver").click(function(){
    $("#registro .1-2").addClass('noDisplay');
    $("#registro .1-1").removeClass('noDisplay');
})

$("#registro .1-2 .siguiente").click(function(){
    alert("Registro")
})

$(".info").mouseover(function(){
    $(".info div").removeClass("noDisplay");
})

$(".info").mouseout(function(){
    $(".info div").addClass("noDisplay");
})