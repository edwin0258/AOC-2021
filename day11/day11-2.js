const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err

    dumbos = data.toString().split('\n').map(x => x.split('').map(n => +n));

    // add one to all
    function addOneDumbos(dumbos) {
      return dumbos.map(row => row.map(x => x + 1));
    }

    // dumbos ready to flash (greater than 9)
    function getGreaterThan(dumbos, lim) {
      let greater = [];
      dumbos.forEach((row, y) => {
        row.forEach((d, x) => { if(d > lim) greater.push([y, x]) })
      })
      return greater;
    }

    // Add one around max dumbos
    function addOneAround(dmbs, maxs) {
      //console.log('before', dmbs);
      
      maxs.forEach(z=> {
        let [zy, zx] = [z[0], z[1]];
        let around = [[zy+1, zx-1], [zy+1, zx], [zy+1, zx+1],
                      [zy,   zx-1] /* dumbo */, [zy,   zx+1],
                      [zy-1, zx-1], [zy-1, zx], [zy-1, zx+1]];
        
        // add one if defined
        around.forEach(c => {
          let [cy, cx] = [c[0], c[1]]
          // not undefined and not a 9 or -1
          if(!(dmbs[cy] === undefined || dmbs[cy][cx] === undefined) && 
             (dmbs[cy][cx] != -1)) {
            
            dmbs[cy][cx] = dmbs[cy][cx] + 1;
          }
        })
      })
      //console.log('after', dmbs);
      return dmbs;
    }

    // set dumbos that are greater than 10 to -1 to avoid being used in any way before next loop
    function flashDumbos(dumbos, lim) {
      return dumbos.map(row => row.map(x => (x > lim) ? -1 : x));
    }

    // reset all flashed dumbos to 0
    function resetFlashed(dumbos) {
      return dumbos.map(row => row.map(x => (x == -1) ? 0 : x));
    }

    // determine if all dumbos are flashing at the same time
    function isAllFlashing(dumbos) {
      // a return of 0 means all are flashing
      return dumbos.filter(row => row.filter(x => x != 0).length > 0).length;
    }

    let stepCount = 100;
    let steps = 0;
    let flashes = 0;
    let energyLimit = 9;
    while(isAllFlashing(dumbos) != 0) {
      steps += 1;
      dumbos = addOneDumbos(dumbos);
      totalStepFlashes = 0;

      maxDumbos = getGreaterThan(dumbos, energyLimit);
      // loop until no new nines appear
      while(maxDumbos.length > 0) {
        dumbos = flashDumbos(dumbos, energyLimit);
        dumbos = addOneAround(dumbos, maxDumbos);
        flashes += maxDumbos.length; // add to total flashes
        totalStepFlashes += maxDumbos.length;
        maxDumbos = getGreaterThan(dumbos, energyLimit);
      }

      dumbos = resetFlashed(dumbos);
    }

    console.log(steps);
})
