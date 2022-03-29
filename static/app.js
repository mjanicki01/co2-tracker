
// Sort table

$("tr > td").each(function(thead) {
    $(this).on("click", function() {

      let type = $(this).data("type");
      let rows = $("table").find("tbody > tr");

        rows.sort(function(a, b) {
          let cell1 = $(a).children("td").eq(thead).text();
          let cell2 = $(b).children("td").eq(thead).text();
            if(type == "num"){
                cell1 *= 1;
                cell2 *= 1;
            }
          return (cell1 < cell2) ? -1 : (cell1 > cell2 ? 1 : 0)
        })
        $.each(rows, function(index, row) {
          $("tbody").append(row);
        })
    })
})



// Activity forms

$("#clth").on("click", () => {
    $("#form-clth").show();
    $("#form-drv").hide();
    $("#form-air").hide();
    $("#form-btl").hide();
  })

$("#btl").on("click", () => {
    $("#form-btl").show();
    $("#form-clth").hide();
    $("#form-drv").hide();
    $("#form-air").hide();
  })

$("#air").on("click", () => {
    $("#form-air").show();
    $("#form-clth").hide();
    $("#form-drv").hide();
    $("#form-btl").hide();
  })

$("#drv").on("click", () => {
    $("#form-drv").show();
    $("#form-clth").hide();
    $("#form-air").hide();
    $("#form-btl").hide();
  })


// About page sections
$("#impact-btn").on("click", () => {
    $("#impact").show();
    $("#numbers").hide();
    $("#goals").hide();
    $("#tools").hide();
    $("#credit").hide();
  })

$("#numbers-btn").on("click", () => {
    $("#impact").hide();
    $("#numbers").show();
    $("#goals").hide();
    $("#tools").hide();
    $("#credit").hide();
  })

$("#goals-btn").on("click", () => {
    $("#impact").hide();
    $("#numbers").hide();
    $("#goals").show();
    $("#tools").hide();
    $("#credit").hide();
  })

$("#tools-btn").on("click", () => {
    $("#impact").hide();
    $("#numbers").hide();
    $("#goals").hide();
    $("#tools").show();
    $("#credit").hide();
  })

$("#credit-btn").on("click", () => {
    $("#impact").hide();
    $("#numbers").hide();
    $("#goals").hide();
    $("#tools").hide();
    $("#credit").show();
  })