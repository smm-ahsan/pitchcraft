# Examples

Real output from PitchCraft, captured from actual runs.

## A 30-second pitch

Command:

```bash
python3 pitchcraft.py --name "Ahsan" --business "a social media service for Malta cafes" --audience "cafe owners in Malta" --problem "posting inconsistently and getting no customers from Instagram" --result "steady enquiries every week without the owner filming anything" --seconds 30
```

Output:

```
Hi, I am Ahsan. I help cafe owners in Malta with a social media service for Malta cafes.
Most cafe owners in Malta struggle with posting inconsistently and getting no customers from Instagram, and it costs them time and customers.
A social media service for Malta cafes turns that around with a simple, done-for-you approach.
The result: steady enquiries every week without the owner filming anything.
If that sounds useful, let us talk this week.
(75 words, about 30 seconds at a natural speaking pace)
```

## A 60-second pitch

Same inputs with `--seconds 60`. The hook becomes a question about the problem, the solution adds a low-risk first step, and the closing offers a free example.

Command:

```bash
python3 pitchcraft.py --name "Ahsan" --business "a social media service for Malta cafes" --audience "cafe owners in Malta" --problem "posting inconsistently and getting no customers from Instagram" --result "steady enquiries every week without the owner filming anything" --seconds 60
```

Output:

```
Have you ever struggled with posting inconsistently and getting no customers from Instagram? I am Ahsan, and I help cafe owners in Malta fix exactly that.
Most cafe owners in Malta struggle with posting inconsistently and getting no customers from Instagram, and it costs them time and customers.
A social media service for Malta cafes turns that around with a simple, done-for-you approach. We start small, prove it works, and grow from there.
The result: steady enquiries every week without the owner filming anything.
I would love to show you a free example made for your business. Shall we talk this week?
(102 words, about 41 seconds at a natural speaking pace)
```
