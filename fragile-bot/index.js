//-------------------------------------------
// index.js
// 		-- Isaac Yep; CS-594 Project
//-------------------------------------------


//---Dependencies---------------------------
const fs = require('fs');
const { Client, Collection, Intents } = require('discord.js');
const { token } = require('./config.json');
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

//---Commands handler------------------------
client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	client.commands.set(command.data.name, command);
}

//---Execution-------------------------------
// ready
client.once('ready', () => {
	console.log('Ready!');
});

// Handlers
client.on('guildDelete', () => {
	console.log("Error! Server has been destroyed!");
	console.log("Exiting, ever so gracefully...");
	client.destroy();
	return 10004;
})
client.on('guildUnavailable', () => {
	console.log("Error! Server has crashed!");
	console.log("Exiting, ever so gracefully...");
	client.destroy();
	return 10004; // bad data body error-code
})
client.on('shardError', (error, shardId) => {
	console.log(`Error! ${error.code}. Websocket disruption with shard: ${shardId}`);
	client.destroy();
	return 4010; // websocket shard failure error-code
})
client.on('interactionCreate', async interaction => {
	if (!interaction.isCommand()) return;

	const command = client.commands.get(interaction.commandName);

	if (!command) return;

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		return interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
	}
});

// Login
client.login(token).catch(console.error);