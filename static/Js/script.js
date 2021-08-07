addnew = document.getElementById("add");
addnewDiv = document.getElementById("newpost");

$("#newpost").hide();

$("#add").click(function(){
    $("#newpost").fadeToggle("slow");
    console.log("here")
  });