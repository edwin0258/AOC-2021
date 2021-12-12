const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err;

    let boardSize = 5; // five rows per board

    let [nums, ...boards] = data.toString().split('\n')
    nums = nums.split(',');
    boards = boards.filter(x => x.length > 4); // filter out empty lines
    let boardsSplit = []; // 2d array with 1st level representing each board
    let boardStats = []; // hold how many marked in x and y 

    for(let i = 0; i < boards.length; i+=boardSize) {
        boardsSplit.push(boards.slice(i, i+boardSize)); // one board per index
        boardStats.push({'x': Array(boardSize).fill(0), 'y': Array(boardSize).fill(0)})
    }
    
    boardsSplit = boardsSplit.map(board => board.join(' ').split(' ').filter(x => x.length != 0));
    callBingoNums(nums, boardsSplit, boardStats, boardSize); 
})


function callBingoNums(bns, boards, stats, size) {
    let calledNums = [];
    bns.some(num => { // some used so can break out once winner determined
        calledNums.push(num); // record number being called
        // record num being found in board stats if found
        boards.forEach((b, bi) => {
            let matches = b.filter(bnum => bnum == num);
            if(matches.length > 0) {
                let y = b.indexOf(matches[0]) % size; // col of match
                let x = Math.floor(b.indexOf(matches[0]) / size);

                stats[bi]['x'][x] += 1;
                stats[bi]['y'][y] += 1;
            }
        })

        let check = checkStats(stats);
        if(check[0] != -1) {
            console.log("WINNER BOARD: " + (check[0]+1)); 
            printSolution(boards[check[0]], calledNums);
            return true; // we are done
        }
    })
}

// check to see if there is a bingo winner
// returns: [winner? (-1, board index), (0: row, 1: col), row/col index]
function checkStats(stats) {
    let check = [-1, -1, -1];
    stats.forEach((bstats, bi) => {
        if(bstats['x'].indexOf(5) != -1) {
            check = [bi, 0, bstats['x'].indexOf(5)];
        } else if(bstats['y'].indexOf(5) != -1) {
            check = [bi, 1, bstats['y'].indexOf(5)];
        }
    })

    return check;
}

// calculate and print solution to challenge
function printSolution(board, calledNums) {
    let sum = board.filter(x => calledNums.indexOf(x) == -1)
               .reduce((sum, x) => sum + parseInt(x), 0);
    console.log(sum * calledNums[calledNums.length - 1]);
}
