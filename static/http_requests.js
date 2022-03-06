const BASE_URL = "http://localhost:5000"
const ENDPOINT_URL = "https://beta3.api.climatiq.io/estimate"
const AUTH_TOKEN = "301Y795S5PMYHAPY7X67D51WS7NB"



$("#form-clth").on("submit", async function(evt) {
    evt.preventDefault();
  // todo: add form validation handling
  
    const e_id = "consumer_goods-type_clothing";
  
    let user_id = 3 //parseInt($("#user_id").val());
    let spend_qty = parseInt($("#spend_qty").val());
    let date = $("#date").val();
  
    const resp = await axios.post(ENDPOINT_URL, {
      "emission_factor": e_id,
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
  
    const newEvent = await axios.post(`${BASE_URL}/postactivity`, 
      {
        "user_id": user_id,
        "e_id": e_id,
        "date": date,
        "spend_qty": spend_qty,
        "spend_unit": "usd",
        "co2e": co2e,
        "leg_1": "",
        "leg_2": ""
      });
  
      $("#form-clth").trigger("reset");
  })