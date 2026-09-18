# Memory Leaks in Java

## What is a Memory Leak?

A **memory leak** happens when a Java program keeps references to objects that it **no longer needs**.

The important point is:

> **The Garbage Collector can only remove objects that are unreachable.**

If an object is still referenced by another object, the Garbage Collector considers it **reachable** and cannot reclaim its memory.

---

## Simple Example

```java
List<User> users = new ArrayList<>();

while (true) {
    users.add(new User());
}
```

Every loop creates a new `User` object:

```text
Heap

User 1 ← users
User 2 ← users
User 3 ← users
User 4 ← users
User 5 ← users
...
```

The `users` list still contains references to all these objects.

Therefore:

```text
User object
     ↓
still reachable
     ↓
GC cannot delete it
```

Eventually, the Heap can become full:

```text
Heap
████████████████████ 100%
                    ↓
             OutOfMemoryError
```

---

## Why Doesn't the Garbage Collector Fix It?

The Garbage Collector works by checking whether objects are still reachable.

```text
Object is reachable?
       │
   ┌───┴───┐
  YES      NO
   │        │
   ↓        ↓
 Keep     Reclaim
```

### Example: No Memory Leak

```java
User user = new User();

user = null;
```

Now the object has no reference:

```text
user variable
     ↓
    null

User object
     ↓
unreachable
     ↓
GC can reclaim it
```

### Example: Memory Leak

```java
List<User> users = new ArrayList<>();

User user = new User();

users.add(user);

user = null;
```

Even though `user` is now `null`, the object is still referenced by the list:

```text
user → null

users → List → User object
                  ↑
             still referenced
```

Therefore, the Garbage Collector **cannot reclaim the `User` object**.

---

# Common Causes of Memory Leaks

## 1. Static Collections

Static collections can keep objects alive for a long time.

```java
class Cache {

    static List<User> users = new ArrayList<>();
}
```

If we continuously add objects:

```java
Cache.users.add(new User());
```

the objects remain referenced by the static list.

```text
Static List
    │
    ├── User
    ├── User
    ├── User
    ├── User
    └── ...
```

---

## 2. Forgetting to Remove Objects from Collections

```java
List<User> users = new ArrayList<>();

users.add(user);
```

If the object is no longer needed but is never removed:

```java
users.remove(user);
```

the collection continues to hold the reference.

---

## 3. Listeners and Callbacks

Applications can register listeners:

```java
button.addListener(myListener);
```

If the listener is no longer needed but remains registered, it can keep other objects reachable.

This can prevent those objects from being garbage collected.

---

## 4. Caches

Caching can improve performance:

```java
Map<String, User> cache = new HashMap<>();
```

However, if the cache grows indefinitely:

```text
Cache
 ├── User
 ├── User
 ├── User
 ├── User
 ├── User
 └── ...
```

it can consume a large amount of memory.

Using a bounded cache or an appropriate eviction mechanism can help prevent this problem.

---

# Memory Leak vs Normal Garbage

## Normal Garbage

```text
Object
  ↓
No references
  ↓
Garbage Collector
  ↓
Memory reclaimed
```

## Memory Leak

```text
Object
  ↓
Unwanted reference still exists
  ↓
GC considers object reachable
  ↓
Object remains in memory
```

The important difference is **reachability**.

---

# Example That Can Cause OutOfMemoryError

```java
public class MemoryLeakExample {

    private static List<byte[]> data = new ArrayList<>();

    public static void main(String[] args) {

        while (true) {
            data.add(new byte[1024 * 1024]); // 1 MB
        }
    }
}
```

Each iteration creates a new **1 MB array**.

The array is then stored in the `data` list.

Because `data` is `static`, the list remains reachable, and the objects inside it remain reachable as well.

The process can eventually look like:

```text
Heap
 ↓
Memory usage increases
 ↓
GC runs
 ↓
Objects are still reachable
 ↓
GC cannot reclaim them
 ↓
Heap becomes full
 ↓
OutOfMemoryError
```

---

# Key Point

> **A memory leak in Java occurs when objects that are no longer needed remain reachable through references, preventing the Garbage Collector from reclaiming their memory.**

### Easy way to remember

```text
No reference
     ↓
Garbage
     ↓
GC can remove it

Unwanted reference
     ↓
Still reachable
     ↓
GC keeps it
     ↓
Memory Leak
```
