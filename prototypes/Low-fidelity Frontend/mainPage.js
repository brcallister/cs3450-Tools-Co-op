document.title = "Tools Co-op";

// -- Build the title div at the top --
mainBox = document.getElementById("mainBox");
mainBox.setAttribute("class", "title-box");

title = document.createElement('h1');
title.textContent = "Tools Co-op";
mainBox.appendChild(title)


// -- Build Main Content for the page --
content = document.getElementById("main_content");
content.setAttribute("class", "main_text");

header = document.createElement('h2');
header.textContent = "Welcome";
content.appendChild(header);

words = document.createElement('p');
words.textContent = "Welcome to our site, this is some nice example text.";
content.appendChild(words);
