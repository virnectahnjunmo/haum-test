def greet(name):
    """Simple greeting helper. Added 2026-04-25 for Opus 4.7 verification."""
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"


def greet_team(names: list[str]) -> str:
    """Greet multiple people."""
    greetings = [greet(n) for n in names]
    return " | ".join(greetings)
