def format_name(full_name: str) -> str:
    """Format a full name into "Last, First".

    Examples:
    - "Virat Kohli" -> "Kohli, Virat"
    - "Elon Musk" -> "Musk, Elon"

    Behavior/assumptions:
    - Leading/trailing whitespace is ignored.
    - If the input contains more than two name parts (e.g. "Mary Ann Smith"),
      the last token is treated as the last name and everything before it as the first name(s):
      "Mary Ann Smith" -> "Smith, Mary Ann".
    - If only a single name is provided, it is returned unchanged.
    - Non-string inputs raise TypeError.
    """

    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string")

    parts = full_name.strip().split()

    if not parts:
        return ""

    if len(parts) == 1:
        return parts[0]

    last = parts[-1]
    first = " ".join(parts[:-1])
    return f"{last}, {first}"


if __name__ == "__main__":
    examples = {
        "Virat Kohli": "Kohli, Virat",
        "Elon Musk": "Musk, Elon",
        "Mary Ann Smith": "Smith, Mary Ann",
        "Single": "Single",
        "  Leading  Trailing  ": "Trailing, Leading",
    }

    for inp, expected in examples.items():
        out = format_name(inp)
        print(f'Input: "{inp}" -> Output: "{out}" (expected: "{expected}")')
        assert out == expected, f"For input {inp!r} expected {expected!r} but got {out!r}"

    print("All tests passed")
