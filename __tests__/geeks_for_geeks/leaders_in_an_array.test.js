const {
  solution1,
  solution2,
} = require("../../geeks_for_geeks/leaders_in_an_array");

test("test leaders in an array - solution 1", () => {
  expect(solution1([1, 2, 3, 4, 0], 5)).toEqual([4, 0]);
});

test("test leaders in an array - solution 2", () => {
  expect(solution2([1, 2, 3, 4, 0], 5)).toEqual([4, 0]);
});
