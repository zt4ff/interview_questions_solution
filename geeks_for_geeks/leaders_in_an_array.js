// Article can be found here: https://www.geeksforgeeks.org/leaders-in-an-array/

// Solution 1 - simple or brute force method
// Time complexity: O(n * n)
const solution1 = (arr, n) => {
  let ans = [];
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (arr[j] >= arr[i]) break;
      ans.push(arr[i]);
    }
  }
  ans.push(arr[n - 1]);
  return ans;
};

// solution 2 - max from right
// Time Complexity: O(n)
const solution2 = (arr, n) => {
  let max_number = arr[n - 1];
  let ans = [max_number];
  for (let i = n - 2; i >= 0; i--) {
    // check if the next right number is greater than the max_number
    if (arr[i] > max_number) {
      max_number = arr[i];
      ans.unshift(max_number);
    }
  }

  return ans;
};

exports.solution1 = solution1;
exports.solution2 = solution2;
