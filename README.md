# Sokoban AI Solver

## Overview
This project implements an artificial intelligence agent designed to automatically solve Sokoban puzzles. It utilizes advanced search algorithms and distance-based heuristics to navigate complex maps efficiently while avoiding deadlocks and redundant explorations.

## Search Algorithms
* **Beam Search:** Optimized using a heap data structure to retain only the best `K` states, significantly reducing sorting costs during state-space exploration. 
* **LRTA* (Learning Real-Time A*):** Implemented with a maximum iteration limit to prevent infinite loops, alongside a penalty mechanism that increases the cost of "pull" moves.

## Heuristics Evaluated
To guide the algorithms toward optimal solutions, several heuristics were developed and benchmarked:
* **Misplaced Boxes:** Counts boxes not on target positions; proved slow and inefficient, generating massive search trees.
* **Manhattan Distance:** Calculates the sum of distances from boxes to the nearest targets, improving progress on simple maps but failing to account for wall blockages.
* **Euclidean Distance:** Uses straight-line measurements; improved behavior on open maps but struggled in confined, walled spaces.
* **EMM (Each-Matched-Minimum) Manhattan:** Associates each box with the closest available target to prevent multiple boxes from tracking the same destination, effectively eliminating random, counterproductive moves.
* **EMM Euclidean:** Combines the strict target-allocation of EMM with accurate Euclidean distance measurements.

## Performance Analysis & Conclusions
Extensive testing across various map difficulties yielded the following analytical insights:
* **Best Overall Heuristic:** The **EMM Euclidean heuristic** outperformed all others, achieving a 100% success rate across both algorithms.
* **Beam Search vs. LRTA*:** Beam Search proved faster and more efficient in terms of explored states on most standard maps. However, LRTA* excelled on "Super Hard" maps. Because Beam Search rigidly limits itself to the best `K` states, it prunes seemingly suboptimal paths that are sometimes necessary for complex solutions. LRTA*, while slower, explores more dynamically and corrects its path in real-time, making it superior for highly complex layouts.
