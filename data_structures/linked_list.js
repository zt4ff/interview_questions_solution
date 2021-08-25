class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor(head = null) {
    if (head) {
      this.head = new Node(head);
    } else {
      this.head = null;
    }
  }

  add(item) {
    const new_node = new Node(item);
    if (this.head) {
      new_node.next = this.head;
      this.head = new_node;
    } else {
      this.head = new_node;
    }
  }

  print() {
    let current = this.head;
    let str = "";
    while (current) {
      str = str + " " + current.data;
      current = current.next;
    }
    return str.trim();
  }

  remove(data) {
    if (!this.head) throw new Error("linkedlist is empty");
    if (this.head.data == data) {
      this.head = this.head.next;
    } else {
      let prev;
      let current = this.head;
      while (current) {
        prev = current;
        current = current.next;
        if (current.data == data) {
          prev.next = current.next;
          current = null;
          return;
        }
      }
    }
  }
}

exports.SinglyLinkedList = SinglyLinkedList;
