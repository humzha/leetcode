from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int
    prev: 'Node | None' = None
    next: 'Node | None' = None

class LRUCache:
    """Solution for designing a Least Recently Used (LRU) cache.

    Implement the `LRUCache` class with the following behavior:
    - `LRUCache(capacity)`: Initialize the cache with a positive integer capacity.
    - `get(key)`: Return the value associated with `key` if it exists; otherwise return −1.
    - `put(key, value)`: Update or insert the key‑value pair. If insertion causes the number
      of keys to exceed the capacity, evict the least recently used key. Both `get` and
      `put` must run in O(1) average time complexity.
    """

    def __init__(self, capacity: int):
        """Initializes the LRU cache with the given capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        # Most recently used
        self.head = Node(-1, -1)
        # LRU
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache: dict[int, Node] = {}
        self.capacity = capacity

    def _remove(self, key: int) -> Node | None:
        """
        Deletes node from the DLL
        
        Returns:
            Node | None: None if key doesn't exist
        """
        if key not in self.cache:
            return None

        node = self.cache[key]
        p, n = node.prev, node.next
        p.next, n.prev = n, p
        del self.cache[key]
        
        return node
    
    def _appendleft(self, node: Node):
        """
        Also sets the key in the cache to the node
        """
        p, n = self.head, self.head.next
        p.next, n.prev = node, node
        node.prev, node.next = p, n
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        """Retrieves the value associated with the provided key.

        Args:
            key (int): The key to look up in the cache.

        Returns:
            int: The value of the key if found; −1 otherwise.
        """
        if key not in self.cache:
            return -1

        node = self._remove(key)
        self._appendleft(node)
        
        return node.val

    def put(self, key: int, value: int)-> None:
        """Inserts or updates a key‑value pair in the cache.

        If the key already exists, update its value. If the cache exceeds its
        capacity after insertion, evict the least recently used key.

        Args:
            key (int): The key to insert or update.
            value (int): The value associated with the key.

        Returns:
            None: Modifies the cache in place.
        """
        if key in self.cache:
            self._remove(key)

        node = Node(key, value)
        self._appendleft(node)
        
        if len(self.cache) > self.capacity:
            self._remove(self.tail.prev.key)