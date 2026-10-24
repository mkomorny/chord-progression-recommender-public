#!/usr/bin/env python3
r"""
Chord Progression Recommender Engine
Mines 31,032 real-world song chord sequences from B:\DATABASES\Music_Audio\Music_Theory\midi_datasets\lmd_chords
"""

import sys
import json
import argparse
from pathlib import Path
from collections import Counter

try:
    import pyarrow.parquet as pq
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyarrow"])
    import pyarrow.parquet as pq

DATASET_PATH = Path(r"B:\DATABASES\Music_Audio\Music_Theory\midi_datasets\lmd_chords\train-00000-of-00001.parquet")

CHORD_ALIASES = {
    "amin": "Am", "a min": "Am", "a minor": "Am", "a-": "Am",
    "bmin": "Bm", "b min": "Bm", "b minor": "Bm", "b-": "Bm",
    "cmin": "Cm", "c min": "Cm", "c minor": "Cm", "c-": "Cm",
    "dmin": "Dm", "d min": "Dm", "d minor": "Dm", "d-": "Dm",
    "emin": "Em", "e min": "Em", "e minor": "Em", "e-": "Em",
    "fmin": "Fm", "f min": "Fm", "f minor": "Fm", "f-": "Fm",
    "gmin": "Gm", "g min": "Gm", "g minor": "Gm", "g-": "Gm",
    "cmaj": "C", "dmaj": "D", "emaj": "E", "fmaj": "F", "gmaj": "G", "amaj": "A", "bmaj": "B",
    "c major": "C", "d major": "D", "e major": "E", "f major": "F", "g major": "G", "a major": "A", "b major": "B"
}

def clean_chord(c_str):
    if not c_str:
        return ""
    c_str = c_str.strip()
    low = c_str.lower()
    if low in CHORD_ALIASES:
        return CHORD_ALIASES[low]
    # Standardize sharps/flats
    return c_str

def load_data():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(f"LMD chords dataset not found at: {DATASET_PATH}")
    return pq.read_table(str(DATASET_PATH), columns=['title', 'artist', 'year', 'chords'])

def get_next_chords(current_chord, top_k=5):
    target = clean_chord(current_chord)
    table = load_data()
    next_counts = Counter()
    song_matches = {}

    num_rows = table.num_rows
    for i in range(num_rows):
        symbols = table['chords'][i]['symbol'].as_py()
        artist = table['artist'][i].as_py() or "Unknown Artist"
        title = table['title'][i].as_py() or "Untitled"
        year = table['year'][i].as_py() or ""
        
        for j in range(len(symbols) - 1):
            s1 = symbols[j]
            s2 = symbols[j+1]
            if s1 == target and s2 != 'N' and s2 != target:
                next_counts[s2] += 1
                if s2 not in song_matches:
                    song_matches[s2] = []
                if len(song_matches[s2]) < 2 and (artist, title) not in [(x['artist'], x['title']) for x in song_matches[s2]]:
                    song_matches[s2].append({"artist": artist, "title": title, "year": year})

    total_transitions = sum(next_counts.values()) or 1
    results = []
    for chord, count in next_counts.most_common(top_k):
        pct = round((count / total_transitions) * 100, 1)
        results.append({
            "chord": chord,
            "count": count,
            "percentage": pct,
            "examples": song_matches.get(chord, [])
        })

    return {
        "input_chord": target,
        "total_occurrences": total_transitions,
        "recommendations": results
    }

def find_songs_by_progression(progression_str, max_songs=8):
    chords = [clean_chord(c) for c in progression_str.replace("->", ",").replace("-", ",").split(",") if c.strip()]
    if not chords:
        return {"error": "No valid chords provided."}

    table = load_data()
    matched_songs = []
    num_rows = table.num_rows

    for i in range(num_rows):
        symbols = table['chords'][i]['symbol'].as_py()
        # Search for exact or near sub-sequence
        n = len(chords)
        for j in range(len(symbols) - n + 1):
            if symbols[j:j+n] == chords:
                artist = table['artist'][i].as_py() or "Unknown Artist"
                title = table['title'][i].as_py() or "Untitled"
                year = table['year'][i].as_py() or ""
                matched_songs.append({
                    "artist": artist,
                    "title": title,
                    "year": year,
                    "progression": chords
                })
                break
        if len(matched_songs) >= max_songs:
            break

    return {
        "queried_progression": chords,
        "match_count": len(matched_songs),
        "songs": matched_songs
    }

def main():
    parser = argparse.ArgumentParser(description="Query chord transitions and progressions from 31,000 songs.")
    parser.add_argument("--after", help="Recommend chords that follow this chord (e.g. 'Am', 'Dm9', 'G7')")
    parser.add_argument("--progression", help="Find songs matching a progression (e.g. 'Am,F,C,G')")
    parser.add_argument("--limit", type=int, default=5, help="Number of results")
    args = parser.parse_args()

    if args.after:
        res = get_next_chords(args.after, top_k=args.limit)
        print(json.dumps(res, indent=2))
    elif args.progression:
        res = find_songs_by_progression(args.progression, max_songs=args.limit)
        print(json.dumps(res, indent=2))
    else:
        print(json.dumps({"error": "Please provide --after <chord> or --progression <chords>"}))

if __name__ == "__main__":
    main()
