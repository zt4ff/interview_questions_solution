const { SinglyLinkedList } = require("../../data_structures/linked_list");

describe("test the implemetation of linkedlist in JS", () => {
  const ll = new SinglyLinkedList();
  ll.add("1");
  ll.add("2");
  ll.add("3");

  test("list contains items", () => {
    expect(ll.print()).toEqual("3 2 1");
  });

  test("remove items", () => {
    ll.remove("2");
    expect(ll.print()).toEqual("3 1");
  });
});
