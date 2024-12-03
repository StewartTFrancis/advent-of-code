function Bot (controller, number, slot, target, slot2, target2) {
	var _low, _high;
	
	var _holding = null;
	this. push = (chip) => { /* Why push? See 'processLine', we are either 'push'ing on a bot or an array. Easier to make the bot push than the array something else. */
		if(_holding === null)
			_holding = chip;
		else
		{
			controller.give(this, _low, Math.min(_holding, chip), _high, Math.max(_holding, chip));
			_holding = null;
		}
	};
	
	this.set = (slot, destination) =>
	{
		if(slot == 'high')
			_high = destination;
		else
			_low =  destination;
	};
	
	this.number = number;
	
	if(slot && target)
		this.set(slot, target);

	if(slot2 && target2)
		this.set(slot2, target2);
}

function Controller(input) {
	var _targets = {
		bot: [],
		output: []
	};

	var _watch = [];		
	
	var processLine = (line) =>
	{
		var cmd = line.split(' ');
		
		if(cmd[0] == 'bot') //0:bot 1:2 2:gives 3:low 4:to 5:bot 6:1 7:and 8:high 9:to 10:bot 11:0
		{
			var number = +cmd[1];
			
			var slot1 = cmd[3];
			var dest1 = {type: cmd[5], number: +cmd[6]}; 
			var slot2 = cmd[8];
			var dest2 = {type: cmd[10], number: +cmd[11]};
			
			if(!_targets.bot[number])
				_targets.bot[number] = new Bot(this, number, slot1, dest1, slot2, dest2);
		} else if (cmd[0] == 'value') //0:value 1:3 2:goes 3:to 4:bot 5:1
			_targets[cmd[4]][+cmd[5]].push(+cmd[1]);
	};
	
	this.run = () => {
		for(var i = 0; i < input.length; i++) //Run all the 'bot x give y' first... :-/ We have to do two passes, but we ensure we're not having a bot run off without having set a destination first.
			if(input[i][0] == "b")
				processLine(input[i]);
		
		for(var i = 0; i < input.length; i++) //Run all the values next
			if(input[i][0] == "v")
				processLine(input[i]);
	};
	
	var place = (dest, chip) => {
		if(dest.type == 'output' && !(_targets.output[dest.number]))
			_targets.output[dest.number] = [];
	
		_targets[dest.type][dest.number].push(chip);
	};
	
	this.give = (bot, low_dest, low_chip, high_dest, high_chip) =>
	{
		if(_watch[low_chip] && _watch[low_chip].includes(high_chip))
			console.log("Bot " + bot.number + " is comparing chip " + low_chip + " & chip " + high_chip);
		
		place(low_dest, low_chip);
		place(high_dest, high_chip);
	};
	
	this.watch = (chip1, chip2) =>
	{
		var low = Math.min(chip1, chip2);
		var high = Math.max(chip1, chip2);
		
		if(!_watch[low])
			_watch[low] = [];
		
		_watch[low].push(high);
	};
	
	this.getOutputs = () => _targets.output.slice();
}
	
function test(input) {
	var master = new Controller(input);
	master.watch(61, 17); //test1
	master.run();
	
	var output = master.getOutputs(); //test2
	console.log(output[0] * output[1] * output[2]);
}
	
test(['bot 76 gives low to bot 191 and high to bot 21']);