def greet_user(name, gender):
    gender = gender.lower()

    # titles
    titles = {
        "male": "Mr.",
        "female": "Mrs.",
        "other": "Mx."
    }

    # default also gender-neutral
    title = titles.get(gender, "Mx.")

    return f"Hello, {title} {name}! Welcome."