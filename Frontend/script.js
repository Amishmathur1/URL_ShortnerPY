const form = document.getElementById("url-form");

form.addEventListener("submit", async (event) => {
event.preventDefault();

const response = await fetch("https://url-shortnerpy.onrender.com/shorten", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        homepage: document.getElementById("url").value
    })
});

const data = await response.json();
const shortUrl = document.getElementById("short-url");

shortUrl.innerText = data.new_url;
shortUrl.href = data.new_url;

});
