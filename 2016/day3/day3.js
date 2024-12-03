//As in real life, of course the data needs to get cleaned first.
var inpt = [
 // Removed.
];

((input) => {
	var isPossible = (set) => {
		set.sort((a,b) => { return a-b; }); //Oh, JavaScript
		
		return (set[0] + set[1]) > set[2];
	};

	var count = 0;
	
	//part 1:
	for(var i = 0; i < input.length; i++)
		if(isPossible(input[i].split(' ').map((ele) => { return parseInt(ele); })))
			count++;

		console.log(count);

	//part 2:
	count = 0;
	var cleaned = [[]];
	
	var row = 0;
	var col = 0;
	
	//This can be refactored to not store the pivoted data... just change row = (i%3) + index;
	//and when col === 2 run isPossible on cleaned[0] -> cleaned[2];
	for(var i = 0; i < input.length; i++) 
	{
		input[i].split(' ').map((ele, index) => { 
			row =  (i - (i%3)) + index;
			col = i%3;
			
			if(!cleaned[row])
				cleaned[row] = [];
			
			cleaned[row][col] = parseInt(ele);
		});
	}	
	
	for(var i = 0; i<cleaned.length; i++)
		if(isPossible(cleaned[i]))
			count++;
			
	return count;
})(inpt);