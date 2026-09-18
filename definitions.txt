# Java Memory Management — Definitions

### Memory Management

The process of allocating, using, and releasing memory during program execution.

### JVM

The Java Virtual Machine is the environment that executes Java bytecode and manages Java program execution and memory.

### RAM

Random Access Memory is the computer's temporary memory used by running programs.

### Stack

A memory area used mainly to manage method execution, including method frames, local variables, parameters, and references.

### Stack Frame

A memory structure created for each method call that contains the information required to execute that method.

### Thread

An independent unit of execution in a program. Each thread has its own Stack.

### Local Variable

A variable declared inside a method, constructor, or block whose scope is limited to that area.

### Heap

A memory area used mainly to store objects and arrays created during program execution.

### Object

An instance of a class created during program execution and generally stored in the Heap.

### Reference

A value that allows a program to access an object.

### Garbage Collector

A JVM mechanism that automatically identifies unreachable objects and reclaims the memory they occupy.

### Garbage Collection

The process of identifying unreachable objects and reclaiming the memory associated with them.

### Garbage

An object that is no longer reachable from any GC Root and is therefore eligible for Garbage Collection.

### GC Root

A starting point used by the Garbage Collector to determine which objects are still reachable.

### Reachability

The ability to access an object by following references from a GC Root.

### Memory Leak

A situation where a program keeps unnecessary references to objects, preventing the Garbage Collector from reclaiming their memory.

### null

A special value that indicates that a reference does not point to an object.

### Metaspace

A JVM memory area used to store metadata about loaded classes.

### Memory Allocation

The process of reserving memory for data required by a program.

### Memory Reclamation

The process of making memory available again after it is no longer needed.

### Stop-the-World

A period during which application threads are temporarily paused while the JVM performs certain operations.

### Young Generation

A Heap area that primarily contains recently created objects in generational Garbage Collectors.

### Old Generation

A Heap area that primarily contains objects that have survived previous Garbage Collection cycles.

### Young Collection

A Garbage Collection operation that primarily processes the Young Generation.

### Mark

A Garbage Collection phase that identifies objects reachable from GC Roots.

### Sweep

A Garbage Collection phase that reclaims memory occupied by unreachable objects.

### Compact

A process that moves objects in memory to reduce fragmentation and organize free memory.

### Mark-and-Sweep

A Garbage Collection approach that marks reachable objects and then reclaims memory occupied by unreachable objects.

### Generational Garbage Collection

A Garbage Collection approach that divides the Heap into areas based on the approximate age of objects.

### Survivor Space

A memory area used by some generational Garbage Collectors to store objects that survive certain collections.

### Object Lifecycle

The sequence of an object's creation, use, loss of reachability, eligibility for Garbage Collection, and eventual memory reclamation.

### Finalization

A historical Java mechanism associated with object cleanup before reclamation that should not be relied upon for resource management.

### Try-with-Resources

A Java mechanism that automatically closes resources implementing `AutoCloseable` or `Closeable`.

### External Resource

A resource outside normal Java object memory, such as a file, database connection, socket, or network connection, that must be properly managed.

### OutOfMemoryError

An error that occurs when the JVM cannot provide enough memory for an operation.

### StackOverflowError

An error that occurs when a thread exhausts its available Stack memory, commonly because of excessive or infinite recursion.
