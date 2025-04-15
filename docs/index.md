# Birdwatch Documentation

Welcome to the Birdwatch documentation! Birdwatch is a simple command-line tool for logging and listing bird sightings.

## Quick Start

```bash
# Install
git clone https://github.com/mtnlark/birdwatch.git
cd birdwatch
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Log your first sighting
python -m birdwatch.cli log "American Robin"
```

## Documentation Sections

### [Usage Guide](usage.md)
Comprehensive guide with detailed examples for:

- Logging bird sightings
- Listing and filtering observations
- Exporting data to CSV
- Best practices and tips

### [Technical Reference](reference.md)
Detailed technical documentation covering:

- Complete command reference
- Parameter specifications
- Data formats
- Error handling
- System requirements

## Key Features

- 🦜 Simple command-line interface for logging bird sightings
- 🔍 Filter sightings by species or location
- 📊 Export data to CSV for analysis
- 📝 Add detailed notes to each observation
- 💾 Local JSON storage for all sightings

## Common Actions

### Log Sightings
```bash
# Basic sighting
python -m birdwatch.cli log "Northern Cardinal"

# Detailed sighting
python -m birdwatch.cli log "American Robin" \
    --location "Central Park" \
    --count 2 \
    --notes "Pair with nest-building materials"
```

### View Sightings
```bash
# View all
python -m birdwatch.cli list

# Filter by species
python -m birdwatch.cli list --species "American Robin"

# Filter by location
python -m birdwatch.cli list --location "Central Park"
```

### Export Data
```bash
# Quick export
python -m birdwatch.cli export

# Named export
python -m birdwatch.cli export --filename "my_sightings.csv"
```

## Getting Help

- Use `--help` with any command for more information
- Check the [Usage Guide](usage.md) for detailed examples
- Consult the [Technical Reference](reference.md) for complete documentation
- Visit the [GitHub repository](https://github.com/mtnlark/birdwatch) for any updates

## Contributing

This is primarily a solo demo project I built to play around with tracking my own bird sightings locally and to serve as an example of Python CLI development with documentation. While it's mainly here for personal use, feel free to:

- Fork the repository
- Submit issues for bugs or suggestions
- Use it as inspiration for your own birding + coding fun!

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/mtnlark/birdwatch/blob/main/LICENSE) file for details.
