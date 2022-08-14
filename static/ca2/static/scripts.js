//////////////////////////////////////////////////////////////////////////////////////////
//                                                                                      //
//      SPECIAL FEATURES                                                                //
//      - The cheat code to make the game easier is: iwantnobaddies                     //
//          This will remove all enemies from the game                                  //
//      - Tileset & assets from here:                                                   //
//          https://0x72.itch.io/16x16-dungeon-tileset                                  //
//                                                                                      //
//////////////////////////////////////////////////////////////////////////////////////////       

// COMMENT
//////////// TO DO
// // // // // // // SECTION TITLE // // // // // // //
// // // SUB HEAD // // //



//////////// Sword swipe motion shouldn't work if E held down
//////////// Make music that loops throughout (changes per floor)
//////////// Make sounds & have these trigger
//////////// At the end of a game, if the user is logged in, their score could be stored in a database (using Ajax)
//////////// Server side component to save game (floor / room / player object) as necessary




// // // // // // // FUNCTION VARIABLES // // // // // // //

let canvas;
let context;

let request_id;

let xhttp;

let fpsInterval = 1000 / 30; // 30 fps
let now;
let then = Date.now();

let moveLeft = false;
let moveUp = false;
let moveRight = false;
let moveDown = false;

let margin = 50;

const nf = new Intl.NumberFormat ("en-UK", {
    minimumIntegerDigits: 2
});



// // // // // // // OBJECTS // // // // // // //

// // // PLAYER SPECIFIC // // //

// Design and parameters of the player
let playerImage = new Image();

let player = {
    x   :   500, // pull this, the y and the size from the image dimensions so that it auto calls an outline from the png???
    y   :   500,
    size:   50,
    speed : 10,
    maxHealth  : 100,
    health: 100,
    damage: 25,
    attack: false,
    complete: false
};





// // // GHOUL SPECIFIC // // //

//////////// Make sprites for ghoul
let ghoulSprite = new Image();

// Array container for ghouls
let ghouls = [];





// // // TREASURE SPECIFIC // // //

let chestSprite = new Image();

// Array container for chests
let chests = [];

// Available powerups that can be secured by picking up chests
let items = ["speed +20", "damage +20", "max health +20", "health restore", "score +5000"];





// // // GATE SPECIFIC // // //

// Design and parameters of the goal that the player needs to reach to progress
let gate = {
    x     :     0,
    y     :     0,
    xSize :     0,
    ySize :     0
};

let prevGate = {
    x     :     0,
    y     :     0,
    xSize :     0,
    ySize :     0
};





// // // OBSTACLE SPECIFIC // // //

let obstacleTile = new Image();

// Design and parameters of the obstacles in a room
let obstacle = [];





// // // WORLD DESIGN // // //

//////////// Make the tilesets differ slightly per floor
let insideTileSetG = new Image();
let insideTileSet1 = new Image();
let insideTileSet2 = new Image();
let insideTileSet3 = new Image();
let insideTileSet4 = new Image();

let outsideTileSet = new Image();

let treasureOpen = new Image();

let treasureClosed = new Image();





// // // // // // // EMPTY VARIABLES // // // // // // //

let cheat;
let cheat_error;
let form;

let level;
let room;
let floor;
let score;
let timeScore;
let noOfChests;
let noOfEnemies;
let noOfObstacles;
let killedGhouls; // When the player reaches the chamber on the 5th floor, they are told to retread their steps back to the entrance. When they leave, this variables # of ghouls are outside. The game is only complete when these ghouls are defeated.
let bounceSpeed;
let activeCheat;

let startTime = Math.floor(Date.now() / 1000);





// // // // // // // INITIALISE // // // // // // //

// Calls the init function when DOMContentLoaded is satisfied (on page load)
document.addEventListener("DOMContentLoaded", init, false);

// initialise function for the page
function init() {

    // cheatcode form
    cheat = document.querySelector("#cheat");
    cheat_error = document.querySelector("#cheat_error")
    form = document.querySelector("form");
    form.addEventListener("submit", cheatCode, false);

    // selects the canvas on our html page
    canvas = document.querySelector("canvas");

    // "picasso" fills the canvas
    context = canvas.getContext("2d");

    // listens for "keydown" and runs the activate function
    window.addEventListener("keydown", activate, false);
    // listens for "keyup" and runs the deactivate function
    window.addEventListener("keyup", deactivate, false);

    // grabs the tilesets for our world
    playerImage.src = "static/knight_sprite.png";
    ghoulSprite.src = "static/ghoul_sprite.png";
    chestSprite.src = "static/chest_sprite.png";

    insideTileSetG.src = "static/inside_tileG.jpg"; // Ground floor inside tiles
    insideTileSet1.src = "static/inside_tile1.jpg";
    insideTileSet2.src = "static/inside_tile2.jpg";
    insideTileSet3.src = "static/inside_tile3.jpg";
    insideTileSet4.src = "static/inside_tile4.jpg";

    outsideTileSet.src = "static/outside_tile.jpg";
    obstacleTile.src = "static/obstacle_tile.png";
    treasureClosed.src = "static/treasure_closed.png";
    treasureOpen.src = "static/treasure_open.png";

    // // grabs the audio for our world
    // document.querySelector("audio").play();

    // initialises some of our blank variables
    level = 0;
    room = 0;
    floor = 0;
    score = 0;
    noOfEnemies = 0;

    // Calling a function to fill in gate object details upon init
    levelProgress(room);

    noOfChests = 0;
    noOfObstacles = 0;

    // calls our game function within the canvas
    draw();

};



// // // // // // // GAME CODE // // // // // // //

function draw() {

    // repeats the function every few milliseconds to animate it
    request_id = window.requestAnimationFrame(draw);

    // prevents pc's from getting overloaded. Keeps the code at 30fps
    // if the duration between now and then is less than 1 fps then wait a second
    // so as to not have things animate before page is loaded.
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
       return;
    }
    then = now - (elapsed % fpsInterval);

    // creating a Timer for scoring purposes
    timeScore = (Math.floor(Date.now() / 1000)) - startTime;

    // Creating a Timer for display purposes
    let timeSeconds = Math.floor(Date.now() / 1000);
    let elapsedSeconds = timeSeconds - startTime;
    for (let i = Math.floor(elapsedSeconds / 60); i > 0; i -= 1) {
        elapsedSeconds -= 60;
    };

    let elapsedMinutes = Math.floor(((Date.now() / 1000) - startTime) / 60);
    for (let i = Math.floor(elapsedMinutes / 60); i > 0; i -= 1) {
        elapsedMinutes -= 60;
    };

    let elapsedHours = Math.floor((((Math.floor(Date.now() / 1000)) - startTime) / 60) / 60);
    document.querySelector("#timer").innerHTML = elapsedHours + ":" + nf.format(elapsedMinutes) + "'" + nf.format(elapsedSeconds) + '"';

    // Creating a score display
    document.querySelector("#score").innerHTML = "Score : " + score;

    // Creating a display of what room and floor we're on
    document.querySelector("#room").innerHTML = "Room# : " + room;
    document.querySelector("#floor").innerHTML = "Floor# : " + floor;

    // clears previous canvas frame so that we aren't animating over previous frames  
    context.clearRect(0, 0, canvas.width, canvas.height);

    // draws background of canvas
    if (room === 0) {
        context.drawImage(outsideTileSet, 0, 0);

    } else if (room != 0) {
        if (floor === 0) {
            context.drawImage(insideTileSetG, 0, 0);
        } else if (floor === 1) {
            context.drawImage(insideTileSet1, 0, 0);
        } else if (floor === 2) {
            context.drawImage(insideTileSet2, 0, 0);
        } else if (floor === 3) {
            context.drawImage(insideTileSet3, 0, 0);
        } else if (floor === 4) {
            context.drawImage(insideTileSet4, 0, 0);
        }
        
    };
    //////////// Make the tilesets differ slightly per floor
    


    
    // // // // // // // OBSTACLES // // // // // // //
    if (obstacle.length < noOfObstacles) {
        let o = {
            x           : (randint(2, 8))*100, // doing it like this to control the randomness of the location a bit
            y           : (randint(2, 8))*100,
            size        : margin * 2
        };
        obstacle.push(o);
    };

    // drawing the obstacles
    for (let o of obstacle) {
        context.drawImage(obstacleTile, o.x, o.y);
    };

    // create an invisible wall to keep character off obstacles
    for (let o of obstacle) {
        if (playerCollides(o)) {
            player.x -= player.speed;
        };
        if (playerCollides(o)) {
            player.y -= player.speed;
        };
        if (playerCollides(o)) {
            player.x += player.speed;
        };
        if (playerCollides(o)) {
            player.ye += player.speed;
        };
    };

    if (player.y <= (margin * 0.75)) { // the same for the margins
        player.y += player.speed;
    } else if (player.x <= (margin * 0.75)) {
        player.x += player.speed;
    } else if (player.y + player.size >= canvas.height - (margin * 0.75)) {
        player.y -= player.speed;
    } else if (player.x + player.size >= canvas.width - (margin * 0.75)) {
        player.x -= player.speed;
    }



    // // // // // // // KNIGHT // // // // // // //
    // drawing the knight
    context.drawImage(playerImage, player.x - (player.size / 2), player.y - (player.size / 2));

    // drawing the knight's hit bar
    context.strokeStyle = "black";
    context.strokeRect(player.x - (player.maxHealth / 2), player.y + margin, player.maxHealth, (margin / 2));

    if (player.health > 50) {
        context.fillStyle = "green";
        context.fillRect(player.x - (player.maxHealth / 2), player.y + margin, player.health, (margin / 2));

    } else if (player.health > 20) {
        context.fillStyle = "orange";
        context.fillRect(player.x - (player.maxHealth / 2), player.y + margin, player.health, (margin / 2));

    } else if (player.health > 0) {
        context.fillStyle = "red";
        context.fillRect(player.x - (player.maxHealth / 2), player.y + margin, player.health, (margin / 2));
    };



    // // // // // // // GHOULS // // // // // // //
    // Figuring out how many ghouls to draw (increases based on # of levels completed)
    // if (activeCheat == true) {
        if (ghouls.length < noOfEnemies) {
            let g = {
                x           : (randint(1, 9))*100, // doing it like this to control the randomness of the location a bit
                y           : (randint(1, 9))*100,
                size        : 50,
                health      : 100,
                maxHealth   : 100,
                speed       : 8,
                alert       : false
            };
            ghouls.push(g);
        };
    
        // drawing the ghouls
        if (room != 6) {
            for (let g of ghouls) {
                context.drawImage(ghoulSprite, g.x - (g.size / 2), g.y - (g.size / 2));

                // drawing the ghoul's hit bar
                context.strokeStyle = "black";
                context.strokeRect(g.x - (g.maxHealth / 2), g.y + margin, g.maxHealth, (margin / 2));

                if (g.health > 50) {
                    context.fillStyle = "green";
                    context.fillRect(g.x - (g.maxHealth / 2), g.y + margin, g.health, (margin / 2));
    
                } else if (g.health > 20) {
                    context.fillStyle = "orange";
                    context.fillRect(g.x - (g.maxHealth / 2), g.y + margin, g.health, (margin / 2));
    
                } else if (g.health > 0) {
                    context.fillStyle = "red";
                    context.fillRect(g.x - (g.maxHealth / 2), g.y + margin, g.health, (margin / 2));
                };
            };
    
        // Controls for ghoul movements
        for (let g of ghouls) {
            if (g.alert === true) { // if the ghoul has been put on alert then it should move toward the player automatically
                if (g.x < player.x) {
                    g.x += g.speed;
                } else if (g.x > player.x) {
                    g.x -= g.speed;
                }
    
                if (g.y < player.y) {
                    g.y += g.speed;
                } else if (g.y > player.y) {
                    g.y -= g.speed;
                }
    
            } else if (g.alert === false) { // otherwise we want the ghoul to patrol in a square
                if (g.x - margin < (margin * 2)) { // if ghoul's top left is within 2 margins then we need to increase g.x
                    g.x += g.speed;
                }
                
                if (g.x - margin > (canvas.width - (margin * 2))) { // if ghoul's top right is within 2 margins of the right wall then we need to decrease g.x
                    g.x -= g.speed;
                } 
                
                if (g.y - margin < (margin * 2)) {
                    g.y += g.speed;
                }
                
                if (g.y + margin < (canvas.width - (margin * 2))) {
                    g.y -= g.speed;
                }

                if (margin * 2 < g.x < (canvas.width - (margin * 2)) && margin * 2 < g.y < (canvas.height - (margin * 2))) {
                    
                }
            };
        }
    
        // Calling the collision functions for the ghouls
        for (let g of ghouls) {
            if (alert(g)) { // if a player enters a ghouls eyeshot
                g.alert = true;
            } 
            
            if (playerCollides(g)) { // if a ghoul actually makes contact w the player
                if (player.attack) { // if the player is attacking, we need to run the attack function
                    ghoulKill(g);
                } else if (player.attack === false) { // else the player takes damage
                    if (player.health > 0) {
                        player.health -= 10;
                        // I want the player to bounce back when hit as well
                        bounceSpeed = g.speed * 2;
                        ghoulAttack(bounceSpeed, g);
                    } else if (player.health <= 0) { // if the player's health falls below 0 then the ghoul has killed the player
                        gameOver("You lose!", elapsedSeconds, score);
                    }
                }
            }
        };
    
    }
    


    // // // // // // // TREASURE // // // // // // //
    // assigning object details to the random number of chests we're building
    
    if (chests.length < noOfChests) {
        let c = {
            x       : (randint(1, 9))*100,
            y       : (randint(1, 9))*100,
            size    : 50
        };

        chests.push(c);
    }

    // drawing the chests
    for (let c of chests) {
        context.drawImage(chestSprite, c.x - (c.size / 2), c.y - (c.size / 2));
    };

    // calling the treasure function if touching a chest:
    for (let c of chests) {
        if (playerCollides(c)) {
            if (player.attack) {
                noOfChests -= 1;
                treasure(c);
            }
        }
    };


    // // // // // // // GATES // // // // // // //
    if (floor === 5) {
        if (player.complete === true) {
            context.fillStyle = "white";
            context.fillRect(gate.x, gate.y, gate.xSize, gate.ySize);
            context.drawImage(treasureOpen, prevGate.x, prevGate.y);

        } else {
            context.drawImage(treasureClosed, gate.x, gate.y);
            context.fillStyle = "white";
            context.fillRect(prevGate.x, prevGate.y, prevGate.xSize, prevGate.ySize);
        }

    } else {
        // drawing the doors (room 0 should have been called in init)
        context.fillStyle = "white";
        context.fillRect(gate.x, gate.y, gate.xSize, gate.ySize);
        context.fillStyle = "white";
        context.fillRect(prevGate.x, prevGate.y, prevGate.xSize, prevGate.ySize);
    };
    

    // calling the gates collision function
    if (gateCollides(gate)) {
        if (room === 6) { // means we're in a staircase so we want to increase our floor and reset our room # to 1
            floor += 1;
            noOfEnemies += 1;
            room = 1;
            levelProgress(room);
        }
        if (floor === 5 && room === 6) { // if on floor 5 in room 6 and the collission is called, they are touching the treasure at the end of the castle so the main quest is complete
            player.complete = true;
            levelProgress(room);
        } else if (floor != 5 && room != 6) {
            room += 1
            levelProgress(room);
        } 
    };



    // // // // // // // EVENT LISTENERS & PLAYER MOVEMENT // // // // // // //
    // // attempt at having a mouse follower for direction & movement
    // window.addEventListener("click", mouseMove, false);

    // player movement parameters
    if (moveLeft) {
        player.x = player.x - player.speed;
    };

    if (moveRight) {
        player.x = player.x + player.speed;
    };

    if (moveUp) {
        player.y = player.y - player.speed;
    };

    if (moveDown) {
        player.y = player.y + player.speed;
    };

};





// // // // // // // KEY STROKE ACTIONS // // // // // // //

// function mouseMove(event) {
//     // the clientX and clientY are currently in relation to viewport.
//     // They need to be in relation to the canvas.
//     if (event.clientX < (window.innerWidth / 2) + (canvas.width / 2) ||
//         event.clientX > (window.innerWidth / 2) - (canvas.width / 2)) {
//             player.x = event.clientX;
//         };

//     if (event.clientY < (window.innerHeight / 2) + (canvas.height / 2) ||
//         event.clientY > (window.innerHeight / 2) - (canvas.height / 2)) {
//             player.y = event.clientY;
//         };
// };

function activate(event) {
    let key = event.key;
    if(key === "ArrowLeft" || key === "a") {
        moveLeft = true;
    } else if (key === "ArrowUp" || key === "w") {
        moveUp = true;
    } else if (key === "ArrowDown" || key === "s") {
        moveDown = true;
    } else if (key === "ArrowRight" || key === "d") {
        moveRight = true;
    } else if (key === "e") {
        // document.querySelector('audio').play();
        player.attack = true;
    } // else if (key === "mouseDown") {
    //    player.x = e.pageX;
    //    player.y = e.pageY;
    //}

    // // // put js for following the direction of the mouse in here so that it only happens while the mouse is pressed
    // } else if (key === "MouseClick") {
    //     document.addEventListener("mousemove") {
    //         player.x = ____.pageX
    //         player.y = ____.pageY
    //     }
    // } else if (key === "RightMouseClick") {
    //          swing sword
    //     }

};

function deactivate(event) {
    let key = event.key;
    if(key === "ArrowLeft" || key === "a") {
        moveLeft = false;
    } else if (key === "ArrowUp" || key === "w") {
        moveUp = false;
    } else if (key === "ArrowDown" || key === "s") {
        moveDown = false;
    } else if (key === "ArrowRight" || key === "d") {
        moveRight = false;
    } else if (key === "e") {
        player.attack = false;
    }
};





// // // // // // // PRE WRITTEN FUNCTIONs // // // // // // //

function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
};

function handle_response() {
    // check that the response has fully arrived
    if (xhttp.readyState === 4) {
        // check that the request was successful
        if (xhttp.status === 200) {
            if (xhttp.responseText === "success") {
                // score was successfully stored in db
            } else {
                // score was not successfully stored in db
            }
        }
    }
};







// // // // // // // CHEAT CODES // // // // // // //
function cheatCode(event) { // selects the cheat code that has been input into the js form on our html page
    let cheatCode = cheat.value;
    if (cheatCode === "iwantnobaddies") {
        activeCheat = true;
    } else {
        activeCheat = false;
    }
    event.preventDefault;
    return;
};








// // // // // // // DIFFERENT COLLISION FUNCTIONs // // // // // // //
// figures out if something has collided with the player vice versa
function playerCollides(obstacle) {
    if (player.x + player.size < obstacle.x ||
        obstacle.x + obstacle.size < player.x ||
        player.y > obstacle.y + obstacle.size ||
        obstacle.y > player.y + player.size) {
            return false;
    } else {
            return true;
    }
};

// Because the gates are strangely sized, I have a slightly different function for them
function gateCollides(obstacle) {
    if (player.x + player.size < obstacle.x ||
        obstacle.x + obstacle.xSize < player.x ||
        player.y > obstacle.y + obstacle.ySize ||
        obstacle.y > player.y + player.size) {
            return false;
    } else {
            return true;
    }
};

// figures out if player has entered an enemies alert radius
function alert(obstacle) {
    if (player.x + player.size < obstacle.x - (margin * 2) ||
        obstacle.x + (margin * 2) < player.x ||
        player.y > obstacle.y + (margin * 2) ||
        obstacle.y - (margin * 2) > player.y + player.size) {
            return false;
    } else {
            return true;
    }
};



// // // // // // // GHOULS // // // // // // //
// function to kill a ghoul (IE reduce it's health and eventually remove it entirely)
function ghoulKill(g) {
    if (g.health > 0) {
        g.health -= player.damage
    } else if (g.health <= 0) {
        score += (g.maxHealth * 100)

        // //////// Create a new element that shows the score received after killing a ghoul, disappears after 2 seconds.
        // //////// Would be better if it moved upward on Y axis and reduced opacity.
        // new_element = document.createElement("p");
        // new_element.innerHTML = score
        noOfEnemies -= 1;
        killedGhouls += 1;
        ghouls.pop(g);
    }
    return;
};

// Function to propel player backwards if they've been hit by a ghoul
function ghoulAttack(bounceSpeed, obstacle) {
    if (player.x + player.size < obstacle.x) { // if player is touched from the right
        player.x -= bounceSpeed;
    } else if (obstacle.x + obstacle.size < player.x) { // if player is touched from the left
        player.x += bounceSpeed;
    } else if (player.y > obstacle.y + obstacle.size) { // if player is touched from the bottom
        player.y -= bounceSpeed;
    } else if (obstacle.y > player.y + player.size) { // if player is touched from the top
        player.y += bounceSpeed;
    }
    return;
};

// Game Over function for if player loses IE if playerCollides w g = true & p health = 0
function gameOver(message, score) {

    let maxTime = 3600000; // number of miliseconds in an hour
    timeScore = maxTime - timeScore;
    score = score + timeScore;

    // stop listening for events
    window.removeEventListener("keydown", activate, false);
    window.removeEventListener("keyup", deactivate, false);

    // stop animating
    window.cancelAnimationFrame(request_id);

    // clear the canvas
    // context.clearRect(0, 0, canvas.width, canvas.height);

    // acknowledge the loss on the page by displaying it
    let outcome_element = document.querySelector("#outcome");
    outcome_element.innerHTML = message;

    // AJAX send score to db
    let data = new FormData();
    data.append("score", score);
    
    xhttp = new XMLHttpRequest();
    xhttp.addvEventListener("readystatechange", handle_response, false)
    xhttp.open("POST", "/store_score", true);
    xhttp.send(data);

    // HAVE A "continue?" button show up at this point
    return;
};



// // // // // // // TREAUSRE // // // // // // //
//////////// Only offer power ups to the player if they attack a treasure chest IE if playerCollides w chest = true
// Eligible power ups from the array: "speed +20", "damage +20", "max health +20", "health restore", "score +5000"
function treasure(chest) {
    let chestContains = randint(0, 4);
    if (items[chestContains] === "speed +20%") {
        player.speed += (player.speed * 0.2)
    } else if (items[chestContains] === "damage +20%") {
        player.damage += (player.damage * 0.2)
    } else if (items[chestContains] === "max health +20%") {
        player.maxHealth += (player.maxHealth * 0.2)
    } else if (items[chestContains] === "health restore") {
        player.health = player.maxHealth
    } else if (items[chestContains] === "score +5000") {
        score += 5000
    };
    chests.pop(chest);

    // //////// Create a new element that shows what power up was received after opening a chest, disappears after 2 seconds.
    // //////// Would be better if it moved upward on Y axis and reduced opacity.
    // new_element = document.createElement("p");
    // new_element.innerHTML = score

    return;
};




// // // // // // // LEVEL CREATION // // // // // // //
// Brings the player to the next Level if they've hit the gate in the level they were in IE if playerCollides w gate = true
// Also being used to treat the different floors differently.
// When the player finishes the game and complete == true, the player then navigates back down to the exit of the castle
function levelProgress(room) {

    // If this function is called then we need to establish a new random # of chests for the next room 
    noOfChests = randint(1, 3);
    chests = [];
    // And a new number of obstacles
    noOfObstacles = randint(1, 20);
    obstacle = [];
    // and reset the start location of the ghouls
    noOfEnemies = floor;
    ghouls = [];

    if (player.complete === false) { // path up the castle
        if (floor != 5) {
            if (room === 0)  {
                // in room 0 the player is outside. No prevGate, just the entrance to the castle.
                gate.xSize = margin;
                gate.ySize = -3;
                gate.x = (canvas.width / 2) - (gate.xSize / 2);
                gate.y = canvas.height - margin;
    
                return;
    
            } else if (room === 1) { // room 1 should have a door at 3oclock
                gate.xSize = -3;
                gate.ySize = margin;
                gate.x = canvas.width - margin;
                gate.y = (canvas.height / 2) - (gate.ySize /2);
    
                // and the player would enter from the top
                prevGate.xSize = margin;
                prevGate.ySize = 3;
                prevGate.x = (canvas.width / 2) - (gate.xSize /2);
                prevGate.y = margin;
    
                // so we need to catapult our player to the x and y of the prev gate for the next room
                player.x = prevGate.x;
                player.y = prevGate.y;
    
                // increase level only and return
                level += 1
                return;
    
            } else if (room === 2) { // room 2 would have a door at 6 o clock
                gate.xSize = margin;
                gate.ySize = 3;
                gate.x = (canvas.width / 2) - (gate.xSize / 2);
                gate.y = canvas.height - margin;
    
                // and the player would enter from 9 o clock
                prevGate.xSize = 3;
                prevGate.ySize = margin;
                prevGate.x = margin;
                prevGate.y = (canvas.height / 2) - (gate.ySize /2);
    
                // so we need to catapult our player to the x and y of the prev gate for the next room
                player.x = prevGate.x;
                player.y = prevGate.y;
    
                // increase level only and return
                level += 1
                return;
    
            } else if (room === 3) { // room 3 would have a door at 9 o clock
                gate.xSize = 3;
                gate.ySize = margin;
                gate.x = margin;
                gate.y = (canvas.height / 2) - (gate.ySize /2);
    
                // and the player would enter from 12 o clock
                prevGate.xSize = margin;
                prevGate.ySize = 3;
                prevGate.x = (canvas.width / 2) - (gate.xSize /2);
                prevGate.y = margin;
    
                // so we need to catapult our player to the x and y of the prev gate for the next room
                player.x = prevGate.x;
                player.y = prevGate.y;
    
                // increase level only and return
                level += 1
                return;
                
            } else if (room === 4) { // because the player would auto-progress if we moved where the gate was first, we'll intermitently move the player to centre field for a frame
                player.x = canvas.width / 2;
                player.y = canvas.height / 2;
    
                // room 4 would have a door at 9 o clock
                gate.xSize = 3;
                gate.ySize = margin;
                gate.x = margin;
                gate.y = (canvas.height / 2) - (gate.ySize /2);
    
                // and the player would enter from 3 o clock
                prevGate.xSize = 3;
                prevGate.ySize = margin;
                prevGate.x = canvas.width - margin;
                prevGate.y = (canvas.height / 2) - (gate.ySize /2);
    
                // so we need to catapult our player back to the x and y of the prev gate
                player.x = prevGate.x;
                player.y = prevGate.y;
    
                // increase level only and return
                level += 1;
                return;
    
            } else if (room === 5) { // room 5 would have a stairway at 12oclock
                gate.xSize = margin;
                gate.ySize = 3;
                gate.x = (canvas.width / 2) - (gate.xSize /2);
                gate.y = margin;
    
                // and the player would enter from the 3 o clock
                prevGate.xSize = 3
                prevGate.ySize = margin;
                prevGate.x = canvas.width - margin;
                prevGate.y = (canvas.height / 2) - (gate.ySize /2);
    
                // so we need to catapult our player to the x and y of the prev gate for the next room
                player.x = prevGate.x;
                player.y = prevGate.y;
    
                // increase level only and return
                level += 1
                return;
    
            } else if (room === 6) { // Should just be stairs and should have a chest w health replenish in it
                gate.xSize = 3;
                gate.ySize = margin;
                gate.x = canvas.width - margin;
                gate.y = (canvas.height / 2) - (gate.ySize / 2);
    
                // // and the player would enter from 6 o clock
                prevGate.xSize = margin;
                prevGate.ySize = 3;
                prevGate.x = (canvas.width / 2) - (gate.xSize / 2);
                prevGate.y = canvas.height - margin;
    
                // so we need to catapult our player to the x and y of the prev gate for the next room
                player.x = prevGate.x;
                player.y = prevGate.y;
    
                // increase level and floor, then return
                level += 1
                return;
            }
        } else if (floor === 5) { // the treasure in the centre of the room will act as a gate
                gate.xSize = margin;
                gate.ySize = margin;
                gate.x = (canvas.width / 2) - (margin / 2);
                gate.y = (canvas.height / 2) - (margin / 2);
    
                // and the player would enter from 6 o clock
                prevGate.xSize = margin;
                prevGate.ySize = 3;
                prevGate.x = (canvas.width / 2) - (gate.xSize / 2);
                prevGate.y = canvas.height - margin;
    
                // so we need to catapult our player to the x and y of the prev gate for the next room
                player.x = prevGate.x;
                player.y = prevGate.y;

                player.complete = true
    
                return;
            }

    } else { // the path back down again
        if (floor === 5) { // the door at 6 o clock that we entered through should now be open to walk through again
            gate.xSize = margin;
            gate.ySize = 3;
            gate.x = (canvas.width / 2) - (gate.xSize / 2);
            gate.y = canvas.height - margin;

            // and the previous gate would be in the centre of the room from 6 o clock
            prevGate.xSize = margin;
            prevGate.ySize = margin;
            prevGate.x = (canvas.width / 2) - (margin / 2);
            prevGate.y = (canvas.height / 2) - (margin / 2);

            return;
        } else {
        
        if (room === 0)  {
            // in room 0 the player is outside at the end of the game. PrevGate is the only gate.
            prevGate.xSize = margin;
            prevGate.ySize = 3;
            prevGate.x = (canvas.width / 2) - (gate.xSize / 2);
            prevGate.y = canvas.height - margin;

            noOfEnemies = killedGhouls; // I want all of the enemies killed so far to be outside waiting for the player

            return;

        } else if (room === 1) {
            gate.xSize = margin;
            gate.ySize = 3;
            gate.x = (canvas.width / 2) - (gate.xSize /2);
            gate.y = margin;
            
            prevGate.xSize = 3;
            prevGate.ySize = margin;
            prevGate.x = canvas.width - margin;
            prevGate.y = (canvas.height / 2) - (gate.ySize /2);
            

            // so we need to catapult our player to the x and y of the prev gate for the next room
            player.x = prevGate.x;
            player.y = prevGate.y;

            // increase level only and return
            level += 1
            return;

        } else if (room === 2) {
        
            gate.xSize = 3;
            gate.ySize = margin;
            gate.x = margin;
            gate.y = (canvas.height / 2) - (gate.ySize /2);

            prevGate.xSize = margin;
            prevGate.ySize = 3;
            prevGate.x = (canvas.width / 2) - (gate.xSize / 2);
            prevGate.y = canvas.height - margin;

            // so we need to catapult our player to the x and y of the prev gate for the next room
            player.x = prevGate.x;
            player.y = prevGate.y;

            // increase level only and return
            level += 1
            return;

        } else if (room === 3) {

            gate.xSize = margin;
            gate.ySize = 3;
            gate.x = (canvas.width / 2) - (gate.xSize /2);
            gate.y = margin;


            prevGate.xSize = 3;
            prevGate.ySize = margin;
            prevGate.x = margin;
            prevGate.y = (canvas.height / 2) - (gate.ySize /2);

            // so we need to catapult our player to the x and y of the prev gate for the next room
            player.x = prevGate.x;
            player.y = prevGate.y;

            // increase level only and return
            level += 1
            return;
            
        } else if (room === 4) { // because the player would auto-progress if we moved where the gate was first, we'll intermitently move the player to centre field for a frame
            player.x = canvas.width / 2;
            player.y = canvas.height / 2;


            gate.xSize = 3;
            gate.ySize = margin;
            gate.x = canvas.width - margin;
            gate.y = (canvas.height / 2) - (gate.ySize /2);


            prevGate.xSize = 3;
            prevGate.ySize = margin;
            prevGate.x = margin;
            prevGate.y = (canvas.height / 2) - (gate.ySize /2);



            // so we need to catapult our player back to the x and y of the prev gate
            player.x = prevGate.x;
            player.y = prevGate.y;

            // increase level only and return
            level += 1;
            return;

        } else if (room === 5) {

            gate.xSize = 3
            gate.ySize = margin;
            gate.x = canvas.width - margin;
            gate.y = (canvas.height / 2) - (gate.ySize /2);


            prevGate.xSize = margin;
            prevGate.ySize = 3;
            prevGate.x = (canvas.width / 2) - (gate.xSize /2);
            prevGate.y = margin;


            // so we need to catapult our player to the x and y of the prev gate for the next room
            player.x = prevGate.x;
            player.y = prevGate.y;

            // increase level only and return
            level += 1
            return;

        } else if (room === 6) {
            gate.xSize = margin;
            gate.ySize = 3;
            gate.x = (canvas.width / 2) - (gate.xSize / 2);
            gate.y = canvas.height - margin;

            prevGate.xSize = 3;
            prevGate.ySize = margin;
            prevGate.x = canvas.width - margin;
            prevGate.y = (canvas.height / 2) - (gate.ySize / 2);

            // so we need to catapult our player to the x and y of the prev gate for the next room
            player.x = prevGate.x;
            player.y = prevGate.y;

            // increase level and floor, then return
            level += 1
            return;
        }
        } 
    
    }
};