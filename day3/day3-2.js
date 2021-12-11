const fs = require('fs');


function filterBinaries(lines, func) {
    let linesTemp = lines; // temp used for filtering for each col solution
    let i = 0;

    while(linesTemp.length > 1) {
        let [ones, zeros] = [0, 0];

        // count number of 1's and 0's in certain col
        for(let row = 0; row < linesTemp.length; row++) {
            if(linesTemp[row][i] == '1') ones += 1
            else if(linesTemp[row][i] == '0') zeros += 1
        }
        
        // pass lines temp into specific filter function
        linesTemp = func(ones, zeros, linesTemp, i);
        i++;
    }

    return linesTemp[0].join('');
}

let getOxyGen = ((ones, zeros, linesTemp, i) => {
    if(ones >= zeros)
        return linesTemp.filter(x => x[i] == '1');
    return linesTemp.filter(x => x[i] == '0');
})

let getCo2 = ((ones, zeros, linesTemp, i) => {
    if(ones < zeros)
        return linesTemp.filter(x => x[i] == '1');
    return linesTemp.filter(x => x[i] == '0');
})

fs.readFile('data.txt', (err, data) => {
    if (err) throw err;

    let l = data.toString().split('\n').map(x => x.split(''));
    let [lifeSupport, oxygenGen, co2] = [0, filterBinaries(l, getOxyGen), filterBinaries(l, getCo2)]; 

    lifeSupport = parseInt(oxygenGen, 2) * parseInt(co2, 2);

    // log solution
    console.log(lifeSupport);
})
