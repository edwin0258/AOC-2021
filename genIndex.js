const fs = require('fs');

let doc = [`<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="author" content="Devin Miller">
        <link rel="icon" href="https://styles.redditmedia.com/t5_2fwo/styles/communityIcon_1bqa1ibfp8q11.png?width=256&s=45361614cdf4a306d5510b414d18c02603c7dd3c">
        <link rel="stylesheet" type="text/css" href="index.css"/>
        <link rel="stylesheet" type="text/css" href="desert.css"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">
        <title>AOC-2021 solutions</title>
    </head>
`,
`<body>
        <script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>
        <h1 id='page-top' class="page-header">AOC-2021 Solutions ~ Devin Miller</h1>
        <h2>Days Completed</h2>
        <a class='to-page-top' href='#page-top'>Back to Top</a>
        
`,
``,
`
    </body>
</html>
`]


let genDoc = []; // Generated html

let files = fs.readdirSync('./');
let days = files.filter(x => x.match(/^day..?$/g));
// sort so days appear in correct order
days.sort((a, b) => +a.substring(3,) > +b.substring(3,))

genDoc.push(`<div class='day-links'>`);
days.forEach(day => {
    genDoc.push(`<a class='day-link' href='#${day}'>${day}</a>`);
})
genDoc.push(`</div>`);

days.forEach(day => {
    genDoc.push(readDay(day));
})

function readDay(day) {
    let html = [];
    let languages = ['js', 'py'];
    let lfns = {'js': 'javascript', 'py': 'python', 'codepen': 'codepen'}; // language full names, for icons

    // only fetch files of languages included above.
    let languagesPattern = languages.map(x => '.' + x).join('|');

    const files = fs.readdirSync(`./${day}`);

    let pattern = new RegExp('..*?(' + languagesPattern + ')$')
    let codepens = files.filter(x => x.match('codepens.txt')); // special codepens embeded file
    let code = files.filter(x => x.match(pattern)); // Only files of desired languages 
    let usedLanguages = new Set(code.map(f => f.slice(f.indexOf('.')+1,f.length))) // using set to remove duplicates

    html.push(`<h2 class='day-header' id='${day}'>${day}`);
    usedLanguages.forEach(lang => {
        html.push(`<img class='lang-icon' src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/${lfns[lang]}/${lfns[lang]}-original.svg" />`);
    })

    if(codepens.length > 0) { // add codepen if used
        html.push(`<img class='lang-icon' src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/codepen/codepen-plain.svg" />`);
    }

    // generate html for code for day
    html.push(`</h2><div class='codes'>`);

    code.forEach(fileName => {
        html.push(readCode(day, fileName));
    })

    // if codepens file exist, embed it/them in page for day 
    if(codepens.length > 0) {
        let codepenData = fs.readFileSync(`./${day}/codepens.txt`);
        codepenData = codepenData.toString().split('\n');
        let codepenNext = false; 
        let namePattern = new RegExp(/^\[.[a-zA-Z\d-]*\]$/);
        let codepenName = "";
        codepenData.forEach(line => {
        
            if(codepenNext) {
                html.push(`<div class='codepen'>`);
                html.push(`<h3 class='code-header'>${codepenName.slice(1,codepenName.length - 1)}</h3>`);
                html.push(line);
                html.push(`</div>`);
                codepenNext = false;
            }

            if(line.match(namePattern)) {
                codepenNext = true;
                codepenName = line;
            }
        })
    }

    html.push(`</div>`);
    return html.join('');
}

function readCode(day, fn) {
    let html = [];
    const data = fs.readFileSync(`./${day}/${fn}`);

    html.push(`<div class='code'>`);
    html.push(`<h3 class='code-header'>${fn}</h3>`);
    html.push(`<pre class='prettyprint'><code>${data.toString()}</code></pre>`);
    html.push(`</div>`);

    return html.join('');
}

function addHTML(html) {
    genDoc.push(html);
}

doc[2] = genDoc.join('');

fs.writeFile('index.html', doc, (err) => {
    if (err) throw err;
})
