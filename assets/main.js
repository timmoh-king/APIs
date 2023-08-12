async function getJoke() {
  const url = "https://official-joke-api.appspot.com/random_joke";
  const request = new Request(url);
  const response = await fetch(request);
  const jokes = await response.json();

  const type = document.getElementById("type");
  const setup = document.getElementById("setup");
  const punchline = document.getElementById("punchline");

  setup.innerHTML = jokes.setup;
  punchline.innerHTML = jokes.punchline;
}

async function getTenJokes() {
  const url = "https://official-joke-api.appspot.com/random_ten";
  const request = new Request(url);
  const response = await fetch(request);
  const tenJokes = await response.json();

  const ul = document.getElementById("ul");
  for (i of tenJokes) {
    const li = document.createElement("li");
    li.innerHTML = `${i.setup} - ${i.punchline}`;
    ul.appendChild(li);
  }
}
