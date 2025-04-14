# Using Birdwatch

Birdwatch is a command-line tool for logging and managing bird sightings. This guide covers all available commands and features in detail.

## Basic Commands

All commands are run using the pattern: `python -m birdwatch.cli [command] [arguments]`

## Logging Sightings

The `log` command is used to record new bird sightings.

### Basic Logging
```bash
# Simple sighting with prompted location and notes
python -m birdwatch.cli log "American Robin"
Location: Prospect Park
Notes (optional): Adult male, foraging on lawn

# Quick sighting of multiple birds
python -m birdwatch.cli log "Canada Goose" --location "Lake Park" --count 12 --notes "Flying overhead in V formation"

# Detailed observation
python -m birdwatch.cli log "Northern Cardinal" \
    --location "Backyard Feeder" \
    --count 1 \
    --notes "Female, eating sunflower seeds, appears to be gathering food for nestlings"
```

### Full Logging Options
```bash
# Example of a detailed morning birding session
python -m birdwatch.cli log "American Robin" \
    --location "Central Park - Ramble" \
    --count 2 \
    --notes "Pair building nest in maple tree, collecting mud and grass"

python -m birdwatch.cli log "Black-capped Chickadee" \
    --location "Central Park - Bird Sanctuary" \
    --count 4 \
    --notes "Mixed flock with Tufted Titmouse, actively feeding in birch trees"

python -m birdwatch.cli log "Red-tailed Hawk" \
    --location "Central Park - Great Lawn" \
    --count 1 \
    --notes "Adult perched on lamp post, eating prey (possibly squirrel)"
```

### Log Command Parameters
- `species` (required): The name of the bird species
- `--location` (prompted): Where you saw the bird
- `--count` (optional): Number of individuals seen (default: 1)
- `--notes` (prompted): Any additional observations (optional)

## Listing Sightings

The `list` command displays your recorded sightings with various filtering options.

### View All Sightings
```bash
# Shows all sightings in chronological order
python -m birdwatch.cli list

Example output:
1. 2 American Robin at Central Park - Ramble
   Notes: Pair building nest in maple tree, collecting mud and grass
2. 4 Black-capped Chickadee at Central Park - Bird Sanctuary
   Notes: Mixed flock with Tufted Titmouse, actively feeding in birch trees
3. 1 Red-tailed Hawk at Central Park - Great Lawn
   Notes: Adult perched on lamp post, eating prey (possibly squirrel)
```

### Filtering Options

#### Filter by Species
```bash
# Find all Robin sightings across locations
python -m birdwatch.cli list --species "American Robin"

Example output:
1. 2 American Robin at Central Park - Ramble
   Notes: Pair building nest in maple tree, collecting mud and grass
2. 1 American Robin at Prospect Park
   Notes: Adult male, foraging on lawn

# Track hawk activity
python -m birdwatch.cli list --species "Red-tailed Hawk"

Example output:
1. 1 Red-tailed Hawk at Central Park - Great Lawn
   Notes: Adult perched on lamp post, eating prey (possibly squirrel)
```

#### Filter by Location
```bash
# View all activity in a specific area
python -m birdwatch.cli list --location "Central Park - Bird Sanctuary"

Example output:
1. 4 Black-capped Chickadee at Central Park - Bird Sanctuary
   Notes: Mixed flock with Tufted Titmouse, actively feeding in birch trees

# Monitor backyard activity
python -m birdwatch.cli list --location "Backyard Feeder"

Example output:
1. 1 Northern Cardinal at Backyard Feeder
   Notes: Female, eating sunflower seeds, appears to be gathering food for nestlings
```

#### Filter by Both
```bash
# Track specific species in a particular location
python -m birdwatch.cli list \
    --species "American Robin" \
    --location "Central Park - Ramble"

Example output:
1. 2 American Robin at Central Park - Ramble
   Notes: Pair building nest in maple tree, collecting mud and grass
```

### List Command Parameters
- `--species` (optional): Filter results to show only this species
- `--location` (optional): Filter results to show only sightings from this location

Note: Filters are case-insensitive for easier matching.

## Exporting Data

The `export` command allows you to save your sightings to a CSV file for use in spreadsheets or data analysis.

### Basic Export
```bash
# Export with automatic timestamp
python -m birdwatch.cli export

Example output:
Successfully exported 6 sightings to bird_sightings_20250414_182605.csv

# The resulting CSV might look like:
species,location,count,notes,export_timestamp
"American Robin","Central Park - Ramble",2,"Pair building nest in maple tree, collecting mud and grass","2025-04-14 18:26:05"
"Black-capped Chickadee","Central Park - Bird Sanctuary",4,"Mixed flock with Tufted Titmouse, actively feeding in birch trees","2025-04-14 18:26:05"
"Red-tailed Hawk","Central Park - Great Lawn",1,"Adult perched on lamp post, eating prey (possibly squirrel)","2025-04-14 18:26:05"
```

### Named Export
```bash
# Export with custom filename for monthly record
python -m birdwatch.cli export --filename "april_2025_sightings.csv"

# Export for a specific location
python -m birdwatch.cli export --filename "central_park_records.csv"

# Export for data analysis
python -m birdwatch.cli export --filename "spring_migration_data.csv"
```

### Export Command Parameters
- `--filename` (optional): Custom name for the export file

### CSV Format
The exported CSV file includes the following columns:
- species: The bird species name
- location: Where the bird was seen
- count: Number of individuals
- notes: Additional observations
- export_timestamp: When the export was created

## Data Storage

All sightings are stored locally in a `sightings.json` file. This file is:
- Created automatically when you log your first sighting
- Updated with each new sighting
- Used as the source for listing and exporting
- Can be backed up or version controlled (though it's gitignored by default)

## Tips and Best Practices

1. **Species Names**: Be consistent with species names for easier filtering
2. **Locations**: Use consistent location names to make filtering more effective
3. **Notes**: Include details like behavior, weather, or habitat in the notes
4. **Regular Exports**: Consider regular CSV exports as backups of your data
5. **Multiple Locations**: If you bird-watch in multiple locations, always use the location parameter for better organization

## Error Handling

- If no sightings are found when filtering, you'll receive a clear message
- Invalid commands or parameters will show usage help
- Export errors (like permission issues) will be reported clearly

## Getting Help

For any command, you can add `--help` to see available options:
```bash
python -m birdwatch.cli --help
python -m birdwatch.cli log --help
python -m birdwatch.cli list --help
python -m birdwatch.cli export --help
```
