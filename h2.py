import numpy as np

coefficients = [2, -8, 6, -4, 2]
poly = np.poly1d(coefficients)

print("Формула полінома:")
print(poly)

roots = poly.r
print("\nКорені полінома:", roots)

derivative = poly.deriv()
print("\nПохідна полінома:")
print(derivative)

second_derivative = poly.deriv(2)
print("\nДруга похідна полінома:")
print(second_derivative)

n = 50
result = poly(n)
print(f"\nЧас виконання при n=50: {result}")
