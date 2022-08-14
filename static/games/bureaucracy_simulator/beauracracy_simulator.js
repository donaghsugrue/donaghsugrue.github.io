///////////////////////////////
///////////////////////////////
// Beauracracy Simulator 1.0 //
///////////////////////////////
///////////////////////////////


let canvas;
let context;

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();


document.addEventListener("DOMContentLoaded", init, false);


function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);

    snake();
}


// Have it so that the player moves toward the screen click on screen click
// When they arrive at the point of the screen click they should stop
function player_move(event) {
    let changeX = event.clientX;
    let changeY = event.clientY;
}



function timer() {
    let full_day = 8 * 60 * 60 * 1000 ; // working hours * minutes in an hour * seconds in a minute * milliseconds in a second
}


function opponent() {
    return
}

function comput





// if player makes contact w another employee, they'll be dragged into another 

// Pop up "you haven't procrastinated in a while, maybe head back to your computer?" <-- kills 30 mins

// Life bar called "attention span"
//      - If it drops to zero, you lose control and the player moves back to computer / home, this kills 30 mins
//      - toilet break / coffee break replenish attention
//      - 


replenished

// The "twist" is that you're working for private industry, not public sector. NOOOOOOOOOO!