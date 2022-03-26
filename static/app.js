

function filterTable() {
// allow user to filter based on click events (buttons)
// HTML will have nav bar with filter buttons: All, Clth, Flights, Driving, Bottles
}


// $(window).on("load", function() {
//   $("#form-clth").hide();
//   $("#form-drv").hide();
//   $("#form-air").hide();
//   $("#form-btl").hide();
// })

$("#clth").on("click", async function() {
  $("#form-clth").show();
  $("#form-drv").hide();
  $("#form-air").hide();
  $("#form-btl").hide();
})

$("#btl").on("click", async function() {
  $("#form-btl").show();
  $("#form-clth").hide();
  $("#form-drv").hide();
  $("#form-air").hide();
})

$("#air").on("click", async function() {
  $("#form-air").show();
  $("#form-clth").hide();
  $("#form-drv").hide();
  $("#form-btl").hide();
})

$("#drv").on("click", async function() {
  $("#form-drv").show();
  $("#form-clth").hide();
  $("#form-air").hide();
  $("#form-btl").hide();
})




