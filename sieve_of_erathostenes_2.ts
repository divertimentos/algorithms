// 1. Declare p to be prime, and cross off all the multiples of that number in the
// table, starting from p2;

// 2. Find the next number in the table after p that is not yet crossed off and set
// p to that number; and then repeat from step 1.

let numbers: Array<number> = [
  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
  // 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  // 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
  // 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
  // 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
  // 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
  // 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
  // 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
];

function sieve() {
  for (let i = 0; i < numbers.length; i++) {
    let iPointer = numbers[i];
    console.log(`\niPointer: ${iPointer}`);
    for (let j = 0; j < numbers.length; j++) {
      let jPointer = numbers[j];
      console.log(`jPointer: ${jPointer}`);
      console.log(`${iPointer} * ${jPointer} = ${iPointer * jPointer}`);
      numbers.splice(numbers.indexOf(iPointer * jPointer), 1);
      console.log(`\ncurrent numbers array: ${numbers}\n`);
    }
  }

  console.log(`FINAL NUMBERS ARRAY: ${numbers}`);
}

console.log(sieve());
