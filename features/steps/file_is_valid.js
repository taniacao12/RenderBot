const { Given, When, Then } = require('@cucumber/cucumber');
const fs = require('fs');
const assert = require('assert');
const readline = require('readline');

let filePath, info, externalDoors, numExDoors, hExits, vExits;

Given('the name of a file', function (callback) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Please enter the file name: ', (fileName) => {
        filePath = `output/JSON/${fileName}.json`;
        assert(fs.existsSync(filePath), `File ${fileName} does not exist in the dataset folder.`);
        rl.close();
        callback();
    });
});

When('I read the file', function () {
    console.log(`Reading ${filePath}.`);
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    info = JSON.parse(fileContent);
    // console.log(info);
});

Then('it should have at least 3 walls', function () {
    const externalWalls = info.External.Walls;
    const internalWalls = info.Internal.Walls;
    const numWalls = Object.values(externalWalls).flat().length +
                    Object.values(internalWalls).flat().length;
    assert(numWalls >= 3, 'Less than three walls found in the file');
    console.log(`File contains ${numWalls} walls.`);
});

Then('it should have at least 1 door', function () {
    externalDoors = info.External.Doors;
    const internalDoors = info.Internal.Doors;
    numExDoors = Object.values(externalDoors).flat().length
    const numDoors = numExDoors + Object.values(internalDoors).flat().length;
    assert(numDoors > 0, 'No doors found in the file');
    console.log(`File contains ${numDoors} doors.`);
});

Then('at least 1 door should be an exit', function () {
    assert(numExDoors > 0, 'No exits found in the file');
    console.log(`File contains ${numExDoors} exits.`);
});

Then('I should say the file is valid', function () {
    console.log('File is valid.');
});

Given('list of exits', function (callback) {
    callback();
    console.log("Checking exits.");
    hExits = vExits = [];
    if ('Horizontal' in externalDoors) {
        hExits = externalDoors.Horizontal;
    };
    if ('Vertical' in externalDoors) {
        vExits = externalDoors.Vertical;
    };
});

Then('each should be between 34 to 48 inches', function () {
    for (let i = 0; i < hExits.length; i++) {
        let width = hExits[i][1][1] - hExits[i][0][1];
        assert(width >= 34, `Exit is ${width} inches long.`);
        assert(width <= 48, `Exit is ${width} inches long.`);
        console.log(`Horizontal Exit ${i + 1}: ${width} inches wide`);
    };
    for (let i = 0; i < vExits.length; i++) {
        let width = vExits[i][2][0] - vExits[i][1][0];
        assert(width >= 34, `Exit is ${width} inches long.`);
        assert(width <= 48, `Exit is ${width} inches long.`);
        console.log(`Vertical Exit ${i + 1}: ${width} inches wide`);
    };
});

Then('I should say all exits are valid', function () {
    console.log('All exit doors are valid.');
});