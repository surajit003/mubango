$(document).on('ready', function(){

	//------- Google Maps ---------//

	// Creating a LatLng object containing the coordinate for the center of the map
	var latlng = new google.maps.LatLng(53.385846,-1.471385);

	// Creating an object literal containing the properties we want to pass to the map
	var options = {
		zoom: 15, // This number can be set to define the initial zoom level of the map
		center: latlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP // This value can be set to define the map type ROADMAP/SATELLITE/HYBRID/TERRAIN
	};
	// Calling the constructor, thereby initializing the map
	var map = new google.maps.Map(document.getElementById('map_div'), options);

	// Define Marker properties
	var image = new google.maps.MarkerImage('images/pin1.png',
		new google.maps.Size(64, 64),
		new google.maps.Point(0,0),
		new google.maps.Point(0, 0)
	);

	// Define Marker properties
	var image2 = new google.maps.MarkerImage('images/pin2.png',
		new google.maps.Size(64, 64),
		new google.maps.Point(0,0),
		new google.maps.Point(0, 0)
	);

	// Define Marker properties
	var image3 = new google.maps.MarkerImage('images/pin3.png',
		new google.maps.Size(64, 64),
		new google.maps.Point(0,0),
		new google.maps.Point(0, 0)
	);

	// Define Marker properties
	var image4 = new google.maps.MarkerImage('images/pin4.png',
		new google.maps.Size(64, 64),
		new google.maps.Point(0,0),
		new google.maps.Point(0, 0)
	);

	// Define Marker properties
	var image5 = new google.maps.MarkerImage('images/pin5.png',
		new google.maps.Size(64, 64),
		new google.maps.Point(0,0),
		new google.maps.Point(0, 0)
	);


	// Add Marker
	var marker1 = new google.maps.Marker({
		position: new google.maps.LatLng(53.385846,-1.471385),
		map: map,
		icon: image // This path is the custom pin to be shown. Remove this line and the proceeding comma to use default pin
	});

	// Add Marker
	var marker2 = new google.maps.Marker({
		position: new google.maps.LatLng(53.389000,-1.473000),
		map: map,
		icon: image2 // This path is the custom pin to be shown. Remove this line and the proceeding comma to use default pin
	});

	// Add Marker
	var marker3 = new google.maps.Marker({
		position: new google.maps.LatLng(53.381000,-1.471000),
		map: map,
		icon: image3 // This path is the custom pin to be shown. Remove this line and the proceeding comma to use default pin
	});

	// Add Marker
	var marker4 = new google.maps.Marker({
		position: new google.maps.LatLng(53.391000,-1.480000),
		map: map,
		icon: image4 // This path is the custom pin to be shown. Remove this line and the proceeding comma to use default pin
	});

	// Add Marker
	var marker5 = new google.maps.Marker({
		position: new google.maps.LatLng(53.385000,-1.490000),
		map: map,
		icon: image5 // This path is the custom pin to be shown. Remove this line and the proceeding comma to use default pin
	});

	// Add listener for a click on the pin
	google.maps.event.addListener(marker1, 'click', function() {
		infowindow1.open(map, marker1);
		$('body .infowindow').parent().parent().parent().parent().parent().parent().addClass('custom-tooltip')
	});

	// Add listener for a click on the pin
	google.maps.event.addListener(marker2, 'click', function() {
		infowindow2.open(map, marker2);
		$('body .infowindow').parent().parent().parent().parent().parent().parent().addClass('custom-tooltip')
	});

	// Add listener for a click on the pin
	google.maps.event.addListener(marker3, 'click', function() {
		infowindow3.open(map, marker3);
		$('body .infowindow').parent().parent().parent().parent().parent().parent().addClass('custom-tooltip')
	});

	// Add listener for a click on the pin
	google.maps.event.addListener(marker4, 'click', function() {
		infowindow4.open(map, marker4);
		$('body .infowindow').parent().parent().parent().parent().parent().parent().addClass('custom-tooltip')
	});

	// Add listener for a click on the pin
	google.maps.event.addListener(marker5, 'click', function() {
		infowindow5.open(map, marker5);
		$('body .infowindow').parent().parent().parent().parent().parent().parent().addClass('custom-tooltip')
	});

	// Add information window
	var infowindow1 = new google.maps.InfoWindow({
		content:  createInfo('<div class="ml-box"> <div class="ml-thumb"><img src="images/resource/ml1.jpg" alt="" /><span>Open</span><h6><i class="flaticon-phone-call"></i>+ 44 20 456 823</h6></div> <div class="ml-title"> <h3><a href="#" title="">Liberty Club</a></h3><div class="placedetails"> <span class="pull-left"><i class="flaticon-pin"></i>Roma, Italy</span> </div> <ul class="listmetas"> <li><span class="rated">3.5</span>3 Ratings</li> </ul></div></div>')
	});

	// Add information window
	var infowindow2 = new google.maps.InfoWindow({
		content:  createInfo('<div class="ml-box"> <div class="ml-thumb"><img src="images/resource/ml1.jpg" alt="" /><span>Open</span><h6><i class="flaticon-phone-call"></i>+ 44 20 456 823</h6></div> <div class="ml-title"> <h3><a href="#" title="">Liberty Club</a></h3><div class="placedetails"> <span class="pull-left"><i class="flaticon-pin"></i>Roma, Italy</span> </div> <ul class="listmetas"> <li><span class="rated">3.5</span>3 Ratings</li> </ul></div></div>')
	});

	// Add information window
	var infowindow3 = new google.maps.InfoWindow({
		content:  createInfo('<div class="ml-box"> <div class="ml-thumb"><img src="images/resource/ml1.jpg" alt="" /><span>Open</span><h6><i class="flaticon-phone-call"></i>+ 44 20 456 823</h6></div> <div class="ml-title"> <h3><a href="#" title="">Liberty Club</a></h3><div class="placedetails"> <span class="pull-left"><i class="flaticon-pin"></i>Roma, Italy</span> </div> <ul class="listmetas"> <li><span class="rated">3.5</span>3 Ratings</li> </ul></div></div>')
	});

	// Add information window
	var infowindow4 = new google.maps.InfoWindow({
		content:  createInfo('<div class="ml-box"> <div class="ml-thumb"><img src="images/resource/ml1.jpg" alt="" /><span>Open</span><h6><i class="flaticon-phone-call"></i>+ 44 20 456 823</h6></div> <div class="ml-title"> <h3><a href="#" title="">Liberty Club</a></h3><div class="placedetails"> <span class="pull-left"><i class="flaticon-pin"></i>Roma, Italy</span> </div> <ul class="listmetas"> <li><span class="rated">3.5</span>3 Ratings</li> </ul></div></div>')
	});

	// Add information window
	var infowindow5 = new google.maps.InfoWindow({
		content:  createInfo('<div class="ml-box"> <div class="ml-thumb"><img src="images/resource/ml1.jpg" alt="" /><span>Open</span><h6><i class="flaticon-phone-call"></i>+ 44 20 456 823</h6></div> <div class="ml-title"> <h3><a href="#" title="">Liberty Club</a></h3><div class="placedetails"> <span class="pull-left"><i class="flaticon-pin"></i>Roma, Italy</span> </div> <ul class="listmetas"> <li><span class="rated">3.5</span>3 Ratings</li> </ul></div></div>')
	});

	// Create information window
	function createInfo(title, content) {
		return '<div class="infowindow"><span>'+ title +'</span>'+content+'</div>';
	}

});
