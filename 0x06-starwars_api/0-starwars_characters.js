#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error("Error: Movie ID is required.");
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. HTTP Status Code: ${response.statusCode}`);
    process.exit(1);
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    if (!characters || characters.length === 0) {
      console.log("No characters found for the provided movie ID.");
      process.exit(1);
    }

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(`Error fetching character data: ${error.message}`);
          return;
        }

        if (response.statusCode !== 200) {
          console.error(`Failed to fetch character data. HTTP Status Code: ${response.statusCode}`);
          return;
        }

        try {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } catch (error) {
          console.error(`Error parsing character data: ${error.message}`);
        }
      });
    });
  } catch (error) {
    console.error(`Error parsing movie data: ${error.message}`);
  }
});
