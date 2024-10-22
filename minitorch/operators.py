"""Collection of the core mathematical operators used throughout the code base."""

import math
from typing import Callable, Iterable


def mul(x: float, y: float) -> float:
    """Multiply `x` by `y`"""
    return x * y


def id(x: float) -> float:
    """Return input `x` unchanged"""
    return x


def add(x: float, y: float) -> float:
    """Add `x` and `y`"""
    return x + y


def neg(x: float) -> float:
    """Negate `x`"""
    return -x


def lt(x: float, y: float) -> bool:
    """Return True if `x` is less than `y`, otherwise returns False"""
    return x < y


def eq(x: float, y: float) -> bool:
    """Return True if `x` is equal to  `y`, otherwise returns False"""
    return x == y


def max(x: float, y: float) -> float:
    """Returns the maximum value between `x` and `y`"""
    return x if x > y else y


def is_close(x: float, y: float) -> bool:
    """Check if floats `x` and `y` are within 1e-2"""
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    """Calculate the sigmoid activation function."""
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))


def relu(x: float) -> float:
    """Applies the ReLU (Rectified Linear Unit) activation function.

    Args:
    ----
        x (Number): The input value.

    Returns:
    -------
        Number: The result of the ReLU function, which is max(0, x).

    """
    return max(0.0, x)


def log(x: float) -> float:
    """Calculate the natural logarithm of `x`. Raises ValueError if `x` <= 0."""
    if x <= 0:
        raise ValueError("log function is only defined for positive numbers.")
    return math.log(x)


def exp(x: float) -> float:
    """Calculate the exponential function of `x` (returns e^x)."""
    return math.exp(x)


def inv(x: float) -> float:
    """Calculate the reciprocal x (1/x). Raises ValueError if `x` is 0."""
    if x == 0:
        raise ValueError("Cannot compute the reciprocal of zero.")
    return 1 / x


def log_back(x: float, d: float) -> float:
    """Compute the derivative of the natural logarithm function, scaled by a second argument.

    Args:
    ----
        x (Number): The input value, must be positive.
        d (Number): The scaling factor for the derivative.

    Returns:
    -------
        float: The scaled derivative of the log function, calculated as d / x.

    Raises:
    ------
        ValueError: If x is less than or equal to 0, as the derivative is undefined for non-positive numbers.

    Example:
    -------
        >>> log_back(2, 3)
        1.5

    """
    if x <= 0:
        raise ValueError("log_back function is only defined for positive numbers.")
    return d / x


def inv_back(x: float, d: float) -> float:
    """Compute the derivative of the reciprocal function, scaled by a second argument.

    Args:
    ----
        x (float): The input value, must not be 0.
        d (float): The scaling factor for the derivative.

    Returns:
    -------
        float: The scaled derivative of the reciprocal function, calculated as -d / x^2.

    Raises:
    ------
        ValueError: If x is equal to 0, as the derivative is undefined.

    Example:
    -------
        >>> inv_back(2, 3)
        -0.75

    """
    if x == 0:
        raise ValueError("inv_back function is not defined for x = 0.")
    return -d / (x**2)


def relu_back(x: float, d: float) -> float:
    """Compute the derivative of the ReLU function, scaled by a second argument.

    Args:
    ----
        x (float): The input value.
        d (float): The scaling factor for the derivative.

    Returns:
    -------
        Number: The scaled derivative of the ReLU function. Returns d if x > 0, otherwise 0.

    Example:
    -------
        >>> relu_back(3, 2)
        2
        >>> relu_back(-1, 2)
        0

    """
    return d if x > 0 else 0


def map(fn: Callable[[float], float], lst: Iterable[float]) -> Iterable[float]:
    """Applies a function to each element in an iterable.

    Args:
    ----
        fn (Callable[[float], float]): A function that takes a float and returns a float.
        lst (Iterable[float]): An iterable of floats to which the function will be applied.

    Returns:
    -------
        Iterable[float]: A new iterable with the function applied to each element.

    Example:
    -------
        >>> list(map(lambda x: x * 2, [1.0, 2.0, 3.0]))
        [2.0, 4.0, 6.0]

    """
    return (fn(x) for x in lst)


def zipWith(
    fn: Callable[[float, float], float], lst1: Iterable[float], lst2: Iterable[float]
) -> Iterable[float]:
    """Applies a function to pairs of elements from two iterables.

    Args:
    ----
        fn (Callable[[float, float], float]): A function that takes two floats and returns a float.
        lst1 (Iterable[float]): The first iterable of floats.
        lst2 (Iterable[float]): The second iterable of floats.

    Returns:
    -------
        Iterable[float]: A new iterable with the function applied to corresponding elements of lst1 and lst2.

    Example:
    -------
        >>> list(zipWith(lambda x, y: x + y, [1.0, 2.0], [3.0, 4.0]))
        [4.0, 6.0]

    """
    return (fn(x, y) for x, y in zip(lst1, lst2))


def reduce(fn: Callable[[float, float], float], lst: Iterable[float]) -> float:
    """Reduces an iterable to a single value using a given function.

    Args:
    ----
        fn: A function that takes two floats and returns a float.
            This function will be applied cumulatively to the elements of the iterable.
        lst: An iterable of floats to be reduced.

    Returns:
    -------
        A float that is the result of reducing the iterable using the function `fn`.

    Raises:
    ------
        TypeError: If the iterable `lst` is empty.

    Example:
    -------
        >>> reduce(lambda x, y: x + y, [1.0, 2.0, 3.0, 4.0])
        10.0

    """
    it = iter(lst)

    # Use the first element as the initial value
    try:
        acc = next(it)

    except StopIteration:
        raise TypeError("reduce() of empty sequence")

    # Apply the function to theremaining element
    for x in it:
        acc = fn(acc, x)
    return acc


def negList(lst: Iterable[float]) -> Iterable[float]:
    """Negate all elements in a list."""
    return map(lambda x: -x, lst)


def addLists(lst1: Iterable[float], lst2: Iterable[float]) -> Iterable[float]:
    """Add corresponding elements from two lists."""
    return zipWith(lambda x, y: x + y, lst1, lst2)


def sum(lst: Iterable[float]) -> float:
    """Sum all elements in a list."""
    if not lst:
        return 0.0  # Return 0 for an empty list
    return reduce(lambda x, y: x + y, lst)


def prod(lst: Iterable[float]) -> float:
    """Calculate the product of all elements in a list."""
    if not lst:
        return 1.0  # Return 1 for an empty list
    return reduce(lambda x, y: x * y, lst)
