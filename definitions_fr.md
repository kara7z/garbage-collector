# Gestion de la mémoire en Java — Définitions

### Gestion de la mémoire

Processus d’allocation, d’utilisation et de libération de la mémoire pendant l’exécution d’un programme.

### JVM

La JVM (Java Virtual Machine) est l’environnement qui exécute le bytecode Java et gère notamment l’exécution et la mémoire du programme.

### RAM

La RAM (Random Access Memory) est la mémoire temporaire de l’ordinateur utilisée par les programmes en cours d’exécution.

### Stack (Pile)

Zone mémoire utilisée principalement pour gérer l’exécution des méthodes, notamment les frames, les variables locales, les paramètres et les références.

### Stack Frame

Structure mémoire créée lors de l’appel d’une méthode et contenant les informations nécessaires à son exécution.

### Thread

Unité indépendante d’exécution d’un programme. Chaque thread possède sa propre Stack.

### Variable locale

Variable déclarée à l’intérieur d’une méthode, d’un constructeur ou d’un bloc, dont la portée est limitée à cette zone.

### Heap (Tas)

Zone mémoire utilisée principalement pour stocker les objets et les tableaux créés pendant l’exécution du programme.

### Objet

Instance d’une classe créée pendant l’exécution du programme et généralement stockée dans le Heap.

### Référence

Valeur permettant à un programme d’accéder à un objet.

### Garbage Collector

Mécanisme de la JVM qui identifie automatiquement les objets inaccessibles et récupère la mémoire qu’ils occupent.

### Garbage Collection

Processus d’identification des objets inaccessibles et de récupération de la mémoire qu’ils occupent.

### Garbage

Objet qui n’est plus accessible depuis aucune GC Root et qui est donc éligible à la Garbage Collection.

### GC Root

Point de départ utilisé par le Garbage Collector pour déterminer quels objets sont encore accessibles.

### Accessibilité (Reachability)

Possibilité d’atteindre un objet en suivant une chaîne de références à partir d’une GC Root.

### Fuite mémoire (Memory Leak)

Situation dans laquelle un programme conserve des références inutiles vers des objets, empêchant le Garbage Collector de récupérer leur mémoire.

### null

Valeur spéciale indiquant qu’une référence ne pointe vers aucun objet.

### Metaspace

Zone mémoire de la JVM utilisée pour stocker les métadonnées des classes chargées.

### Allocation mémoire

Processus consistant à réserver de la mémoire pour les données nécessaires au programme.

### Récupération de mémoire

Processus consistant à rendre disponible la mémoire qui n’est plus nécessaire au programme.

### Stop-the-World

Période pendant laquelle les threads de l’application sont temporairement interrompus afin que la JVM puisse effectuer certaines opérations.

### Young Generation

Zone du Heap contenant principalement les objets récemment créés dans les Garbage Collectors utilisant une organisation générationnelle.

### Old Generation

Zone du Heap contenant principalement les objets ayant survécu à plusieurs cycles de Garbage Collection.

### Young Collection

Opération de Garbage Collection qui traite principalement la Young Generation.

### Mark (Marquage)

Phase de Garbage Collection durant laquelle les objets accessibles depuis les GC Roots sont identifiés.

### Sweep (Balayage)

Phase de Garbage Collection durant laquelle la mémoire occupée par les objets inaccessibles peut être récupérée.

### Compact (Compactage)

Processus consistant à déplacer les objets en mémoire afin de réduire la fragmentation et d’organiser l’espace libre.

### Mark-and-Sweep

Technique de Garbage Collection qui consiste à identifier les objets accessibles, puis à récupérer la mémoire des objets inaccessibles.

### Garbage Collection générationnelle

Approche de Garbage Collection qui divise le Heap en différentes zones selon l’âge approximatif des objets.

### Survivor Space

Zone mémoire utilisée par certains Garbage Collectors générationnels pour stocker les objets qui survivent à certaines collections.

### Cycle de vie d’un objet

Ensemble des étapes allant de la création d’un objet à son utilisation, sa perte d’accessibilité, son éligibilité à la Garbage Collection et finalement la récupération de sa mémoire.

### Finalization

Ancien mécanisme de Java associé au nettoyage des objets avant leur récupération, qui ne doit pas être utilisé comme mécanisme fiable de gestion des ressources.

### Try-with-resources

Mécanisme Java permettant de fermer automatiquement les ressources qui implémentent `AutoCloseable` ou `Closeable`.

### Ressource externe

Ressource extérieure à la gestion normale des objets Java, comme un fichier, une connexion à une base de données, un socket ou une connexion réseau, qui doit être correctement gérée.

### OutOfMemoryError

Erreur qui se produit lorsque la JVM ne dispose pas de suffisamment de mémoire pour effectuer une opération.

### StackOverflowError

Erreur qui se produit lorsqu’un thread épuise l’espace disponible dans sa Stack, souvent à cause d’une récursion excessive ou infinie.
