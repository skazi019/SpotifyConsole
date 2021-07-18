let artist_short = document.getElementById('artists-data-past-month');
let artist_medium = document.getElementById('artists-data-past-sixmonth');
let artist_long = document.getElementById('artists-data-all-time');

artist_medium.style.display = "none";
artist_long.style.display = "none";

function pastMonth(){
	if (artist_short.style.display === "none") {
		artist_short.style.display = "flex";
		artist_medium.style.display = "none";
		artist_long.style.display = "none";
	}
}

function pastSixMonth(){
	if (artist_medium.style.display === "none") {
		artist_short.style.display = "none";
		artist_medium.style.display = "flex";
		artist_long.style.display = "none";
	}
}

function allTime(){
	if (artist_long.style.display === "none") {
		artist_short.style.display = "none";
		artist_medium.style.display = "none";
		artist_long.style.display = "flex";
	}
}
