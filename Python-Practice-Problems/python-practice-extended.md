# Python Practice Problems (Intermediate Foundations)

---

## 1. Nested Conditionals

Write a program that checks if `age` is greater than 18, and, if so, checks if the user is also a student. Print different messages depending on both conditions.

---

## 2. Conditional Type Check

Write a function `describe_type(value)` that returns `"Integer"`, `"String"`, `"Boolean"`, etc., based on the type of `value`.

---

## 3. Math with Mixed Types

Add an `int`, a `float`, and a `bool` together. Print the result and its type.

---

## 4. Multiple Conditions

Write a conditional that checks if `x` is between 10 and 20 (inclusive) and is an even number.

---

## 5. Boolean Logic

Create booleans `logged_in` and `is_admin`, write a conditional that prints:

- `"Welcome, admin"` if both are true
- `"Welcome, user"` if only logged in
- `"Access denied"` otherwise

---

## 6. Using `None` in a Function

Write a function `get_username(user)` that returns `"Guest"` if `user` is `None`, otherwise returns the username.

---

## 7. Invalid Operation

What happens if you try to add a string and a boolean? Can you create a similar situation by adding any other pairs of types?

---

## 8. Function with Multiple Parameters

Write a function `greet(name, is_morning)` that returns:

- `"Good morning, <name>!"` if `is_morning` is True
- `"Hello, <name>!"` otherwise

---

## 9. Default Values with `or`

Create a variable `display_name` that defaults to `"Guest"` if `username` is falsy. Set `username = ""` to test it.

---

## 10. Boolean Conditions as Output

Write a function `is_divisible(x, y)` that returns `True` if `x` is divisible by `y`, else `False`.

---

## 11. Type Mismatch

What happens when you compare an `int` and a `str` with `==`? Try it and explain the result.

---

## 12. Lambda with Condition

Write a lambda function that returns `"Even"` if the input number is even, `"Odd"` otherwise.

---

## 13. Floating Point Rounding

Print the result of `0.1 + 0.2`. Then write a function that checks if the result is approximately `0.3`.

---

## 14. Use a Function Inside Another

Write a function `shout(message)` that returns the result of another function `make_loud(message)` which adds `"!!!"` to the end.

---

## 15. Complex Boolean Expression

Given `x = 10`, `y = 5`, `z = 0`, write a conditional that prints `"Only x is positive"` if only `x` is greater than 0.

---

## 16. Function That Returns `None`

Write a function that prints something but returns `None`. Verify with `print(type(your_function()))`.

---

## 17. Use of Bytes

Create a bytes object with `b'hello'`, convert it to a string, and print it.

---

## 18. String Comparison

Ask the user to enter a password. If it matches `"OpenSesame"` (case-sensitive), print `"Access Granted"`; otherwise, `"Access Denied"`.

---

## 19. Use Boolean in Ternary

Set `has_permission = False`. Use a ternary expression to set `status = "Allowed"` or `"Denied"`.

---

## 20. Function Returns Function

Write a function `make_adder(n)` that returns a lambda function. The returned function should add `n` to its input.

Example:

```
python
add5 = make_adder(5)
print(add5(3))  # Output: 8
```

## 21. Match function outputs string

Write a function grade(score) that uses match with guards (if) to print the correct grade for the score given.


## 22. Match calculator

Write a function calculate(operation, num_one, num_two) that uses match to return the result of a basic operation.