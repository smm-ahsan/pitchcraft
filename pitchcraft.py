#!/usr/bin/env python3
"""PitchCraft - write a spoken elevator pitch script (30 or 60 seconds).

Standard library only. Give it a name, a business, an audience, a problem
and a result, and it prints a short pitch written to be read out loud,
with a word count and an estimated speaking time.
"""

import argparse
import sys

WORDS_PER_MINUTE = 150

CLOSING_30 = "If that sounds useful, let us talk this week."
CLOSING_60 = (
    "I would love to show you a free example made for your business. "
    "Shall we talk this week?"
)
EXTRA_60 = "We start small, prove it works, and grow from there."


def capitalise_first(text):
    text = text.strip()
    if not text:
        return text
    return text[0].upper() + text[1:]


def build_script(name, business, audience, problem, result, seconds):
    lines = []
    if seconds == 60:
        lines.append(
            f"Have you ever struggled with {problem}? "
            f"I am {name}, and I help {audience} fix exactly that."
        )
    else:
        lines.append(f"Hi, I am {name}. I help {audience} with {business}.")
    lines.append(
        f"Most {audience} struggle with {problem}, "
        "and it costs them time and customers."
    )
    solution = (
        f"{capitalise_first(business)} turns that around with a simple, "
        "done-for-you approach."
    )
    if seconds == 60:
        solution += f" {EXTRA_60}"
    lines.append(solution)
    lines.append(f"The result: {result}.")
    lines.append(CLOSING_60 if seconds == 60 else CLOSING_30)
    return lines


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write a spoken elevator pitch script (30 or 60 seconds)."
    )
    parser.add_argument("--name", required=True,
                        help="person or brand name, e.g. 'Ahsan'")
    parser.add_argument("--business", required=True,
                        help="what it is, e.g. 'a social media service for Malta cafes'")
    parser.add_argument("--audience", required=True,
                        help="who it serves, e.g. 'cafe owners in Malta'")
    parser.add_argument("--problem", required=True,
                        help="the pain the audience struggles with")
    parser.add_argument("--result", required=True,
                        help="the promised outcome")
    parser.add_argument("--seconds", type=int, choices=[30, 60], default=30,
                        help="pitch length in seconds (default: 30)")
    args = parser.parse_args(argv)

    lines = build_script(
        args.name.strip(),
        args.business.strip(),
        args.audience.strip(),
        args.problem.strip(),
        args.result.strip(),
        args.seconds,
    )
    script = "\n".join(lines)
    words = len(script.split())
    spoken_seconds = round(words / WORDS_PER_MINUTE * 60)
    print(script)
    print(f"({words} words, about {spoken_seconds} seconds at a natural speaking pace)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
