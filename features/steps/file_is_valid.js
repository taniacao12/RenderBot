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
    const externalWalls = info.Features.External.Walls;
    const internalWalls = info.Features.Internal.Walls;
    let sum = 0;
    for (let item in externalWalls) {
        sum += Object.values(externalWalls[item]).flat().length;
    } for (let item in internalWalls) {
        sum += Object.values(internalWalls[item]).flat().length;
    }
    assert(sum >= 3, 'Less than three walls found in the file');
    console.log(`File contains ${sum} walls.`);
});

Then('it should have at least 1 door', function () {
    externalDoors = info.Features.External.Doors;
    const internalDoors = info.Features.Internal.Doors;
    let sum = 0;
    for (let item in externalDoors) {
        numExDoors = Object.values(externalDoors[item]).flat().length;
        sum += numExDoors;
    } for (let item in internalDoors) {
        sum += Object.values(internalDoors[item]).flat().length;
    }
    assert(sum > 0, 'No doors found in the file');
    console.log(`File contains ${sum} doors.`);
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
    hExits = vExits = {};
    if ('Horizontal' in externalDoors) {
        hExits = externalDoors.Horizontal;
    } if ('Vertical' in externalDoors) {
        vExits = externalDoors.Vertical;
    }
});

Then('each should be between 34 to 48 inches', function () {
    for (let item in hExits) {
        let coors = hExits[item].Coordinates;
        let width = Math.abs(coors[1][0] - coors[0][0]);
        assert(width >= 34, `Exit is ${width} inches long.`);
        assert(width <= 48, `Exit is ${width} inches long.`);
        console.log(`Horizontal Exit ${item} is ${width} inches wide`);
    };
    for (let item in vExits) {
        let coors = vExits[item].Coordinates;
        let width = Math.abs(coors[2][1] - coors[1][1]);
        assert(width >= 34, `Exit is ${width} inches long.`);
        assert(width <= 48, `Exit is ${width} inches long.`);
        console.log(`Vertical Exit ${item} is ${width} inches wide`);
    };
});

Then('I should say all exits are valid', function () {
    console.log('All exit doors are valid.');
});