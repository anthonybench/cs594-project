# **CS-594 Project**
*Internetowrking Protocols; Portland State University*

<br />

### Welcome to my term project
<hr>

This project, for CS-594 Internetworking Protocols at Portland State University for fall-2021 focuses on the networking aspects of chat applications, through the development of a Discord chat bot!

As per my agreement and approval from the instructor, **Dr. Nirupama Bulusu**, the following list enumerates the 17 promised features/requirements of the application (with the extra credit features):

- [X] Bot can connect to server
- [X] Bot can create a channel
- [X] Bot can list all channels
- [X] Bot can join a channel
- [X] Bot can leave a channel
- [X] Bot can list members of channel
- [X] Multiple bots can connect to a server
- [X] Bot can send messages to a room
- [X] Bot can join multiple channels
- [X] Bot can send distinct messages to multiple selected channels
- [X] Bot can disconnect from server
- [X] Bot can kick users
- [X] Bot can gracefully handle mis-use from users
- [X] Bot can gracefully handle bot-server-crashes
- [X] Programming Style (*Proofread three times*)
- [X] Bot can DM users 🔥 ***Extra Credit***
- [X] Bot can deliver files 🔥 ***Extra Credit***

<br />

### **Table of Contents** 📖
<hr>

  - [Welcome](#welcome-to-my-term-project)
  - [**Get Started**](#get-started-)
  - [Usage](#usage-)
  - [Technologies](#technologies-)
  - [Contribute](#Contribute-)
  - [Acknowledgements](#acknowledgements-)
  - [License/Stats/Author](#license-stats-author-)

<br />

### Get Started 🚀
<hr>

You may fetch the dependencies (enumerated in the dependencies section) with:
```bash
npm install
```
as well as
```bash
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```

To run the the Javascript supported features, you may launch the node server application with:
```bash
node ./deploy-commands.js;
wait;
node ./index.js
```
And visit the Discord Server *`Isaac Yep`* (by invitation only) to interact with it's client-server features powered by the JS API.

To interact with the python API features, simply run (there are `zsh` shell for each pythons file) the file name for each feature you want to turn a listener on for. \
Example:
```bash
./python-functions/list-channels.py
```

<br />

### Usage ⚙
<hr>

<details>
  <summary>
  ✅ Bot can connect to server
  </summary>

  `./python-functions/main.py` \
  `node index.js`
</details>

<!-- 2 -->
<details>
  <summary>
  ✅ Bot can create a channel
  </summary>

  `./python-functions/main.py` \
  `>> create-channel <channel_to_clone> <new_channel_name>`
</details>

<!-- 3 -->
<details>
  <summary>
  ✅ Bot can list all channels
  </summary>

  `./python-functions/main.py` \
  `>> list-channels`
</details>

<!-- 4 -->
<details>
  <summary>
  ✅ Bot can join a channel
  </summary>

  `./python-functions/main.py` \
  `node index.js` \
  *Setting the appropriate permssions in the invite link.*
</details>

<!-- 5 -->
<details>
  <summary>
  ✅ Bot can leave a channel
  </summary>

  `python-functions/main.py` \
  `>> /logout` \
  *Setting the appropriate permssions in the invite link. Also can be kicked.*
</details>

<!-- 6 -->
<details>
  <summary>
  ✅ Bot can list members of channel
  </summary>

  `./python-functions/main.py` \
  `>> list-members`
</details>

<!-- 7 -->
<details>
  <summary>
  ✅ Multiple bots can connect to a server
  </summary>

  `./python-functions/main.py` \
  `./second-bot/dm-user.py` (another shell) \
  `>> list-members` \
  `>> dm-user`
</details>

<!-- 8 -->
<details>
  <summary>
  ✅ Bot can send messages to a room
  </summary>

  `./python-functions/main.py` \
  `>> message-channels <channels>` \
</details>

<!-- 9 -->
<details>
  <summary>
  ✅ Bot can join multiple channels
  </summary>

  *Bot invite link is built with calculated permission code (can monitor any channel)*
</details>

<!-- 10 -->
<details>
  <summary>
  ✅ Bot can send distinct messages to multiple selected channels
  </summary>

  `./python-functions/main.py` \
  `>> message-channels <channels>`
</details>

<!-- 11 -->
<details>
  <summary>
  ✅ Bot can disconnect from server
  </summary>

  `python-functions/main.py` \
  `>> /logout` \
  *Setting the appropriate permssions in the invite link. Also can be kicked.* \
  *Also through error handling, in crash or disconnection events.* \
</details>

<!-- 12 -->
<details>
  <summary>
  ✅ Bot can kick users
  </summary>

  `node index.js`
  `>> /kick @USER_NAME` will remove the user from the guild (server).
</details>

<!-- 13 -->
<details>
  <summary>
  ✅ Bot can gracefully handle mis-use from users
  </summary>

  `node index.js`
  `>> /kick @floopyflop` \
  --> try using bad bot token \
  *bot will handle http errors in a multitude of wasy, and display helpful info per mis-use/error of user*
</details>

<!-- 14 -->
<details>
  <summary>
  ✅ Bot can gracefully handle bot-server-crashes
  </summary>

  --> create new server \
  --> server id \
  --> authenticate with https://discord.com/api/oauth2/authorize?client_id=916175763621965885&permissions=8&scope=bot%20applications.commands \
  --> set new guild-id, and login \
  --> crash (destroy) the server with bot logged in. \
  *bot will catch the error event and exit gracefully*
</details>

<!-- 15 -->
<details>
  <summary>
  ✅ Programming Style
  </summary>

  Developed with eslint, follows consistant style, proofread 4 times after testing.
</details>

<!-- 16 -->
<details>
  <summary>
  ✅ Bot can DM users 🔥 ***Extra Credit***
  </summary>

  `./python-functions/main.py` \
  `>> dm-me`
</details>

<!-- 17 -->
<details>
  <summary>
  ✅ Bot can deliver files 🔥 ***Extra Credit***
  </summary>

  `./python-functions/main.py` \
  `>> deliver-file`
</details>

<br />

### Technologies 🧰
<hr>

  - [@discordjs/builders: ^0.8.2](https://www.npmjs.com/package/@discordjs/builders)
  - [@discordjs/rest": ^0.1.0-canary.0](https://www.npmjs.com/package/@discordjs/rest)
  - [discord-api-types](https://www.npmjs.com/package/discord-api-types)
  - [discord.js: ^13.3.1](https://discord.js.org/#/docs/main/stable/general/welcome)
  - [dotenv: ^10.0.0](https://www.npmjs.com/package/dotenv)

<br />

### Contribute 🤝
<hr>

There is no interest from the author to recieve/review PR's for this project at this time. \
This repository purley serves as a school project.

<br />

### Acknowledgements 💙
<hr>

I'd like to thank ***Dr. Nirupama Bulusu*** for providing such an excellent ***Internetworking Protocols*** class at *Portland State University*!

<br />

### License, Stats, Author 📜
<hr>

<img align="right" alt="example image tag" src="https://i.imgur.com/jtNwEWu.png" width="200" />

<!-- badge cluster -->

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/anthonybench/cs594-project)
![GitHub repo size](https://img.shields.io/github/repo-size/anthonybench/cs594-project)
![GitHub](https://img.shields.io/github/license/anthonybench/cs594-project)

<!-- / -->
See [License](https://opensource.org/licenses/MIT) for the full license text.

This repository was authored by *Isaac Yep*.

[Back to Table of Contents](#table-of-contents-)