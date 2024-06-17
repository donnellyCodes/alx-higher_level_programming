#!/usr/bin/node
function findSecondBiggest(args) {
	let max = - Infinity, secondMax = -Infinity;
	args.forEach((args) => {
		const num = parseInt(arg, 10);
		if (num > max) {
			[secondMax, max] = [max, num];
		} else if (num > secondMax && num < max) {
			secondMax = num;
		}
	});
	return secondMax;
}
const args = process.argv.slice(2);
if (args.length < 2) {
	console.log(0);
} else {
	console.log(findSecondBiggest(args));
}
