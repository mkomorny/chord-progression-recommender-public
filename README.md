# Chord Progression Recommender

> **Tri-Platform Agent Skill** for Claude Desktop / Code, Grok CLI, and Google Antigravity / Gemini.  
> Mines 31,032 real-world song chord sequences from the Lakh MIDI dataset on Drive B to recommend mathematically and musically proven chord transitions and full progressions.

---

## Overview

When writing music, producers and songwriters frequently encounter creative blocks:
* *"I have a verse chord movement — what chord should come next?"*
* *"What is an unexpected, spicy turnaround chord to lead into the chorus?"*
* *"Has anyone written a hit using this specific four-chord loop?"*

Instead of relying on generic boilerplate rules, **`chord-progression-recommender`** queries a pre-compiled dataset of **31,032 analyzed songs** stored locally on Drive B. It calculates statistical transition frequencies, isolates top chord movements, and cites real famous songs that utilize the exact same harmonic DNA.

---

## Dataset & Technical Details

- **Dataset Location**: `B:\DATABASES\Music_Audio\Music_Theory\midi_datasets\lmd_chords\train-00000-of-00001.parquet`
- **Volume**: 31,032 unique songs with parsed chord sequences, metadata (artist, title, release year), and symbolic labels.
- **Query Engine**: `scripts/recommend_chords.py` leveraging Apache PyArrow (`pyarrow.parquet`) for sub-second in-memory column filtering.

---

## CLI Usage

The core Python script can be run standalone or silently invoked by AI agents:

### 1. Finding Top Next Chords
Find the most frequent chords that follow a specific root or chord symbol:
```bash
python scripts/recommend_chords.py --after "Am" --limit 5
```

**Output**:
```json
{
  "input_chord": "Am",
  "total_occurrences": 77799,
  "recommendations": [
    {
      "chord": "F",
      "count": 9916,
      "percentage": 12.7,
      "examples": [
        { "artist": "Daniel Balavoine", "title": "Sauver L'Amour", "year": 1985 },
        { "artist": "Verona", "title": "La Musica", "year": "" }
      ]
    },
    {
      "chord": "G",
      "count": 8641,
      "percentage": 11.1,
      "examples": [
        { "artist": "Russ Taff", "title": "I Cry (LP Version)", "year": "" }
      ]
    }
  ]
}
```

### 2. Searching by Chord Progression
Discover songs that feature a specific multi-chord sequence:
```bash
python scripts/recommend_chords.py --progression "Am,F,C,G" --limit 6
```

---

## Agent Chat Presentation Protocol

When recommending chords back to the user in chat, agents follow a 4-part presentation framework:

1. **Top Categorized Next Moves**:
   - **The Strong Resolution**: Dominant or tonic arrivals ($ii \rightarrow V$, $V \rightarrow I$).
   - **The Modal / Emotional Color**: Relative keys, borrowed chords ($\flat\text{VI}$, $\text{iv}$).
   - **The Surprise Turnaround**: Tritone substitutions, secondary dominants, or passing chromatic chords.
2. **Harmonic Explanation & Roman Numerals**: Voice leading rationale, shared common tones, and scale degrees.
3. **Voicing & Chord Spelling**: Clear note-by-note breakdown (Root, 3rd, 5th, 7th, 9th) for immediate piano/guitar playback.
4. **Song DNA Citing**: 1–2 real songs from the database exemplifying the transition.

---

## Tri-Platform Architecture

Zero duplicate code across tools. Canonical source resides in `.agents`:
- **Canonical**: `C:\Users\<you>\.agents\skills\chord-progression-recommender`
- **Claude**: `C:\Users\<you>\.claude\skills\chord-progression-recommender` (NTFS Junction)
- **Grok**: `C:\Users\<you>\.grok\skills\chord-progression-recommender` (NTFS Junction)
- **Antigravity**: `C:\Users\<you>\.gemini\config\skills\chord-progression-recommender` (NTFS Junction)

---

## Documentation Suite

- [`HOW_TO_USE.txt`](file:///C:/Users/<you>/.agents/skills/chord-progression-recommender/HOW_TO_USE.txt): Standardized user guide and prompt templates.
- [`IMPLEMENTATION_PLAN.md`](file:///C:/Users/<you>/.agents/skills/chord-progression-recommender/IMPLEMENTATION_PLAN.md): Feature checklist and roadmap.
- [`App Changes Tracker.html`](file:///C:/Users/<you>/.agents/skills/chord-progression-recommender/App%20Changes%20Tracker.html): Interactive visual version log.
- [`SKILL.md`](file:///C:/Users/<you>/.agents/skills/chord-progression-recommender/SKILL.md): Agent system instructions and triggers.
