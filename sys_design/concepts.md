# Systems Design

## Production Architecture

### CI/CD

## Pillars of Design

Good design is focoused on scalability, maintainability, and Efficiancy. It also means planning for failure and maintaining reliability. 

### Moving Data

### Storing Data

Understanding access patterns, indexing, and backup solutions.

### Transforming Data

## CAP/Brewer's Theorum

This theorum says you must choose tow of the three pillars of the theorum and must optimize for these to maintain a systems integrity. The three pillars are Consistance, Availability, and Partitioned Tolarance.

### Consistancey

### Availability

This is the time a system remains avaialable. The golden goal here is 5 9's or 99.999% uptime relating to about 8 minutes of down tiem per year. Thos also means implimenting redundant asystems to allow our system to function when there are issues. This means we have backups that can take on loads when necessary.

We also need to keep track of throughput, how much data our system can handle in a period of time, and latency which is how long a single operation takes. Optimizing for one may reduce the other. It'e iomportant to understand the requirments for your system.

### Partitioned Tolerance
