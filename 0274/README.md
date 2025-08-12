# 274. H-Index

## Problem Description

Given an array of integers `citations` where `citations[i]` represents the number of citations received for the researcher's i-th paper, calculate and return the researcher's **h-index**.

## What is H-Index?

The **h-index** is a metric used to measure both the productivity and citation impact of a researcher. It is defined as the maximum value `h` such that the researcher has published **at least `h` papers** that have each been cited **at least `h` times**.

## Examples

### Example 1
```
Input: citations = [3, 0, 6, 1, 5]
Output: 3
```

**Explanation:**
- The researcher has 5 papers with citation counts: [3, 0, 6, 1, 5]
- To find h-index = 3, we need at least 3 papers with ≥3 citations each
- Papers with ≥3 citations: [3, 6, 5] (3 papers) ✓
- Remaining papers: [0, 1] (≤3 citations each) ✓
- Therefore, h-index = 3

### Example 2
```
Input: citations = [1, 3, 1]
Output: 1
```

**Explanation:**
- The researcher has 3 papers with citation counts: [1, 3, 1]
- To find h-index = 1, we need at least 1 paper with ≥1 citation
- Papers with ≥1 citation: [1, 3, 1] (3 papers) ✓
- Therefore, h-index = 1

## Constraints

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## Key Insights

1. **Sorting helps**: Sort citations in descending order to easily find papers with sufficient citations
2. **Binary search approach**: Can use binary search to find the optimal h-index value
3. **Linear approach**: Iterate through sorted citations to find the first index where `citations[i] < i+1`

## Approach

The most efficient approach involves:
1. Sort the citations array in descending order
2. Find the largest index `i` where `citations[i] >= i + 1`
3. Return `i + 1` as the h-index

**Time Complexity:** O(n log n) due to sorting
**Space Complexity:** O(1) if sorting in-place, O(n) if creating a copy