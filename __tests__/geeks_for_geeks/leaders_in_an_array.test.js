const solution = require("../../geeks_for_geeks/leaders_in_an_array");

test("test leaders in an array", () => {
  expect(solution([1, 2, 3, 4, 0], 5)).toMatch([4, 0]);
});
