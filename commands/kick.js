//---Dependencies-------------
const { SlashCommandBuilder } = require('@discordjs/builders');

//---Execution----------------
module.exports = {
	data: new SlashCommandBuilder()
		.setName('kick')
		.setDescription('Select a member and kick them from the server.')
		.addUserOption(option => option.setName('target').setDescription('The member to kick')),
	async execute(interaction) {
		const user = interaction.options.getUser('target');
		// await interaction.reply({ content: `Kicking ${user.username}...`, ephemeral: true });
    await interaction.options.getMember('target').kick();
    return interaction.reply({ content: `${user.username} kicked!`, ephemeral: true });
	},
};