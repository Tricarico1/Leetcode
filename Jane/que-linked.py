"""
Jane Street Memoization Problem - Complete Solution

This demonstrates three levels of memoization:
1. Basic memoization with hash table
2. FIFO eviction with O(1) complexity
3. LRU eviction with O(1) complexity using doubly-linked list
"""

from collections import deque
from typing import Callable, Any, Optional


# ============================================================================
# PART 1: Basic Memoization
# ============================================================================

def memo_basic(f: Callable[[int], int]) -> Callable[[int], int]:
    """
    Basic memoization using a dictionary (hash table).
    
    Time: O(1) for lookups and insertions
    Space: O(n) where n is number of unique inputs - UNBOUNDED!
    
    Problem: Memory leak - cache grows forever
    """
    cache = {}
    
    def memoized(x: int) -> int:
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    
    return memoized


# ============================================================================
# PART 2: FIFO Eviction with O(1) Complexity
# ============================================================================

def memo_fifo(f: Callable[[int], int], max_size: int = 256) -> Callable[[int], int]:
    """
    Memoization with FIFO (First In First Out) eviction policy.
    
    Strategy:
    - Keep a queue to track insertion order
    - When cache exceeds max_size, dequeue oldest entry and remove from cache
    
    Time: O(1) for all operations
    Space: O(max_size)
    
    Trade-offs:
    - Simple to implement
    - Doesn't consider usage patterns
    - May evict frequently used items
    """
    cache = {}
    order_queue = deque()
    
    def memoized(x: int) -> int:
        # Cache hit
        if x in cache:
            return cache[x]
        
        # Cache miss - compute result
        result = f(x)
        
        # If at capacity, evict oldest (FIFO)
        if len(cache) >= max_size:
            oldest = order_queue.popleft()  # O(1)
            del cache[oldest]  # O(1)
        
        # Add new entry
        cache[x] = result
        order_queue.append(x)
        
        return result
    
    return memoized


# ============================================================================
# PART 3: LRU Eviction with O(1) Complexity - THE OPTIMAL SOLUTION
# ============================================================================

class Node:
    """Doubly-linked list node for LRU cache."""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    """
    LRU Cache using doubly-linked list + hash table.
    
    Key insight: Hash table provides O(1) lookup, doubly-linked list 
    provides O(1) reordering and eviction.
    
    Structure:
    - Hash table: {key -> Node}
    - Doubly-linked list: ordered by recency (head = most recent, tail = least recent)
    - Dummy head and tail nodes simplify edge cases
    
    Operations:
    - get(): O(1) - lookup in hash table, move to head
    - put(): O(1) - add to hash table and head, evict tail if needed
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Dummy head and tail nodes simplify operations
        self.head = Node(0, 0)  # Most recently used
        self.tail = Node(0, 0)  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        """Remove node from doubly-linked list. O(1)"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node) -> None:
        """Add node right after head (most recently used position). O(1)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_head(self, node: Node) -> None:
        """Move existing node to head (mark as recently used). O(1)"""
        self._remove(node)
        self._add_to_head(node)
    
    def get(self, key: int) -> Optional[int]:
        """Get value and mark as recently used. O(1)"""
        if key not in self.cache:
            return None
        
        node = self.cache[key]
        self._move_to_head(node)  # Update recency
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """Add/update key-value pair. O(1)"""
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # Evict LRU if over capacity
            if len(self.cache) > self.capacity:
                # Remove from tail (least recently used)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]


def memo_lru(f: Callable[[int], int], max_size: int = 256) -> Callable[[int], int]:
    """
    Memoization with LRU (Least Recently Used) eviction policy.
    
    Strategy:
    - Use LRUCache which combines hash table + doubly-linked list
    - Hash table: O(1) lookups
    - Doubly-linked list: O(1) reordering and eviction
    
    Time: O(1) for all operations (get, put, evict)
    Space: O(max_size)
    
    Why this is optimal:
    - Evicts least recently used items (better than FIFO)
    - All operations are O(1) (better than O(n) linear scan or O(log n) heap)
    - Adapts to usage patterns
    """
    lru_cache = LRUCache(max_size)
    
    def memoized(x: int) -> int:
        # Try to get from cache
        cached_result = lru_cache.get(x)
        if cached_result is not None:
            return cached_result
        
        # Cache miss - compute and store
        result = f(x)
        lru_cache.put(x, result)
        return result
    
    return memoized


# ============================================================================
# Testing and Examples
# ============================================================================

def expensive_function(x: int) -> int:
    """Simulates an expensive computation."""
    print(f"  Computing f({x})...")
    return x * x


def test_memo_solutions():
    """Test all three memoization approaches."""
    
    print("=" * 60)
    print("PART 1: Basic Memoization")
    print("=" * 60)
    f1 = memo_basic(expensive_function)
    print("Call f(5):")
    print(f"Result: {f1(5)}")
    print("Call f(5) again:")
    print(f"Result: {f1(5)}")  # Should not recompute
    print()
    
    print("=" * 60)
    print("PART 2: FIFO Eviction (max_size=3)")
    print("=" * 60)
    f2 = memo_fifo(expensive_function, max_size=3)
    print("Computing f(1), f(2), f(3):")
    print(f"f(1) = {f2(1)}")
    print(f"f(2) = {f2(2)}")
    print(f"f(3) = {f2(3)}")
    print("\nCache is full. Now call f(4) - should evict f(1):")
    print(f"f(4) = {f2(4)}")
    print("\nCall f(1) again - should recompute (was evicted):")
    print(f"f(1) = {f2(1)}")
    print()
    
    print("=" * 60)
    print("PART 3: LRU Eviction (max_size=3)")
    print("=" * 60)
    f3 = memo_lru(expensive_function, max_size=3)
    print("Computing f(1), f(2), f(3):")
    print(f"f(1) = {f3(1)}")
    print(f"f(2) = {f3(2)}")
    print(f"f(3) = {f3(3)}")
    print("\nAccess f(1) to mark as recently used:")
    print(f"f(1) = {f3(1)}")
    print("\nNow call f(4) - should evict f(2) (least recently used):")
    print(f"f(4) = {f3(4)}")
    print("\nCall f(2) again - should recompute (was evicted):")
    print(f"f(2) = {f3(2)}")
    print("\nCall f(1) again - should still be cached:")
    print(f"f(1) = {f3(1)}")
    print()


# ============================================================================
# Complexity Analysis Summary
# ============================================================================

"""
COMPLEXITY COMPARISON:

Basic Memoization:
  - Lookup: O(1)
  - Insert: O(1)
  - Eviction: N/A (unbounded)
  - Space: O(∞) - MEMORY LEAK!

FIFO Eviction:
  - Lookup: O(1)
  - Insert: O(1)
  - Eviction: O(1)
  - Space: O(max_size)
  - Pros: Simple, bounded memory
  - Cons: Doesn't consider usage patterns

LRU Eviction:
  - Lookup: O(1)
  - Insert: O(1)
  - Eviction: O(1)
  - Space: O(max_size)
  - Pros: Optimal eviction policy, all O(1) operations
  - Cons: More complex implementation

WHY LRU WITH DOUBLY-LINKED LIST IS OPTIMAL:

1. Hash Table alone: O(1) lookup, but can't track order efficiently
2. Array/List: Can track order, but removal is O(n)
3. Heap: Can prioritize by timestamp, but update is O(log n)
4. Doubly-Linked List + Hash Table: BEST OF BOTH WORLDS
   - Hash table: O(1) lookup
   - Doubly-linked list: O(1) removal and reordering
   - Combined: All operations are O(1)!

The key insight is that we need TWO data structures:
- Hash table maps keys to nodes for O(1) lookup
- Doubly-linked list maintains order for O(1) eviction/reordering
"""


if __name__ == "__main__":
    test_memo_solutions()


