# Advent Of Code
This is the challenge: https://adventofcode.com/2020

And here's my take on it :)

## Today-I-Learned Summary:

### Day 1

-  concept of yield generator.
- 'with' keyword.
- hash tables.
- working with data, always pay attention to complexity!:
for a list of numbers of length *n*, my algorithm makes *n* sums for *n* times. 
This is the case with my approach, resulting in complexity of *O(n^{2})*. 

Sorting the list takes *nlogn*, so by using:

![Algorithm](https://user-images.githubusercontent.com/64603095/100857815-6f767780-348d-11eb-9b63-d9ff63be3043.png)

Overall complexity is now *nlogn + n - 1*

However, by using hash tabels:
