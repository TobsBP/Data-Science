import numpy as np

# ============================================================================
# ARRAY CREATION
# ============================================================================

# Basic arrays
np.array([1, 2, 3])                    # From list
np.arange(0, 10, 2)                    # Range with step
np.linspace(0, 1, 5)                   # Linear space
np.zeros((3, 4))                       # Array of zeros
np.ones((2, 3))                        # Array of ones
np.eye(3)                              # Identity matrix
np.random.rand(3, 4)                   # Random 0-1
np.random.randn(3, 4)                  # Random normal
np.random.randint(0, 100, (3, 4))      # Random integers

# ============================================================================
# ARRAY ATTRIBUTES
# ============================================================================

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.shape                               # (2, 3) - dimensions
arr.ndim                                # 2 - number of dimensions
arr.size                                # 6 - total elements
arr.dtype                               # Data type
arr.itemsize                           # Bytes per element

# ============================================================================
# INDEXING & SLICING
# ============================================================================

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Basic indexing
arr[0]                                 # First element
arr[-1]                                # Last element
arr[2:7]                               # Elements 2 to 6
arr[::2]                               # Every 2nd element
arr[::-1]                              # Reverse array

# 2D indexing
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

matrix[0, 1]                           # Row 0, column 1
matrix[0, :]                           # First row
matrix[:, 1]                           # Second column
matrix[0:2, 1:3]                      # Submatrix

# Boolean indexing
mask = arr > 50
arr[mask]                              # Elements > 50

# ============================================================================
# MATHEMATICAL OPERATIONS
# ============================================================================

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Arithmetic
a + b                                  # Addition
a - b                                  # Subtraction
a * b                                  # Element-wise multiplication
a / b                                  # Division
a ** 2                                 # Power
a @ b                                  # Matrix multiplication (if 2D)

# Broadcasting
a + 10                                 # Add scalar to all elements
a * 2                                  # Multiply all elements by 2

# Mathematical functions
np.sqrt(a)                             # Square root
np.exp(a)                              # Exponential
np.log(a)                              # Natural logarithm
np.sin(a)                              # Sine
np.cos(a)                              # Cosine
np.abs(a)                              # Absolute value

# ============================================================================
# STATISTICAL FUNCTIONS
# ============================================================================

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

np.mean(data)                          # Mean
np.median(data)                        # Median
np.std(data)                           # Standard deviation
np.var(data)                           # Variance
np.min(data)                           # Minimum
np.max(data)                           # Maximum
np.sum(data)                           # Sum
np.prod(data)                          # Product
np.percentile(data, 75)                # 75th percentile

# ============================================================================
# ARRAY MANIPULATION
# ============================================================================

arr = np.arange(12)

# Reshaping
arr.reshape(3, 4)                      # Reshape to 3x4
arr.reshape(2, 6)                      # Reshape to 2x6
arr.flatten()                          # Flatten to 1D
arr.ravel()                            # Flatten (view)

# Concatenation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate([a, b])                # Join arrays
np.vstack([a, b])                     # Stack vertically
np.hstack([a, b])                     # Stack horizontally

# Splitting
np.split(arr, 3)                       # Split into 3 parts
np.split(arr, [3, 7])                 # Split at indices

# ============================================================================
# LINEAR ALGEBRA
# ============================================================================

A = np.array([[2, 1], [1, 3]])
b = np.array([5, 6])

np.linalg.solve(A, b)                 # Solve Ax = b
np.linalg.inv(A)                      # Matrix inverse
np.linalg.det(A)                      # Determinant
np.linalg.eig(A)                      # Eigenvalues/vectors
np.linalg.svd(A)                      # SVD decomposition

# ============================================================================
# RANDOM NUMBER GENERATION
# ============================================================================

np.random.seed(42)                     # Set random seed
np.random.random(5)                    # Random floats 0-1
np.random.randn(5)                     # Random normal (0,1)
np.random.randint(1, 100, 5)          # Random integers
np.random.uniform(0, 10, 5)           # Random uniform
np.random.choice([1, 2, 3, 4, 5], 3)  # Random choice

# ============================================================================
# USEFUL TRICKS
# ============================================================================

# Find indices where condition is true
np.where(arr > 50)                     # Indices where arr > 50

# Replace values
arr[arr > 50] = 0                     # Replace > 50 with 0

# Unique values
np.unique(arr)                         # Get unique values

# Sort
np.sort(arr)                           # Sort array
np.argsort(arr)                        # Sort indices

# Save and load
np.save('array.npy', arr)              # Save array
loaded_arr = np.load('array.npy')      # Load array

# ============================================================================
# COMMON PATTERNS
# ============================================================================

# Create coordinate grids
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Vectorized operations (avoid loops!)
# Instead of: [x**2 for x in arr]
# Use: arr**2

# Broadcasting rules:
# 1. Arrays must have same number of dimensions, OR
# 2. One array must have dimension 1 in the mismatched axis

# Example: (3,4) + (4,) works because (4,) broadcasts to (1,4)
# Example: (3,4) + (3,1) works because (3,1) broadcasts to (3,4)