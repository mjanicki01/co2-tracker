const BASE_URL_LOCAL = "http://localhost:5000"
const BASE_URL_CLIMATIQ = "https://beta3.api.climatiq.io"
const AUTH_TOKEN = "301Y795S5PMYHAPY7X67D51WS7NB"

//axios.defaults.headers.common["X-CSRFToken"] = "{{ csrf_token() }}";

const e_id1 = "consumer_goods-type_clothing";
const e_id2 = "passenger_vehicle-vehicle_type_motorcycle-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na";
const e_id3 = "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na";
const e_id4 = "consumer_goods-type_clothing";

var clothing = {
  e_id: "consumer_goods-type_clothing",
  param1: "money",
  param2_unitlabel: "money_unit",
  param2_unit: "usd",
  activity_id: "clothing"
}

const driving = {
  e_id: '',
  param1: '',
  param2: '',
  activity_id: ''
}

const bottle = {
  e_id: '',
  param1: '',
  param2: '',
  activity_id: ''
}


// $("form").on("submit", async function(evt) {
//     evt.preventDefault();
//   // todo: add form validation handling
//     let category = evt.target.id
//     console.log(category)
//     console.log(category.e_id)
//     console.log(clothing.e_id)

//     let user_id = 3 //parseInt($("#user_id").val());
//     let spend_qty = parseInt($("#spend_qty").val());
//     let date = $("#date").val();
  
//     const resp = await axios.post(`${BASE_URL_CLIMATIQ}/estimate`, {
//       "emission_factor": `${category.e_id}`,
//         "parameters":
//           {
//           [`${category.param1}`]: spend_qty,
//           [`${category.param2_unitlabel}`]: `${category.param2_unit}`
//           }
//       },
//       {
//         headers: { "Authorization": `Bearer ${AUTH_TOKEN}` }
//       }
//     );
  
//     const co2e = resp.data["co2e"]
  
//     const newEvent = await axios.post(`${BASE_URL_LOCAL}/post-activity`, 
//       {
//         "user_id": user_id,
//         "activity_id": `${category.activity_id}`,
//         "e_id": `${category.e_id}`,
//         "date": date,
//         "spend_qty": spend_qty,
//         "spend_unit": `${category.param1_unit}`,
//         "co2e": co2e,
//         "from": "",
//         "to": ""
//       });
  
//     $("form").trigger("reset");
//   })







$("#form-clth").on("submit", async function(evt) {
    evt.preventDefault();
  // todo: add form validation handling
  
    let user_id = 3 //parseInt($("#user_id").val());
    let spend_qty = parseInt($("#spend_qty").val());
    let date = $("#date").val();
  
    const resp = await axios.post(`${BASE_URL_CLIMATIQ}/estimate`, {
      "emission_factor": e_id1,
        "parameters":
          {
          "money": spend_qty,
          "money_unit": "usd"
          }
      },
      {
        headers: { "Authorization": `Bearer ${AUTH_TOKEN}` }
      }
    );
  
    const co2e = resp.data["co2e"]
  
    const newEvent = await axios.post(`${BASE_URL_LOCAL}/post-activity`, 
      {
        "user_id": user_id,
        "activity_id": "clothing",
        "e_id": e_id1,
        "date": date,
        "spend_qty": spend_qty,
        "spend_unit": "usd",
        "co2e": co2e,
        "from": "",
        "to": ""
      });
  
    $("#form-clth").trigger("reset");
}),


$("#form-distance").on("submit", async function(evt) {
    evt.preventDefault();
  // todo: add form validation handling
  
    let user_id = 3 //parseInt($("#user_id").val());
    let spend_qty = parseInt($("#spend_qty").val());
    let date = $("#date").val();
  
    const resp = await axios.post(`${BASE_URL_CLIMATIQ}/estimate`, {
      "emission_factor": e_id2,
        "parameters":
          {
          "distance": spend_qty,
          "distance_unit": "mi" //might be something else
          }
      },
      {
        headers: { "Authorization": `Bearer ${AUTH_TOKEN}` }
      }
    );
  
    const co2e = resp.data["co2e"]
  
    const newEvent = await axios.post(`${BASE_URL_LOCAL}/post-activity`, 
      {
        "user_id": user_id,
        "activity_id": "driving",
        "e_id": e_id2,
        "date": date,
        "spend_qty": spend_qty,
        "spend_unit": "mi",
        "co2e": co2e,
        "from": "",
        "to": ""
      });
  
      $("#form-distance").trigger("reset");
}),


$("#form-airtravel").on("submit", async function(evt) {
    evt.preventDefault();
  // todo: add form validation handling
  
    let user_id = 3 //parseInt($("#user_id").val());
    let from = $("#from").val();
    let to = $("#to").val();
    let date = $("#date").val();
  
    const resp = await axios.post(`${BASE_URL_CLIMATIQ}/travel/flights`, {
      "emission_factor": e_id3,
        "legs": [
            {
          "from": from,
          "to": to
            }
        ]
      },
      {
        headers: { "Authorization": `Bearer ${AUTH_TOKEN}` }
      }
    );
  
    const co2e = resp.data["co2e"]
  
    const newEvent = await axios.post(`${BASE_URL_LOCAL}/post-activity`, 
      {
        "user_id": user_id3,
        "e_id": e_id,
        "date": date,
        "spend_qty": "",
        "spend_unit": "",
        "co2e": co2e,
        "from": from,
        "to": to
      });
  
      $("#form-airtravel").trigger("reset");
}),


$("#form-btl").on("submit", async function(evt) {
    evt.preventDefault();
  // todo: add form validation handling
  
    let user_id = 3 //parseInt($("#user_id").val());
    let spend_qty = parseInt($("#spend_qty").val());
    let date = $("#date").val();
  
    const resp = await axios.post(`${BASE_URL_CLIMATIQ}/estimate`, {
      "emission_factor": e_id4,
        "parameters":
          {
          "money": spend_qty,
          "money_unit": "usd"
          }
      },
      {
        headers: { "Authorization": `Bearer ${AUTH_TOKEN}` }
      }
    );
  
    const co2e = resp.data["co2e"]
  
    const newEvent = await axios.post(`${BASE_URL_LOCAL}/post-activity`, 
      {
        "user_id": user_id,
        "e_id": e_id4,
        "date": date,
        "spend_qty": spend_qty,
        "spend_unit": "usd",
        "co2e": co2e,
        "from": "",
        "to": ""
      });
  
      $("#form-btl").trigger("reset");
})