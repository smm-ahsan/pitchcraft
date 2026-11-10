# PitchCraft

A tiny command-line tool that writes a spoken elevator pitch script — 30 or 60 seconds — from five simple inputs: who you are, what the business is, who it serves, the problem it solves, and the result it promises.

## The pitch structure

Every script follows the same five-part structure, one part per line:

1. **Hook** — who you are and who you help. The 60-second version opens with a question about the problem instead.
2. **Problem** — the pain the audience struggles with, and what it costs them.
3. **Solution** — how the business turns it around, in one simple line. The 60-second version adds a low-risk first step.
4. **Result** — the promised outcome, stated plainly.
5. **Closing** — a small, specific call to talk this week.

After the script, the tool prints the word count and the estimated speaking time at a natural pace of about 150 words per minute. The 30-second script stays at or under 80 words; the 60-second script at or under 160 words.

## Requirements

- Python 3
- Standard library only — nothing to install

## Usage

A 30-second pitch:

```bash
python3 pitchcraft.py --name "Ahsan" --business "a social media service for Malta cafes" --audience "cafe owners in Malta" --problem "posting inconsistently and getting no customers from Instagram" --result "steady enquiries every week without the owner filming anything" --seconds 30
```

A 60-second pitch, with the question hook and the free-example closing:

```bash
python3 pitchcraft.py --name "Ahsan" --business "a social media service for Malta cafes" --audience "cafe owners in Malta" --problem "posting inconsistently and getting no customers from Instagram" --result "steady enquiries every week without the owner filming anything" --seconds 60
```

See [examples.md](examples.md) for real captured output from both commands.

## Options

| Option | Required | Description |
| --- | --- | --- |
| `--name` | Yes | Person or brand name |
| `--business` | Yes | What it is, e.g. "a social media service for Malta cafes" |
| `--audience` | Yes | Who it serves |
| `--problem` | Yes | The pain the audience struggles with |
| `--result` | Yes | The promised outcome |
| `--seconds` | No | `30` (default) or `60` |

## License

MIT — see [LICENSE](LICENSE).
