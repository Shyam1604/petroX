$.log = function(message){
  var $logger = $("#logger");
  $logger.html($logger.html() + "\n * " + message );
}


$(function(){
        var options = {
          map: "#map",
			 location: "Cape Town"
        };
        
        $("#geocomplete").geocomplete(options).bind("geocode:result", function(event, result){
            $.log("Result: " + result.formatted_address);
          })
          .bind("geocode:error", function(event, status){
            $.log("ERROR: " + status);
          })
          .bind("geocode:multiple", function(event, results){
            $.log("Multiple: " + results.length + " results found");
          });
        
        $("#find").click(function(){
          $("#geocomplete").trigger("geocode");
        });
		  
		  var options = {
          map: "#mapTwo",
			 location: "Melbourne"
        };
		  $("#geosearch").geocomplete(options).bind("geocode:result", function(event, result){
            $.log("Result: " + result.formatted_address);
          })
          .bind("geocode:error", function(event, status){
            $.log("ERROR: " + status);
          })
          .bind("geocode:multiple", function(event, results){
            $.log("Multiple: " + results.length + " results found");
          });
        
        $("#findTwo").click(function(){
          $("#geosearch").trigger("geocode");
        });
        
      
        
      });

// Get the user's current location
function getCurrentLocation() {
  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
          var userLocation = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
          };
          var map = new google.maps.Map(document.getElementById('map'), {
              center: userLocation,
              zoom: 15
          });
          var marker = new google.maps.Marker({
              position: userLocation,
              map: map,
              draggable: true
          });
      });
  } else {
      alert('Geolocation is not supported by this browser.');
  }
}
// Function to handle reorder button click
function reorder(orderId) {
  // Perform reorder action, for example:
  alert("Reorder clicked for order ID: " + orderId);
  // Implement your logic here to place the reorder
}