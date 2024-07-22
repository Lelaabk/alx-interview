#!/usr/bin/node
/* Prints all casts of Star Wars movie */

const req = require('request');
const swAPI = 'https://swapi-api.alx-tools.com/api/';
const endPoint = 'films/';
const movieID = process.argv[2].toString();

request(swAPI + endPoint + movieID, function (error, _, body) {
    if (error)
        console.error(error);
    const objects = JSON.parse(body);
    const casts = objects.characters;
    printRes(casts);
});

function printRes (casts, c = 0) {
    request(casts[c], function (error, _, body) {
        if (error)
            console.error(error);
        console.log(JSON.parse(body).name);
        if (++c < casts.length) {
            printRes(casts, c++);
        }
    });
}
