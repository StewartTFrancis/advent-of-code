var runTest = (input) => {
	var decompressLength1 = (message) => {
		var len = 0, i = 0;
		var iopen = 0, iclose = 0;
		var expando;
		
		while((iopen = message.indexOf('(', i)) != -1 && (iclose = message.indexOf(')', iopen)) != -1)
		{	
			len += (iopen - i); //Assume the difference is all literal
						
			expando = message.substr(iopen + 1, iclose - iopen - 1).split('x');
			
			len += +expando[0] * +expando[1];
			i = iclose + +expando[0] + 1;
		}
		len += message.length - i; //again, diff is literal.
		return len;
	};
	
	var decompressLength2 = (message, i, end, repeat) => {
		i = i || 0;
		end = end || message.length;
		repeat = repeat || 1;

		var len = 0;
		var iopen = 0, iclose = 0;
		var expando;
		
		while((iopen = message.indexOf('(', i)) != -1 && iopen < end && (iclose = message.indexOf(')', iopen)) != -1)
		{	
			len += (iopen - i); //Assume the difference is all literal
						
			expando = message.substr(iopen + 1, iclose - iopen - 1).split('x');
			
			i = iclose + 1;
			len += decompressLength2(message, i, i + +expando[0], +expando[1]);
			i += +expando[0];
		}
		len += (end - i); //again, diff is literal.
		return len * repeat;
	};
	
	
	
	for(var i = 0; i < input.length; i++)
	{
		//console.log(decompressLength1(input[i]));
		console.log(decompressLength2(input[i]));
	}
};

runTest(['(27x3)ZFPNOWLAEAEMVDZHFYHXDUVOFWJ']);