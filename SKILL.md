---
name: chord-progression-recommender
description: Automatically recommends mathematically and musically proven chord transitions and full progressions by mining 31,032 real-world song chord sequences from the Lakh MIDI dataset on Drive B. Activated whenever the user asks for chord ideas, what chord should follow next, or asks to find songs with a specific harmonic sequence.
---

# Chord Progression Recommender

Mines real harmonic transition frequencies across 31,032 analyzed songs in `B:\AI Directories_Databases\Datasets\midi_datasets\lmd_chords`.

Whenever the user asks questions in chat about songwriting, harmony, chord progressions, or what chord should follow next, activate this skill to provide data-backed harmonic recommendations and real song examples.

---

## When to Activate

Trigger this skill whenever the user asks things like:
* *"I have a verse starting on Dm - Gm, what chord should come next?"*
* *"Recommend a chord progression for a melancholic Neo-Soul or R&B track in F minor."*
* *"What chords go well after Cmaj7?"*
* *"Find songs in our database that use the progression Am - F - C - G."*
* *"What are some unexpected or spicy turnaround chords for a bridge?"*

---

## How to Execute Under the Hood (Silent Agent Workflow)

You do **NOT** ask the user to run scripts in PowerShell. Instead, run the query invisibly using terminal/bash commands and format the output directly into chat:

```bash
# To find top next chords after a specific chord:
python "<skill_dir>/scripts/recommend_chords.py" --after "Dm" --limit 5

# To find real songs that use a specific progression:
python "<skill_dir>/scripts/recommend_chords.py" --progression "Am,F,C,G" --limit 6
```

The script returns clean JSON containing:
* The most frequent following chords and their transition percentages.
* Real-world artist, song title, and release year examples for each transition.

---

## Chat Presentation Guidelines

When presenting recommendations back to the user in chat, always provide:

1. **Top 3–4 Categorized Next Moves:**
   * **The Strong Resolution** (e.g. $ii \rightarrow V$ or dominant resolution).
   * **The Modal / Emotional Color** (e.g. relative major/minor, $\flat VI$ borrowed chord).
   * **The Surprise Turnaround** (secondary dominant, tritone substitution, or passing diminished).
2. **Harmonic Explanation & Roman Numerals:** Explain *why* the movement works (e.g. leading tone resolution, common tones, voice leading).
3. **Voicing & Chord Spelling:** Break down the specific notes (Root, 3rd, 5th, 7th, tensions like 9, 11, or 13) so the user can play it immediately on keys or guitar.
4. **Song DNA Citing:** Reference 1 or 2 famous songs from the 31k database that use that exact chord movement.
