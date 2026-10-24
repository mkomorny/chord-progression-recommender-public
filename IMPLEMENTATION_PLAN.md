# Implementation Plan: Chord Progression Recommender

Mines 31,032 real-world song chord sequences from the Lakh MIDI dataset on Drive B to recommend mathematically and musically proven chord transitions and full progressions.

---

## Deliverables Checklist

### v1.0.0 — Initial Release
- [x] **Core Transition Miner**: `scripts/recommend_chords.py` querying PyArrow Parquet table across 31,032 songs (`train-00000-of-00001.parquet`). ✅ done in v1.0.0
- [x] **Chord Alias Normalizer**: Clean mapping for minor/major chord notation strings (e.g. `amin`, `a min`, `a minor`, `cmaj`). ✅ done in v1.0.0
- [x] **Sub-sequence Progression Matcher**: Multi-chord sequence lookup finding songs that share a progression. ✅ done in v1.0.0
- [x] **Tri-Platform Accessibility**: Canonical `.agents` installation linked to Claude, Grok, and Antigravity via NTFS junctions. ✅ done in v1.0.0
- [x] **Standard Documentation Suite**: `SKILL.md`, `HOW_TO_USE.txt`, `README.md`, `App Changes Tracker.html`, and `dev-notes-v1.0.0.md`. ✅ done in v1.0.0

---

## Roadmap & Future Enhancements

### v1.1.0 — Harmonic Context & Voice Leading Intelligence
- [ ] Add genre-filtered transition weighting (e.g. filter by Rock, Jazz, Electronic, Pop).
- [ ] Automatic key context inference to weight diatonic vs chromatic chord transitions.
- [ ] Smooth voice leading suggestions (inversion calculator to minimize half-step motion).

### v1.2.0 — Extended Tensions & DAW Integration
- [ ] Extended tension mining (9ths, 11ths, 13ths, altered dominant chords).
- [ ] Direct export bridge into `ableton-midi-chord-builder` with custom voicings.
- [ ] Camelot wheel and relative key harmonization recommendations.
