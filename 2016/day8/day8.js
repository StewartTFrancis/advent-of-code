var screen = (input, settings) => {
	var display = [[]];
	
	//init: zero out the screen.
	for(var y = 0; y < settings.height; y++)
	{
		display[y] = new Array(settings.width);
		display[y].fill(false, 0, settings.width);
	}
	
	var drawRect = (width, height) => {
		for(var y = 0; y < Math.min(height, settings.height); y++)
			display[y].fill(true, 0, width);
	};
	
	var shiftRow = (row, dist) => {
		dist %= settings.width;
		
		if(dist < 0) //Since we wrap shifting -2 is equivalent to shifting settings.width - 2
			dist += settings.width;
	
		display[row] = display[row].splice(settings.width -  dist).concat(display[row]);
	};
	
	var shiftCol = (col, dist) => {
		dist = -dist; //FML I wrote this backwards (So we shift up instead of down. Invert dist.)
		dist %= settings.height;
		
		if(dist < 0) //Since we wrap shifting -2 is equivalent to shifting settings.width - 2
			dist += settings.height;

		var holder = [];		
		for(var y = 0; y < settings.height; y++)
		{
			holder[y] = display[y][col];
			display[y][col] = ((y + dist) % settings.height < y) ? holder[(y + dist) % settings.height] : display[(y + dist) % settings.height][col];
		}
	};
	
	var getDisplay = () => {
		return display.reduce((output, col) => {
			return output += col.reduce((colOutput, row) => {
				return colOutput += row ? '#' : '.';
			}, '') + '\n';
		}, '');
	};
	
	var countPixels = () => { 
		return display.reduce((output, col) => {
				return output += col.reduce((colOutput, row) => {
					return colOutput += row ? 1 : 0;
				}, 0);
			}, 0);
	};
	
	for(var i = 0; i < input.length; i++)
	{
		/*
			This only makes sense looking at the the input:
			
			'rect 3x2',
			'rotate column x=1 by 1',
			'rotate row y=0 by 4',
			'rotate column x=1 by 1'
		*/
		
		var args = input[i].split(' '); //get first word, either rect or rotate
		
		switch(args[0]) //switch on rect/rotate
		{
			case 'rect': //if rect
				args = args[1].split('x'); //Split 3x2
				drawRect(+args[0], +args[1]); //pass in draw rect, +'3' === 3 (IE: +'string number' is a shorthand for Number parse)
				break;
			case 'rotate': //If rotate
				switch(args[1]) //switch on column/row
				{
					case 'column':
						shiftCol(+args[2].split('=')[1], +args[4]); //grab 'x=1', split on =, take number. Convert last number and run.
						break;
					case 'row':
						shiftRow(+args[2].split('=')[1], +args[4]);		
				}
		}
	}
	
	//output:
	console.log(getDisplay()); 
	console.log(countPixels());
};

screen([
	'rect 3x2',
	'rotate column x=1 by 1',
	'rotate row y=0 by 4',
	'rotate column x=1 by 1'
], {width: 7, height: 3});
