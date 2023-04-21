# History Conflict Serializability
 Transaction Systems, SS 2023
 
 Assignment No. 1
 
 ### Background
 
 History is conflict serializable if it is possible to create conflict equivalent history with serial execution of each transaction. 

In order to test history for conflict serializability in a computational manner, a conflict graph can be constructed. It should contain every conflicting operation between each transaction. Two operations are considered a conflict, if they both work on the same data (resource) and one of them is a WRITE.

Having a conflict (directed) graph for a history, the goal is to detect whether it contains a cycle. Cycle detection is performed based on Deep First Search recursive graph traversal algorithm. Vertices represent transactions, edges conflict operations between them.

If the conflict graph is acyclic it means that there are no two transactions that are co-conflicting and history is conflict serializable, otherwise it is not.

### Script

Based on provided history, script writes to `stdout` if it is conflict serializable (`true` / `false`).

#### Rrerequisites

[python3](https://www.python.org/downloads/)


#### Input

Provide history containing transactions operation as command line arguments separated with spaces:

```
[r/w] [transaction number] [resource] -> w 1 x
```

#### Execution

```
python3 hcs.py r 1 a r 2 a r 3 b w 1 a r 2 c r 2 b w 2 b w 1 c
```
