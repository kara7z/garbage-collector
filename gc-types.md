# Types of Garbage Collectors in Java

Java provides several Garbage Collectors (GCs), each designed for different performance requirements.

## 1. Serial GC

> **Serial GC** is a simple garbage collector that performs garbage collection using **one thread**.

It is suitable for small applications where simplicity and low memory usage are more important than maximum performance.

**Main goal:** Simplicity

---

## 2. Parallel GC

> **Parallel GC** uses **multiple threads** to perform garbage collection, reducing GC time compared with Serial GC.

It is mainly designed to achieve **high application throughput**.

**Main goal:** High throughput

---

## 3. G1 GC — Garbage-First

> **G1 GC (Garbage-First Garbage Collector)** divides the heap into many **regions** and prioritizes regions containing the most garbage.

It aims to provide a balance between **good throughput and predictable pause times**.

**Main goal:** Balance between throughput and pause times

---

## 4. ZGC

> **ZGC (Z Garbage Collector)** is a low-latency garbage collector designed to keep **GC pauses very short**, even with very large heaps.

It is useful for applications where **responsiveness and low latency** are important.

**Main goal:** Very low latency

---

## 5. Shenandoah GC

> **Shenandoah** is a low-pause garbage collector that performs much of its work **concurrently with the application**.

Its main objective is to minimize the time during which the application is paused for garbage collection.

**Main goal:** Very short GC pauses

---

## 6. Epsilon GC

> **Epsilon GC** is a garbage collector that **does not reclaim memory**.

It simply allocates memory until the heap is exhausted. It can be useful for **testing, benchmarking, and applications where garbage collection is unnecessary**.

**Main goal:** No garbage collection

---

## Quick Comparison

| Garbage Collector | Main Goal                    |
| ----------------- | ---------------------------- |
| **Serial GC**     | Simplicity                   |
| **Parallel GC**   | High throughput              |
| **G1 GC**         | Balance + predictable pauses |
| **ZGC**           | Very low latency             |
| **Shenandoah GC** | Very short pauses            |
| **Epsilon GC**    | No garbage collection        |

## Easy Way to Remember

```text
Serial     → Simple
Parallel   → Throughput
G1         → Balance
ZGC        → Low latency
Shenandoah → Low pauses
Epsilon    → No GC
```
