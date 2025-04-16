# 🚀 Getting Started with NumPy

A beginner-friendly roadmap to help you get started with NumPy in Python.

---

## ✅ 1. Install NumPy (if not done already)
Use the following command in your terminal:
```bash
pip3 install numpy
```

---

## ✅ 2. Import NumPy in Python
Always import NumPy like this:
```python
import numpy as np
```
`np` is just an alias to save typing.

---

## ✅ 3. Create Your First NumPy Array
```python
import numpy as np

a = np.array([1, 2, 3])
print(a)
```

---

## ✅ 4. Basic Array Operations
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Dot product:", np.dot(a, b))
```

---

## ✅ 5. Useful NumPy Functions
```python
np.zeros((2, 3))      # 2x3 array of zeros
np.ones((3, 3))       # 3x3 array of ones
np.eye(3)             # Identity matrix
np.arange(0, 10, 2)   # [0 2 4 6 8]
np.linspace(0, 1, 5)  # 5 points between 0 and 1
```

---

## ✅ 6. Indexing & Slicing
```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a[0, 1])    # Element at 1st row, 2nd column → 2
print(a[:, 1])    # All rows, 2nd column → [2 5]
```

---

## ✅ 7. Shape and Reshape
```python
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.shape)             # (3, 2)
print(a.reshape(2, 3))     # [[1 2 3] [4 5 6]]
```

