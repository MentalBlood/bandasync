# Bandasync

Fast. Stubborn. Tool for downloading audio from bandcamp

Remake of [banduncamp](https://github.com/MentalBlood/banduncamp)

Differences:

* Based on `asyncio` module
* Cleaner architecture and code

## Installation

```bash
pip install git+https://github.com/MentalBlood/bandasync
```

## Usage

To get help:

```bash
python -m bandasync -h
```

Tool will not download audio file if it already exists

Tool will not download album if `*mp3` files are exist in corresponding dir already

### Album:

```bash
python -m bandasync https://artist_name.bandcamp.com/album/album_name
```

### Discography:

```bash
python -m bandasync https://artist_name.bandcamp.com/music
```

### Tasks

```bash
python -m bandasync -f <path_to_json>
```

JSON should be like:

```json
{
    "D:/music/Ambient": [
        "https://lalala.bandcamp.com/music",
        "https://lololo.bandcamp.com/releases"
    ],
    "D:/music/Dungeon Synth": [
        "https://lululu.bandcamp.com/album/wow",
        "https://lilili.bandcamp.com/music"
    ]
}
```

## Bugs

No known, if you found one please report [here](https://github.com/MentalBlood/bandasync/issues)