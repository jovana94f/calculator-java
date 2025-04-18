# TEST-RESULTS.md

# Black Box Testing Results for Calculator Program

## Detected Issues

1. **Incorrect Order of Operations**
   - Description: The calculator does not respect the order of operations (PEMDAS/BODMAS).
   - Example: Input `10 + 5 * 4` should return `30`, but it returns `60`.

2. **Handling of Division by Zero**
   - Description: The calculator crashes when attempting to divide by zero.
   - Example: Input `10 / 0` should return an error message, but it throws an exception.

3. **Invalid Input Handling**
   - Description: The calculator does not handle invalid inputs gracefully.
   - Example: Input `10 + a` should return an error message, but it produces an unexpected result.

4. **Floating Point Precision**
   - Description: The calculator has issues with floating point arithmetic.
   - Example: Input `0.1 + 0.2` should return `0.3`, but it returns `0.30000000000000004`.

## Observations

- The user interface is not intuitive for entering complex expressions.
- There is no clear indication of errors or invalid inputs to the user.
- The performance of the calculator decreases with more complex expressions.

## Recommendations

- Implement error handling for invalid inputs and division by zero.
- Ensure that the order of operations is correctly implemented.
- Improve user feedback for errors and invalid inputs.
- Consider using a more robust method for handling floating point arithmetic.