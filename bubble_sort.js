let lista = [5, 4, 6, 3, 7, 1, 9, 0, 10];

let bubbleSort = (inputArr) => {
  let len = inputArr.length;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (inputArr[j] > inputArr[j + 1]) {
        let aux = inputArr[j];
        inputArr[j] = inputArr[j + 1];
        inputArr[j + 1] = aux;
      }
    }
  }
  return inputArr;
};

console.log(bubbleSort(lista));
