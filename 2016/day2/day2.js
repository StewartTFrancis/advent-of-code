(() => {
	var puzz1 = {
		'keypad': [[1,2,3], [4,5,6], [7,8,9]],
		'point': [1,1],
		'input': ['ULL','RRDDD','LURDL','UUUUD']
	};
	
	var puzz2 = {
		'keypad': [
			[   ,   ,'1',   ,   ], 
			[   ,'2','3','4',   ],
			['5','6','7','8','9'],
			[   ,'A','B','C',   ],
			[   ,   ,'D',   ,   ]
		],
		'point': [2,0],
		'input': ['ULL','RRDDD','LURDL','UUUUD']
	};
	
	var solve = (keypad, point, input)=>{
		var answer = ''; //Added a string output since console.log likes combining duplicate output.
		
		for(var line = 0; line < input.length; line++)
		{
			for(var step = 0; step < input[line].length; step++)
			{	
				switch(input[line][step]) /* Of course jagged arrays were next. */
				{
					case "U":
						point[0] = (keypad[point[0] - 1] && keypad[point[0] - 1][point[1]]) ? point[0] - 1 : point[0];
					break;
					case "D": 
						point[0] = (keypad[point[0] + 1] && keypad[point[0] + 1][point[1]]) ? point[0] + 1 : point[0];
					break;
					case "L": 
						point[1] = (keypad[point[0]][ point[1] - 1]) ?  point[1] - 1 : point[1];
					break;
					case "R": 
						point[1] = (keypad[point[0]][point[1] + 1]) ? point[1] + 1 : point[1];
				}
			}
			
			answer += keypad[point[0]][point[1]];
		}
		
		return answer;
	};

	console.log(solve(puzz1.keypad, puzz1.point, puzz1.input));
	console.log(solve(puzz2.keypad, puzz2.point, puzz2.input));
})();



