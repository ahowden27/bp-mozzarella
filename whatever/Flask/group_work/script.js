// const { Configuration, OpenAIApi } = require("openai");
// // import { Configuration, OpenAIApi } from "openai";

// const configuration = new Configuration({
//   apiKey: "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",
// });

// const openai = new OpenAIApi(configuration);

document.getElementById("button").style.display = "none";

// button information send
info = document.getElementById('info');
function movie_info() {
  make_prompt(info.value, "movie");
}
function book_info(){
  make_prompt(info.value, "book");
}
function song_info(){
  make_prompt(info.value, "song");
}

function make_prompt(nameOfThing, typeOfThing) {
  console.log("find the title of 3 " + typeOfThing + "s similar to " + nameOfThing);
  document.getElementById("button").innerHTML = "find the title of 3 " + typeOfThing + "s similar to " + nameOfThing;
}