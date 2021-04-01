# Storyline Notes

## Structure

### Introduction

Give a general outline, motivating the problem of immutability in an open Web based on open standards, linked data and distributed communication, storage and computation paradigms.

Outline the further structure of the document.

### Terminology and Definitions

Overview of the relevant terms:

- Correctness vs trustworthiness vs reliability vs accountability vs ... (and the relation towards data quality)
- Immutability (here especially: schematic/conceptual immutability vs secure/verifiable/provable immutability, could also be called trustworthy immutability) vs integrity vs authenticity vs non-repudiation

### State of the Art

- Outline common paradigms for immutability
- Central vs. Distributed
- No scalable distributed solution
- Tradeoff between security/confidence in immutability and scalability
- No perfect solution possible, but maybe giving up a little immutability could drastically improve scalability/performance/overheads

## Technical Contents

- On-demand signature paradigm (trust model + tradeoff)
- DTCs as a data structure/digital record/transaction agreement model
- ReShare Ontology for interpreting/defining DTCs for LD
- Implementation: DTC Generation handshake, verification procedure
  - 3-way vs shortened 2-way handshake
  - Integration/relation with underlying data transmission
  - The role of RIDs/PIDs/IRIs
