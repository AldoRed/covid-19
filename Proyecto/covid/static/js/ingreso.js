$("#ingreso .siguiente").click(function(){
    var correo = $("#email").val()
    alert(correo);
})

$(".info").mouseover(function(){
    $(".info div").removeClass("noDisplay");
})

$(".info").mouseout(function(){
    $(".info div").addClass("noDisplay");
})