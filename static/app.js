

function filterTable() {
// allow user to filter based on click events (buttons)
// HTML will have nav bar with filter buttons: All, Clth, Flights, Driving, Bottles
}


$(window).on("load", function() {
  $("#form-clth").hide();
  $("#form-distance").hide();
  $("#form-airtravel").hide();
  $("#form-btl").hide();
})

$("#clth").on("click", async function() {
  $("#form-clth").show();
  $("#form-distance").hide();
  $("#form-airtravel").hide();
  $("#form-btl").hide();
})

$("#btl").on("click", async function() {
  $("#form-btl").show();
  $("#form-clth").hide();
  $("#form-distance").hide();
  $("#form-airtravel").hide();
})

$("#air").on("click", async function() {
  $("#form-airtravel").show();
  $("#form-clth").hide();
  $("#form-distance").hide();
  $("#form-btl").hide();
})

$("#road").on("click", async function() {
  $("#form-distance").show();
  $("#form-clth").hide();
  $("#form-airtravel").hide();
  $("#form-btl").hide();
})




