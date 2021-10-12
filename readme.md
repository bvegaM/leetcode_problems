# LeetCode Problems

<div align="center">

> **Developed by:** Bryam David Vega Moreno<br>
> **Title:** Computer Science Engineer <br>
> **University:** Universidad Politécnica Salesiana

[![Tweet](https://img.shields.io/twitter/url/https/shields.io.svg?style=social)](https://twitter.com/BryamDavidVega1)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

</div>



![leetcode](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/LeetCode_Logo_black_with_text.svg/1280px-LeetCode_Logo_black_with_text.svg.png)

<br>

<h3 align="center">🇪🇨Solution problems to LeetCode Platform by Bryam Vega 📊</h3>

<br>

<details>
    <summary>Table Of Contents</summary>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#problems">Problems</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</details>

<br>

# Introduction

<p align="justify">In this repository you will find solutions to various problems of the leetCode platform. The objective of this repository is to show solutions to problems related to data structure. At the same time I try to improve my developer skills, solving problems in the best way.<p>

# Problems

## Algorithms

### Easy problems

<br>

<details>
<summary> Roman to Integer</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(67, 160, 71)">Easy</strong> 
Link: <a href="https://leetcode.com/problems/roman-to-integer/">problem</a>
</p>
</div>
<br>
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, ```2``` is written as ```II``` in Roman numeral, just two one's added together. ```12``` is written as ```XII```, which is simply ```X + II```. The number ```27``` is written as ```XXVII```, which is ```XX + V + II```.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not ```IIII```. Instead, the number four is written as ```IV```. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as ```IX```. There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9. 
* X can be placed before L (50) and C (100) to make 40 and 90. 
* C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
```

**Example 2:**

```
Input: s = "IV"
Output: 4
```

**Example 3:**

```
Input: s = "IX"
Output: 9
```

**Example 4:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 5:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
</details>

<br>

### Medium problems

<br>

<details>
<summary>Add Two Numbers</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(239, 108, 0)">Medium</strong> 
Link: <a href="https://leetcode.com/problems/add-two-numbers/">problem</a>
</p>
</div>

<br>

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![addtwonumbers](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```
</details>

<details>
<summary> Longest Substring Without Repeating Characters</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(239, 108, 0)">Medium</strong> 
Link: <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">problem</a>
</p>
</div>

<br>

Given a string s, find the length of the longest substring without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:**

```
Input: s = ""
Output: 0
```
</details>

<details>
<summary>ZigZag Conversion</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(239, 108, 0)">Medium</strong> 
Link: <a href="https://leetcode.com/problems/zigzag-conversion/">problem</a>
</p>
</div>

<br>

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: ```"PAHNAPLSIIGYIR"```

Write the code that will take a string and make this conversion given a number of rows:

```java
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

**Example 3:**

```
Input: s = "A", numRows = 1
Output: "A"
```
</details>

<br>

### Hard problems

<br>

<details>
<summary>Median of Two Sorted Arrays</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(233, 30, 99)">Hard</strong> 
Link: <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/">problem</a>
</p>
</div>

<br>

Given two sorted arrays ```nums1``` and ```nums2``` of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be ```O(log (m+n))```.

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

**Example 4:**

```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

**Example 5:**

```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```
</details>


<br>

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

All issues are the authorship of the LeetCode platform.

# Contact

Bryam David Vega Moreno - [@BryamDavidVega1](https://twitter.com/BryamDavidVega1) - vegabryam40@gmail.com

Project Link: [https://github.com/bvegaM/leetcode_problems](https://github.com/bvegaM/leetcode_problems)


