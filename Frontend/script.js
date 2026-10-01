// const response = await fetch("https://127.0.0.1:8000/shorten", {
//     method: "POST",
//     headers: {
//         "content-type": "application/json"
//     },
//     body: JSON.stringify({
//         url: document.getElementById("url").value
//     })
// });
//
// const data = await response.json();
//
// const shortUrl = document.getElementById("short-url");
//
// shortUrl.innerText = data.new_url;
// shortUrl.href = data.new_url;
//
// const form = document.getElementById("url-form");
//
// form.addEventListener("submit", async (event) => {
// event.preventDefault();


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
