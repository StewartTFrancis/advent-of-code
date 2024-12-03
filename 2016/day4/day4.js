var inpt =[
	"aaaaa-bbb-z-y-x-123[abxyz]",
	"a-b-c-d-e-f-g-h-987[abcde]",
	"not-a-real-room-404[oarel]",
	"totally-real-room-200[decoy]"
];

((input)=>{
	var generateChecksum = (str) =>{
		var counts = [];
		
		for(var i = 0; i < str.length; i++)
		{
			var cc = str.charCodeAt(i);
			
			if(str[i] === '-')
				continue;
			else if(!(cc in counts))
				counts[cc] = { 'charCode': cc, 'count': 0 }; //This pains me a bit.
			
			counts[cc].count++;
		}
		
		counts.sort((a,b)=>{
			return (a.count !== b.count) ? b.count - a.count : a.charCode - b.charCode; //NOTE! b.count - a.count is reverse!
		});
		
		if(!counts[4])
			return '';
		
		return String.fromCharCode(counts[0].charCode, counts[1].charCode, counts[2].charCode, counts[3].charCode, counts[4].charCode);
	};
	
	var sectorTotal = 0;
	
	var shift = 0;
	var currStr = "";
	var newStr = "";
	for(var i=0; i < input.length;i++)
	{
		var lastDash = input[i].lastIndexOf('-');
		var bracket = input[i].indexOf('[');
		var calculatedChksum = generateChecksum(input[i].substr(0, lastDash));
		var parsedChksum = input[i].substr(bracket + 1, 5);
				
		if(calculatedChksum == parsedChksum)
		{
			//part 1:
			sectorTotal += parseInt(input[i].substr(lastDash + 1, bracket - (lastDash + 1)));
			
			//part 2:
			shift = parseInt(input[i].substr(lastDash + 1, bracket - (lastDash + 1)));
			currStr = input[i].substr(0, lastDash);
			newStr = "";
			for(var j = 0; j < currStr.length; j++)
			{
				if(currStr[j] == '-')
					newStr = newStr.concat(' ');
				else
					newStr = newStr.concat(String.fromCharCode((((currStr.charCodeAt(j) - 97) + shift) % 26) + 97));
			}
			
			console.log(input[i].substr(lastDash + 1, bracket - (lastDash + 1)), newStr);
			
		}
	}
	
	return sectorTotal;
})(inpt);