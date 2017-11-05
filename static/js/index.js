function onPlayGameClicked(e) {
  e.preventDefault();
    var x = document.getElementById("hidden");
    if (x.style.display === "none") {
        x.style.display = "block";
        setTimeout(function(){
          $('html, body').animate({ scrollTop: $("#hidden").offset().top}, 'slow');
        }, 200);
    } else {
        x.style.display = "none";
    }
    var x = document.getElementById("section01");
    if (x.style.display === "none") {
        x.style.display = "block";

    } else {
        x.style.display = "none";

    }
    // HIiiii
}

$("#play_game_btn").on('click', onPlayGameClicked);
