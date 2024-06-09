#!/usr/bin/node

const request = require('request');

const API_URL = 'https://swapi.dev/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];

  request(`${API_URL}/films/${movieId}/`, (err, res, body) => {
    if (err) {
      console.error(`Error fetching movie data: ${err}`);
      process.exit(1);
    }

    if (res.statusCode !== 200) {
      console.error(`Failed to fetch movie data, HTTP Status Code: ${res.statusCode}`);
      process.exit(1);
    }

    let movieData;
    try {
      movieData = JSON.parse(body);
    } catch (parseErr) {
      console.error(`Error parsing movie data: ${parseErr}`);
      process.exit(1);
    }

    const characterUrls = movieData.characters;

    const characterPromises = characterUrls.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (requestErr, response, characterBody) => {
          if (requestErr) {
            reject(`Error fetching character data: ${requestErr}`);
          } else if (response.statusCode !== 200) {
            reject(`Failed to fetch character data, HTTP Status Code: ${response.statusCode}`);
          } else {
            try {
              const characterData = JSON.parse(characterBody);
              resolve(characterData.name);
            } catch (parseErr) {
              reject(`Error parsing character data: ${parseErr}`);
            }
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((promiseErr) => {
        console.error(`Error processing character requests: ${promiseErr}`);
        process.exit(1);
      });
  });
} else {
  console.error("Error: Movie ID argument is required.");
  process.exit(1);
}
