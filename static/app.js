
// Activity forms

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

// About page sections
$("#impact-btn").on("click", async function() {
  $("#impact").show();
  $("#numbers").hide();
  $("#goals").hide();
  $("#tools").hide();
  $("#credit").hide();
})

$("#numbers-btn").on("click", async function() {
  $("#impact").hide();
  $("#numbers").show();
  $("#goals").hide();
  $("#tools").hide();
  $("#credit").hide();
})

$("#goals-btn").on("click", async function() {
  $("#impact").hide();
  $("#numbers").hide();
  $("#goals").show();
  $("#tools").hide();
  $("#credit").hide();
})

$("#tools-btn").on("click", async function() {
  $("#impact").hide();
  $("#numbers").hide();
  $("#goals").hide();
  $("#tools").show();
  $("#credit").hide();
})

$("#credit-btn").on("click", async function() {
  $("#impact").hide();
  $("#numbers").hide();
  $("#goals").hide();
  $("#tools").hide();
  $("#credit").show();
})