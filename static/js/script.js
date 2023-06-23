const headings = document.getElementsByClassName("heading");

for (let i = 0; i < headings.length; i++) {
  const heading = headings[i];
  const textContent = heading.textContent;
  const trimmedContent = textContent.replace(/^\s+|\s+$/g, '');
  const words = trimmedContent.split(/\s+/);
  words[2] = '<span class="title-design">' + words[2] + '</span>';
  words[7] = '<span class="title-design">' + words[7] + '</span>';
  heading.innerHTML = words.join(" ");
}
