# Star Wars Characters Project

The **"0. Star Wars Characters"** project involves interacting with an external API to fetch and display information about Star Wars characters based on a movie ID provided as an argument. This project helps you practice key web programming concepts, API interactions, and asynchronous programming in JavaScript.

## Concepts Needed

### HTTP Requests in JavaScript
- Understanding how to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
- [A Complete Guide to Making HTTP Requests in Node.js](https://www.memberstack.com/blog/node-http-request)

### Working with APIs
- Understanding the basics of RESTful APIs and how to interact with them.
- Parsing JSON data returned by APIs.
- [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

### Asynchronous Programming
- Managing asynchronous operations with callbacks, promises, and async/await syntax.
- Handling API response data asynchronously.
- [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

### Command Line Arguments in Node.js
- Using the `process.argv` array to access command-line arguments passed to a Node.js script.
- [How to Parse Command Line Arguments in Node.js](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/)

### Array Manipulation and Iteration
- Iterating over arrays and manipulating data structures to format and display character names.
- [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.

## Additional Resources
- Mock Technical Interview

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

### More Info

#### Install Node 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard
```bash
$ sudo npm install semistandard --global
```

#### Install request module and use it
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
