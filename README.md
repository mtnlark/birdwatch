# Birdwatch 🐦

A command-line tool for logging and managing bird sightings, with documentation via MkDocs and GitHub Pages.

## Features

- Log bird sightings with species, location, count, and notes
- List all sightings with optional filtering by species and/or location
- Export sightings to CSV format
- Simple and intuitive command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mtnlark/birdwatch.git
cd birdwatch
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Documentation

🌐 **View the documentation:** [Birdwatch Documentation](https://birdwatch.levcraig.com)

## Usage

### Log a Sighting

```bash
# Basic usage
python -m birdwatch.cli log "American Robin"

# With all options
python -m birdwatch.cli log "American Robin" --location "Central Park" --count 2 --notes "Singing in tree"
```

### List Sightings

```bash
# List all sightings
python -m birdwatch.cli list

# Filter by species
python -m birdwatch.cli list --species "American Robin"

# Filter by location
python -m birdwatch.cli list --location "Central Park"

# Filter by both species and location
python -m birdwatch.cli list --species "American Robin" --location "Central Park"
```

### Export Sightings

```bash
# Export with auto-generated filename (includes timestamp)
python -m birdwatch.cli export

# Export with custom filename
python -m birdwatch.cli export --filename my_sightings.csv
```

## Data Storage

Sightings are stored in a local JSON file (`sightings.json`). The CSV export feature allows you to export your data in a format suitable for spreadsheet applications or data analysis.

## Contributing

This is just a fun little project I built for myself! If you're the kind of person who's interested in logging bird sightings with this level of detail, I have a feeling you're already on eBird or would have a much better time there. (But if you feel a burning desire to contribute, hey, feel free to reach out!)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
