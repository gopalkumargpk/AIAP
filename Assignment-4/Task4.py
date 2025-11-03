def count_vowels(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch.isalpha() and ch in vowels)


if __name__ == "__main__":
    examples = {
        "Hello World!": 3,
        "Virat Kohli": 4,   # i,a,o,i
        "MS Dhoni": 2,      # o,i
        "AEIOU aeiou": 10,
        "123!": 0,
    }

    for text, expected in examples.items():
        result = count_vowels(text)
        print(f"{text!r} -> {result} (expected {expected})")
        assert result == expected, f"For {text!r} expected {expected} but got {result}"

    print("All tests passed")
