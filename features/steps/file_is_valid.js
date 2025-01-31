const { Given, When, Then } = require('@cucumber/cucumber');
const fs = require('fs');
const assert = require('assert');
const readline = require('readline');

let filePath, info, walls, doors, exits;

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
});

Then('it should have at least 3 walls', function () {
    walls = info.Features.Walls;
    let num = Object.values(walls).length;
    assert(num >= 3, 'Less than three walls found in the file');
    console.log(`File contains ${num} walls.`);
});

Then('it should have at least 1 door', function () {
    doors = info.Features.Doors;
    let num = Object.values(doors).length;
    assert(num > 0, 'No doors found in the file');
    console.log(`File contains ${num} doors.`);
});

Then('at least 1 door should be an exit', function () {
    exits = {}
    let num = 0
    for (let feature in doors) {
        if (doors[feature].Program == 'Exterior Door') {
            exits[feature] = doors[feature];
            num++;
        }
    }
    assert(num > 0, 'No exits found in the file');
    console.log(`File contains ${num} exits.`);
});

Then('I should say the file is valid', function () {
    console.log('File is valid.');
});

Given('list of exits', function (callback) {
    callback();
    console.log("Checking exits.");
});

Then('each should be between 34 to 48 inches', function () {
    for (let feature in exits) {
        if (doors[feature].Orientation == 'Horizontal') {
            let coors = doors[feature].Coordinates;
            let width = Math.abs(coors[1][0] - coors[0][0]);
            assert(width >= 34, `Exit is ${width} inches long.`);
            assert(width <= 48, `Exit is ${width} inches long.`);
            console.log(`Exit ${feature} is ${width} inches wide.`);
        } else if (doors[feature].Orientation == 'Vertical') {
            let coors = doors[feature].Coordinates;
            let width = Math.abs(coors[2][1] - coors[1][1]);
            assert(width >= 34, `Exit is ${width} inches long.`);
            assert(width <= 48, `Exit is ${width} inches long.`);
            console.log(`Exit ${feature} is ${width} inches wide.`);        }
    }
});

Then('I should say all exits are valid', function () {
    console.log('All exit doors are valid.');
});