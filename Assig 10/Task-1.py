from typing import Callable, Dict

# Mapping of category to a function returning the discount multiplier.
_DISCOUNT_RULES: Dict[str, Callable[[float], float]] = {
    "student": lambda price: 0.9 if price > 1000 else 0.95,
    "_default": lambda price: 0.85 if price > 2000 else 1.0,
}

def discount(price: float, category: str) -> float:
    """
    Calculate discounted price based on category and price.
    Unknown categories use the default rule.
    """
    rate_fn = _DISCOUNT_RULES.get(category, _DISCOUNT_RULES["_default"])
    return price * rate_fn(price)


# Optional: quick self-test (remove if not needed)
if __name__ == "__main__":
    cases = [
        (1200, "student"),
        (900, "student"),
        (2500, "regular"),
        (1800, "regular"),
    ]
    for p, c in cases:
        print(f"{c=}, {p=}, discounted={discount(p, c)}")