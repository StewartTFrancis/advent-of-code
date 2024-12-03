var inpt = [
	"abba[mnop]qrst",
	"abcd[bddb]xyyx",
	"aaaa[qwer]tyui",
	"ioxxoj[asdfgh]zxcvbn"
	];

((input) => {
	
	var bracketedContent = /\[(\w*)\]/g;
	var nonBracketedContent = /(\w+)\[|(\w+)\s?$/g;

	var regexHelper = (regex, string) => {
		var found = [], match;
		
		while(match = regex.exec(string))
			found.push(match[1] || match[2]); //nonBracketedContent has two capture groups. Coalesce them.
		
		return found;
	};
	
	var containsAbba = (segment) => {
		for(var i = 3; i < segment.length; i++) //I realize this can be optimized.
		if(segment[i] !== segment[i-1] && segment[i] == segment[i-3] && segment[i-1] == segment[i-2])
			return true;
		
		return false;
	};
	
	var supportsTLS = (ip) => {
		var bracketed = regexHelper(bracketedContent, ip); //If there is an ABBA set in a bracketed region, return false. (Don't even check non-bracketed regions)
		for(var i = 0; i < bracketed.length; i++)
			if(containsAbba(bracketed[i]))
				return false;
		
		var nonBracketed = regexHelper(nonBracketedContent, ip); //If there's an ABBA set in the non-bracket region, true.
		for(var i = 0; i < nonBracketed.length; i++)
			if(containsAbba(nonBracketed[i]))
				return true;
		
		return false; //Otherwise, neither, false
	};
	
	var findAbasReturnBabs = (segment) =>
	{
		var babs = [];
		for(var i = 2; i < segment.length; i++)
			if(segment[i] !== segment[i-1] && segment[i] == segment[i-2])
				babs.push(segment[i-1] + segment[i] + segment[i-1]);
			
		return babs;
	}
	
	var supportsSSL = (ip) => {
		var nonBracketed = regexHelper(nonBracketedContent, ip); //Find all the non-bracketed segments
		
		var babs = [];
		for(var i = 0; i < nonBracketed.length; i++)
			babs = babs.concat(findAbasReturnBabs(nonBracketed[i])); //Also aware I'm not checking for dupes. I wouldn't put this code in production.
		
		var bracketed = regexHelper(bracketedContent, ip); //Find bracketed segments
		for(var i = 0; i < bracketed.length; i++)
			for(var j = 0; j < babs.length; j++)
				if(bracketed[i].includes(babs[j]))
					return true;
				
		return false;		
	}
	
	var totalABBA = 0;
	var totalSSL = 0;
	
	for(var i = 0; i < input.length; i++)
	{
		// if(supportsTLS(input[i]))
			// totalABBA++;
		
		if(supportsSSL(input[i]))
			totalSSL++;
	}	
	
	//console.log(totalABBA);
	console.log(totalSSL);
})(inpt);