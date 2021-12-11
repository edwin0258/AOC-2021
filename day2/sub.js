const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
    if (err) throw err;

    let lines = data.toString().split('\n').map(x => x.split(' '));
    let [hor, vert] = [0, 0];

    lines.forEach(l => {
        let [dir, a] = [l[0], parseInt(l[1])]
        let funcs = {'forward': (() => hor += a), 
                     'down':    (() => vert += a), 
                     'up':      (() => vert -=a)}
        if(dir in funcs)
            funcs[dir]();
    })

    console.log(hor * vert);
})
