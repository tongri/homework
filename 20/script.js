
const search = (input) =>{
	let response = fetch(`http://api.tvmaze.com/search/shows?q=${input}`);
	response
		.then((data) => {
			return data.json();
		})
		.then(items => {
			console.log(items);
		})
}

let button = document.getElementById('search');
const body = document.querySelectorAll('body');

button.addEventListener('click', () => {
	let input = document.getElementById('film').value;
	console.log(input);
	let response = fetch(`http://api.tvmaze.com/search/shows?q=${input}`);
	response
		.then((data) => {
			return data.json();
		})
		.then(items => {
			console.log(items);
			for (let i = 0; i < items.length; i++){
				let div_f_film = document.createElement("div");
				body[0].appendChild(div_f_film);
				div_f_film.className = 'single';
				img = document.createElement("img");
				h3 = document.createElement("h3");
				h3.innerText = items[`${i}`]['show']['name'];
				div_f_film.appendChild(h3);
				if (items[`${i}`]['show']['image'] !== null){
					img = document.createElement("img");
					div_f_film.appendChild(img);
					img.src = items[`${i}`]['show']['image']['original'];
					div_f_film.style.height = "550px";
				}
			}
		})
});
