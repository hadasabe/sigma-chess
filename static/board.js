var map;
var divSquare = '<div id="s$coord" class="square $color"></div>'
var divFigure = '<div id="f$coord" class="figure">$figure</div>'
var isDragging = false;

$(function () {
    start();
    setInterval('showFiguresPy()', 3000);
})

function start() {
    map = new Array(64);
    addSquares();
    showFiguresPy();
    // moveFigurePy('rnbqkbnrpppppppp11111111111111111111111111111111PPPPPPPPRNBQKBNR');
}

function setDraggable() {
    $('.figure').draggable({
        start: function (event, ui)  {
            isDragging = true;
        }
    });
}

function setDroppable() {
    $('.square').droppable({
        drop: function(event, ui) {
            var frCoord = ui.draggable.attr('id').substring(1);
            var toCoord = this.id.substring(1);
            moveFigure(frCoord, toCoord);
            isDragging = false;
        }
    });
}

function moveFigure(frCoord, toCoord) {
    figure = map[frCoord];
    if (map[toCoord] == 1 || frCoord != toCoord) {
        showFigure(frCoord, '1');
        showFigure(toCoord, figure);
        console.log('move from ' + frCoord + ' to ' + toCoord, figure);
        map[frCoord] = '1';
        map[toCoord] = figure;
        writeToJSONFile(map.join(''));
        console.log(map);
    }
    else {
        showFigure(frCoord - 1, '1');
        showFigure(toCoord - 1, figure);
        console.log('move from ' + map[frCoord] + ' to ' + map[toCoord], figure);
        map[frCoord] = figure;
        map[toCoord] = '1';
        writeToJSONFile(map.join(''));
        console.log(map[frCoord], map[toCoord], map)
        console.log(map[frCoord], map[toCoord])
    }
    setDraggable();
}

function addSquares() {
    $('.board').html('');
    for (var coord = 0; coord < 64; coord++) 
        $('.board').append(divSquare.replace('$coord', coord).replace('$color', isBlackSquare(coord) ? 'black' : 'white'));
    setDroppable();
}

function writeToJSONFile(data) {
    // Переменная, которую нужно передать в Python

var jsonData = JSON.stringify({ 'fen': data });

    $.ajax({
        type: "POST",
        url: "/get_fen",
        data: jsonData,
        contentType: "application/json",
        success: function(response) {
        // console.log("Success: " + response);
  },
    error: function(xhr, status, error) {
        console.error("Error: " + error);
  }
});
}

// function moveFigurePy(map){
//     writeToJSONFile('rnbqkbnrpppppppp11111111111111111111111111111111PPPPPPPPRNBQKBNR');
// }

function showFiguresPy() {
    if (isDragging) return;
    $.getJSON( "static/chess.json", function(data) {
        const figures = data.fen;
        showFigures(figures);
        // console.log(map)
    });
}

function showFigures(figures) {
    for (var coord = 0; coord < 64; coord++)
        showFigure(coord, figures.charAt(coord));
    setDraggable();
}

function showFigure(coord, figure) {
    if (map[coord] == figure) return;
    map[coord] = figure;
    $('#s' + coord).html(divFigure.replace('$coord', coord).replace('$figure', getChessSymbole(figure)));
    setDraggable();
}

function getChessSymbole(figure) {
    switch (figure) {
        case 'R' : return '&#9814';
        case 'B' : return '&#9815';
        case 'K' : return '&#9812';
        case 'Q' : return '&#9813';
        case 'N' : return '&#9816';
        case 'P' : return '&#9817';
        case 'r' : return '&#9820';
        case 'b' : return '&#9821';
        case 'k' : return '&#9818';
        case 'q' : return '&#9819';
        case 'n' : return '&#9822';
        case 'p' : return '&#9823';
        default : return '';
    }
}

function isBlackSquare(coord) {
    return (coord % 8 + Math.floor(coord / 8)) % 2;
}

