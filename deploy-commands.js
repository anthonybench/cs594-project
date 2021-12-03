//-------------------------------------------
// deploy-commands.js
// 		-- Isaac Yep; CS-594 Project
//-------------------------------------------


//---Dependencies----------------------------
const fs = require('fs');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const { clientId, guildId, token } = require('./config.json');

//---Commands handler------------------------
const commands = [];
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	commands.push(command.data.toJSON());
}

//---Register--------------------------------
const rest = new REST({ version: '9' }).setToken(token);
rest.put(Routes.applicationGuildCommands(clientId, guildId), { body: commands })
	.then(() => console.log('Successfully registered application commands.'))
	.catch(error => {
		// gracefully catch and display errors
		console.log(`Error Code:            | ${error.code}`);
		console.log(`Error Message:         | ${error.rawError.message}`);
		console.log(`HTTP Status Code:      | ${error.status}`);
		console.log(`HTTP Method Attempted: | ${error.method.toUpperCase()}`);
		console.log(`API Endpoint:          | ${error.url}`);

		// check appropriate http method for endpoint
		if (error.method.toUpperCase() != 'PUT') {
			console.log(`Bot Application must interact with endpoint ${error.url} via PUT method.`);
		}

		// check application error codes
		let errcode = parseInt(error.code);
		if (errcode == 50035) {
			console.log("Invalid form body submitted; bad client-id (applicationo-id) or guild-id (server-id).");
		} else if (errcode == 0) {
			console.log("Unauthorized; bad token.")
		} else if (errcode == 10001) {
			console.log("Unknown account.")
		} else if (errcode == 10004) {
			console.log("Unknown server (guild).")
		} else if (errcode == 4010) {
			console.log("Websocket shard failure; bad connection.")
		}
		

		// check http status code, and return appropriate message
		let statcode = parseInt(error.status);
		if (statcode < 200 ) {
			console.log("---Informational response:");
			console.log("This interim response may indicate that the client should continue the request or ignore the response if the request is already finished.");
			console.log("This code may be may be sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.");
			console.log("This code may indicate that the server has received and is processing the request, but no response is available yet.");
		} else if (statcode > 299 && statcode < 400) {
			console.log("---Redirection response:");
			console.log("The URL of the requested resource may have been changed permanently. The new URL is given in the response.");
			console.log("It may be that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy.");
			console.log("May direct the client to get the requested resource at another URI with same method that was used in the prior request.");
		} else if (statcode > 399 && statcode < 500) {
			console.log("---Client Error response:");
			console.log("The client may not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource.")
			console.log("Can also be used for payment systems, if requesting assets behind a paywall and user has not authenticated payment.");
			console.log("The server may not find the requested resource. In the browser, this means the URL is not recognized.");
		} else {
			console.log("---Server Error response:");
			console.log("The server may have encountered a situation it does not know how to handle.")
			console.log("This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.")
			console.log("This error response is given when the server is acting as a gateway and cannot get a response in time.")
		}

		return `HTTP Status Code: ${statcode}, Application Error Code: ${errcode}`;
	})
	// .catch(console.error); // for demonstration purposes