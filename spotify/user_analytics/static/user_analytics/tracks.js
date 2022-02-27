let track_short = document.getElementById('track-data-past-month');
let track_medium = document.getElementById('track-data-past-sixmonth');
let track_long = document.getElementById('track-data-all-time');

track_medium.style.display = "none";
track_long.style.display = "none";

function pastMonth(){
	if (track_short.style.display === "none") {
		track_short.style.display = "block";
		track_medium.style.display = "none";
		track_long.style.display = "none";
	}
}

function pastSixMonth(){
	if (track_medium.style.display === "none") {
		track_short.style.display = "none";
		track_medium.style.display = "block";
		track_long.style.display = "none";
	}
}

function allTime(){
	if (track_long.style.display === "none") {
		track_short.style.display = "none";
		track_medium.style.display = "none";
		track_long.style.display = "block";
	}
}
