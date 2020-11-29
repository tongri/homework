let task = +prompt("Which task would u like 2 check? (1-4)");


switch (task){
	case 1:
		let a;
		do{
			a = confirm("Подтвердите действие");
		} while (a == false);
		break;

	case 2:
		let n = +prompt("Enter N: ");
		let array = [];

		for (let i = 0; i < n; i++){
			array.push(i**3);
			console.log(array[i]);
		}
		break;

	case 3:
		let new_n = +prompt("Enter N: ");
		let sum = 0;
		let step = 3;
		for (let i = 1; i <= new_n; i+=step){
			sum += i;
		}
		console.log("Sum is " + sum);
		break;

	case 4:
		let sharp = "#";
		let dot = ".";
		let is_even = 1;
		let height = +prompt("Enter height of chess desk");
		let width = +prompt("Enter width of chess desk");
		let boxes = [];
		for (let i = 0; i < height; i++){
			for (let j = 0; j < width; j++){
				if (is_even % 2){
					boxes.push(sharp, dot);
				}
				else {
					boxes.push(dot, sharp);
				}
			}
			console.log(boxes.join(''));
			is_even++;
			boxes = [];

		}
}