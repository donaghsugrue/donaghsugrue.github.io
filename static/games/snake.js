// create canvas and context variables
let canvas;
let context;

// setting variable for calling to cancel the animation
let request_id;

// create time interval variables
let fpsInterval = 1000 / 30;
let now;
let then = Date.now();

// object to store apple variables 
let apple = {
    x               :   0,
    y               :   0,
    size            :   10
};

// object to store player variables
let player = {
    x               :   0,
    y               :   0,
    size            :   10,
    body_length     :   0
};

let body = [];

// Movement boolean variables
let moveLeft = false;
let moveUp = false;
let moveRight = false;
let moveDown = false;

// allowing the player to pause the game at any time by pressing p
let pause = false;

// tag variables for printing info to the user
let score_tag = document.getElementById("score");

// Event listener, when page is loaded run init
document.addEventListener("DOMContentLoaded", init, false);



// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //



// Initialise function
function init() {

    // select canvas from 
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    // reset the players variables
    player.x = (canvas.width / 2) - (player.size / 2);
    player.y = (canvas.height / 2) - (player.size / 2);
    // player.size = canvas.size / 50

    // reset the apple variables
    // apple.size = player.size
    apple_reset();

    // create event listeners from keystrokes
    window.addEventListener("keydown", activate, false);
    // window.addEventListener("keyup", deactivate, false);

    // Call the snake function to draw
    snake();

};



function snake() {

    // // // // // FRAME SETUP // // // // // 

    // repeat the snake function to animate it
    request_id = window.requestAnimationFrame(snake);

    // set frame rate
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
       return;
    }
    then = now - (elapsed % fpsInterval);

    // clear the previous frame
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Update the score display every frame
    score_tag.innerHTML = "Score: " + player.body_length;





    // // // // // BACKGROUND // // // // //

    context.fillStyle = "black";
    context.fillRect(0, 0, canvas.width, canvas.height);





    // // // // // SNAKE // // // // //

    // Draw the head
    context.fillStyle = "green";
    context.fillRect(player.x, player.y, player.size, player.size);

    // player movement parameters (Releasing the arrow key should do nothing)
    if (pause === false) {
        if (moveLeft) {
            player.x = player.x - player.size;
        }
        if (moveRight) {
            player.x = player.x + player.size;
        }
        if (moveUp) {
            player.y = player.y - player.size;
        }
        if (moveDown) {
            player.y = player.y + player.size;
        }
    };





    // // // // // // BODY // // // // //

    // // For every entry in body, create another rectangle behind where the head is
    // for (let cell of body) {
    //     context.fillStyle = "cyan";
    //     context.fillRect(cell.x, cell.y, cell.size, cell.size);  
    // };

    // // After drawing here we want to change the x and y of each cell to the body to the x and y of the previous one so that the next frame animates them as a tail
    // for (let i = player.body_length; i > -1; i--) {
        
    //     if (i != 0) {
    //         // last index xy should be changed to second last index' xy, second last index xy should be changed to 3rd last index xy, etc.
    //         body[i].x = body[i - 1].x
    //         body[i].y = body[i - 1].y;

    //     } else if (i === 0) {
    //         // 0 index xy should be changed to player.x and player.y
    //         body[0].x = player.x;
    //         body[0].y = player.y;
    //     };

    // };

    // for (let i = 0; i< player.body_length; i++) {
    //     context.fillStyle = "cyan";
    //     context.fillRect(player.x, player.y, player.size, player.size);
    // }





    // // // // // APPLES // // // // //

    // draw apple on canvas
    context.fillStyle = "red";
    context.fillRect(apple.x, apple.y, apple.size, apple.size);





    // // // // // COLLISIONS // // // // //

    // Colliding with the outer wall <--- not working, assuming it's the game_over function that's
    if (player.x === 0 || player.x + player.size === canvas.width || player.y === 0 || player.y + player.size === canvas.height) {
        game_over();
    };

    // Colliding with an Apple 
    if (collision(apple)) {
        apple_reset();

        // body_grow(); // <--- Not working. Body length # is increasing, but code is then freezing.
    };

    // Colliding with the body of the snake
    for (let cell of body) {
        if (collision(cell)) {
            game_over();
        }
    };

};





// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //





// // // // // RANDOM INTEGER // // // // //

function randint(min, max) {

    return Math.round(Math.random() * (max - min)) + min;

};



// // // // // KEYSTROKES // // // // //

function activate(event) {

    let key = event.key;

    if(key === "ArrowLeft") {
        moveLeft = true;
        moveUp = false;
        moveDown = false;
        moveRight = false;
    } else if (key === "ArrowUp") {
        moveLeft = false
        moveUp = true;
        moveDown = false;
        moveRight = false;
    } else if (key === "ArrowDown") {
        moveLeft = false;
        moveUp = false;
        moveDown = true;
        moveRight = false;
    } else if (key === "ArrowRight") {
        moveLeft = false;
        moveUp = false;
        moveDown = false;
        moveRight = true;
    };

    if (key === "p") {
        if (pause === true) {
            pause = false;
        } else if (pause === false) {
            pause = true;
        }
    };

};

// // Deactivation for if key is lifted, keeping this just for testing purposes.
// function deactivate(event) {

//     let key = event.key;

//     if(key === "ArrowLeft") {
//         moveLeft = false;
//     } else if (key === "ArrowUp") {
//         moveUp = false;
//     } else if (key === "ArrowDown") {
//         moveDown = false;
//     } else if (key === "ArrowRight") {
//         moveRight = false;
//     }

// };



// // // // // GAME OVER // // // // //

function game_over() {

    // remove events
    window.removeEventListener("keydown", activate, false);
    window.removeEventListener("keyup", deactivate, false);

    // stop animating
    window.cancelAnimationFrame(request_id);

    // notify player of score and that they've lost
    window.alert("You Lose!");

    return;

};



// // // // // COLLISIONS // // // // // <--- Not working

function collision(obstacle) {

    if (player.x + player.size < obstacle.x ||
        obstacle.x + obstacle.size < player.x ||
        player.y > obstacle.y + obstacle.size ||
        obstacle.y > player.y + player.size) {
            return false;
    } else {
            return true;
    }

};



// // // // // RESET APPLE LOCATION // // // // //

function apple_reset() {

    apple.x = (randint(0, canvas.width/10)) * 10;
    apple.y = (randint(0, canvas.height/10)) * 10;

};



// // // // // GROW SNAKES BODY // // // // //

function body_grow() {

    // if this function has been called, then the snake has eaten an apple and needs to be one cell longer
    player.body_length += 1;

    // put the cell's location on the player's x and y. It will be reset during the next frame anyway, so this is just to mask it so that it's unseen.
    let cell = {
        x       : player.x,
        y       : player.y,
        size    : player.size
    };

    // push to out list so that we can call it during the next frame
    body.push(cell);

};