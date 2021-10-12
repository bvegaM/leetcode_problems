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

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

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

<details>
<summary> Two Sum</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(67, 160, 71)">Easy</strong> 
Link: <a href="https://leetcode.com/problems/two-sum/">problem</a>
</p>
</div>
<br>

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.


**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```
</details>


### Medium problems

<details>
<summary>Add Two Numbers</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(239, 108, 0)">Medium</strong> 
Link: <a href="https://leetcode.com/problems/partition-labels/">problem</a>
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

<details>
<summary>Partition Labels</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(239, 108, 0)">Medium</strong> 
Link: <a href="https://leetcode.com/problems/zigzag-conversion/">problem</a>
</p>
</div>

<br>

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.

**Example 1:**

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

**Example 2:**

```
Input: s = "eccbbbbdec"
Output: [10]
```
</details>

### Hard problems

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








## Database

### Easy problems

<details>
<summary> Combine Two Tables </summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(67, 160, 71)">Easy</strong> 
Link: <a href="https://leetcode.com/problems/combine-two-tables/">problem</a>
</p>
</div>
<br>

`SQL Schema >`

Table: `Person`

```sql
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
This table contains information about the ID of some persons and their first and last names.
```

Table: `Address`

```sql
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
Each row of this table containts information about the city and state of one person with ID = PersonId.
```

Write an SQL query to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `PersonId` is not present in the `Address` table, report null instead.

Return the result table in **any order**.

The query result format is in the following example.

**Example 1:**

```sql
Input: 
Person table:
+----------+----------+-----------+
| PersonId | LastName | FirstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| AddressId | PersonId | City          | State      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| FirstName | LastName | City          | State    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the PersonId = 1 so we return null in their city and state.
AddressId = 1 contains information about the address of PersonId = 2.
```
</details>



### Medium problems

<details>
<summary>Second Highest Salary</summary>

<br>

<div class='container' style="border-bottom: 1px solid rgb(238, 238, 238);">
<p>Dificult: <strong style="color: rgb(239, 108, 0)">Medium</strong> 
Link: <a href="https://leetcode.com/problems/second-highest-salary/">problem</a>
</p>
</div>

<br>

`SQL Schema >`

Table: `Employee`

```sql
+-------------+------+
| Column Name | Type |
+-------------+------+
| Id          | int  |
| Salary      | int  |
+-------------+------+
Id is the primary key column for this table.
Each row of this table contains information about the salary of an employee.
```

Write an SQL query to report the second highest salary from the `Employee` table. If there is no second highest salary, the query should report `null`.

The query result format is in the following example.

**Example 1:**
```sql
Input: 
Employee table:
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```


**Example 2:**

```sql
Input: 
Employee table:
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| Null                |
+---------------------+
```
</details>

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

All issues are the authorship of the LeetCode platform.

# Contact

Bryam David Vega Moreno - [@BryamDavidVega1](https://twitter.com/BryamDavidVega1) - vegabryam40@gmail.com

Project Link: [https://github.com/bvegaM/leetcode_problems](https://github.com/bvegaM/leetcode_problems)


