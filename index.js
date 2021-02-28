// This is a JavaScript version of the Python script I wrote

const Discord = require('discord.js');
const client = new Discord.Client();

const yes = "Yes! LET'S GO!!!";
const no = "No, not yet!";
let evan_flag = false;

client.once('ready', () => {
    console.log('IIFY Bot loaded!');
});

// client.on('message', message => {
//     if (message.author === client.user) { return; }

//     if (message.author.id === '262687110853689355') { evan_flag = true; }
//     else { evan_flag = false; }

//     if (message.content.startsWith("is it ") || message.content.startsWith("Is it ")) {
//         let rest_of_message = message.content.substring(6); // Get the rest of the message
//         var date = new Date();
//         var today = date.getDay(); // Get day of the week as an integer (Sun: 0 - Sat: 6)

//         if (rest_of_message.includes("sunday") || rest_of_message.includes("Sunday") || rest_of_message.includes("sun") || rest_of_message.includes("Sun")) {
//             if (today === 0) { message.channel.send(yes); }
//             else { message.channel.send(no); }
//             return;
//         }
//         if (rest_of_message.includes("monday") || rest_of_message.includes("Monday") || rest_of_message.includes("mon") || rest_of_message.includes("Mon")) {
//             if (today === 1) { message.channel.send(yes); }
//             else { message.channel.send(no); }
//             return;
//         }
//         if (rest_of_message.includes("tuesday") || rest_of_message.includes("Tuesday") || rest_of_message.includes("tues") || rest_of_message.includes("Tues")) {
//             if (today === 2) { message.channel.send(yes); }
//             else { message.channel.send(no); }
//             return;
//         }
//         if (rest_of_message.includes("wednesday") || rest_of_message.includes("Wednesday") || rest_of_message.includes("wed") || rest_of_message.includes("Wed")) {
//             if (today === 3) { message.channel.send(yes); }
//             else { message.channel.send(no); }
//             return;
//         }
//         if (rest_of_message.includes("thursday") || rest_of_message.includes("Thursday") || rest_of_message.includes("thurs") || rest_of_message.includes("Thurs")) {
//             if (today === 4) { message.channel.send(yes); }
//             else { message.channel.send(no); }
//             return;
//         }
//         if (rest_of_message.includes("friday") || rest_of_message.includes("Friday") || rest_of_message.includes("fri") || rest_of_message.includes("Fri")) {
//             if (today === 5) { message.channel.send(yes); }
//             else { message.channel.send(no); }
//             return;
//         }
//         if (rest_of_message.includes("saturday") || rest_of_message.includes("Saturday") || rest_of_message.includes("sat") || rest_of_message.includes("Sat")) {
//             if (today === 6) { message.channel.send(yes); }
//             else { message.channel.send(no); }
//             return;
//         }

//         // If no date has been specified, send an error message
//         message.channel.send("Please enter a valid date.");

//         if (evan_flag === true) { message.channel.send("Are you excited for D&D day, Evan?"); }
//     }
// });

client.login('ODE1NDk2MDI5MDc5NjAxMTkz.YDtP3A.7IIj1go2lBlUpV5mBW_Km9KprT4');