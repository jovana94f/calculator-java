const fs = require('fs');
const path = require('path');

// Funkcija za rekurzivno čitanje fajlova iz direktorijuma
function getAllFiles(dirPath, arrayOfFiles) {
    const files = fs.readdirSync(dirPath);

    arrayOfFiles = arrayOfFiles || [];

    files.forEach((file) => {
        const fullPath = path.join(dirPath, file);
        if (fs.statSync(fullPath).isDirectory()) {
            arrayOfFiles = getAllFiles(fullPath, arrayOfFiles);
        } else {
            arrayOfFiles.push(fullPath);
        }
    });

    return arrayOfFiles;
}

// Funkcija za brojanje linija koda u fajlu
function countLines(filePath) {
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const lines = fileContent.split('\n');
    return lines.length;
}

// Glavna funkcija za izračunavanje LOC metrike
function calculateLOC(projectPath) {
    const allFiles = getAllFiles(projectPath);
    let totalLOC = 0;

    allFiles.forEach((file) => {
        if (file.endsWith('.java')) {
            const loc = countLines(file);
            console.log(`${file}: ${loc} linija`);
            totalLOC += loc;
        }
    });

    console.log(`Ukupno LOC: ${totalLOC} linija`);
}

// Putanja do projekta
const projectPath = path.join(__dirname);
calculateLOC(projectPath);