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

## Bugs

Some artist pages are actually album pages (usually when artist have only one album). Currently `bandasync` can not handle them properly

If you found another bug, please report [here](https://github.com/MentalBlood/bandasync/issues)