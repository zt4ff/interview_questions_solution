// Article can be found here: https://www.geeksforgeeks.org/leaders-in-an-array/

const solution = (arr, n) => {
  let ans = [];
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (arr[j] > arr[i]) return;
      ans.push(arr[i]);
    }
  }
};

export default solution;
