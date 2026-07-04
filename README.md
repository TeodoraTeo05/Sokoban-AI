# Sokoban AI Solver

## Overview
This project implements an artificial intelligence agent designed to automatically solve Sokoban puzzles. [cite_start]It utilizes advanced search algorithms and distance-based heuristics to navigate complex maps efficiently while avoiding deadlocks and redundant explorations[cite: 3, 26].

## Search Algorithms
* [cite_start]**Beam Search:** Optimized using a heap data structure to retain only the best `K` states, significantly reducing sorting costs during state-space exploration[cite: 5]. 
* [cite_start]**LRTA* (Learning Real-Time A*):** Implemented with a maximum iteration limit to prevent infinite loops, alongside a penalty mechanism that increases the cost of "pull" moves[cite: 6].

## Heuristics Evaluated
To guide the algorithms toward optimal solutions, several heuristics were developed and benchmarked:
* [cite_start]**Misplaced Boxes:** Counts boxes not on target positions; proved slow and inefficient, generating massive search trees[cite: 9, 10, 12].
* [cite_start]**Manhattan Distance:** Calculates the sum of distances from boxes to the nearest targets, improving progress on simple maps but failing to account for wall blockages[cite: 16, 17, 18].
* [cite_start]**Euclidean Distance:** Uses straight-line measurements; improved behavior on open maps but struggled in confined, walled spaces[cite: 23, 24].
* [cite_start]**EMM (Each-Matched-Minimum) Manhattan:** Associates each box with the closest available target to prevent multiple boxes from tracking the same destination, effectively eliminating random, counterproductive moves[cite: 28, 29, 30].
* [cite_start]**EMM Euclidean:** Combines the strict target-allocation of EMM with accurate Euclidean distance measurements[cite: 32, 33].

## Performance Analysis & Conclusions
Extensive testing across various map difficulties yielded the following analytical insights:
* [cite_start]**Best Overall Heuristic:** The **EMM Euclidean heuristic** outperformed all others, achieving a 100% success rate across both algorithms.
* [cite_start]**Beam Search vs. LRTA*:** Beam Search proved faster and more efficient in terms of explored states on most standard maps[cite: 246]. [cite_start]However, LRTA* excelled on "Super Hard" maps[cite: 247, 250]. [cite_start]Because Beam Search rigidly limits itself to the best `K` states, it prunes seemingly suboptimal paths that are sometimes necessary for complex solutions[cite: 247, 248]. [cite_start]LRTA*, while slower, explores more dynamically and corrects its path in real-time, making it superior for highly complex layouts[cite: 245, 249].
