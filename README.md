# Lab 2: Data Types and Expressions
The purpose of these series of labs is to get you familiar with using different types of data types and expressions. 

Chapter 2 covers a lot, but here is a summary of what was covered.

|Escape Sequences|Meaning|
|-|-|
|`\b`|Backspace|
|`\n`|Newline|
|`\t`|Horizontal Tab|
|`\\`|The \ Character|
|`\'`|Single Quotation Mark|
|`\"`|Double Quotation Mark|

|Operator|Meaning|Evaluation|Value
|-|-|-|-|
|`-`|Negation|`-(3+2)`| `-5`
|`**`|Exponentiation|`3**2`| `9`|
|`*`|Multiplication|`3*4`| `12`|
|`/`|Division| `45/4` | `11.25`|
|`//`|Quotient| `45/4` | `11`|
|`%`|Modulo/Remainder| `45%4` | `1`

|Convertion Function|Example Use|Value Returned|
|-|-|-|
|`str()`|`str(99.2)`|`'99.2'`|
|`float()`|`float(22)`|`22.0`|
|`int()`| `int("33")`| `33`|
| |`int(6.7)`|`6`|

Useful module: `math`
Other help functions: `help()`, `dir()`
## Grading Criteria
|Lab Number| Description| Total|
|-|-|-|
|Lab 2a| Physics in Action! | 25pts | 
|Lab 2b| Engineering Statics | 25pts |
|Lab 2c| Estimating the Radius of the Earth | 25pts|
|Lab 2d| Calcuating employee pay | 15pts|
|Lab 2e| Taxes on a Restaurant | 10pts|

I will grade mostly for functionality but also do some test cases on my end.
## Test cases

Labs 2a-c will have no test cases as test values are already provided. 
### Lab 2d

Case 1:
```
Enter your hourly pay: 22
Enter the amount of hours worked: 90

Total Hours Worked: 80
Overtime Hours: 10
Regular Pay: $1760
Overtime Pay: $330
Gross Pay: $2090
```

Case 2:
```
Enter your hourly pay: 18
Enter the amount of hours worked: 75

Total Hours Worked: 75
Overtime Hours: 0
Regular Pay: $1350
Overtime Pay: $0
Gross Pay: $1350
```

## Lab 2e
```
Enter your restaurant bill $: 34.90
Gratuity: $3.49
Total bill: $38.39
```