# Birdwatch Reference

This document provides detailed technical reference for all Birdwatch commands, parameters, data structures, and file formats.

## Command Reference

### Global Options

These options are available for all commands:

```bash
--help    Show help message and exit
```

### log

Records a new bird sighting.

```bash
python -m birdwatch.cli log SPECIES [OPTIONS]
```

#### Parameters

| Parameter | Required | Type | Default | Description |
|-----------|----------|------|---------|-------------|
| `species` | Yes | string | - | Name of the bird species observed |
| `--location` | Prompted | string | - | Location where the bird was seen |
| `--count` | No | integer | 1 | Number of individuals observed |
| `--notes` | Prompted | string | "" | Additional observations |

#### Return Value

Returns a dictionary containing the sighting data:
```python
{
    "species": str,
    "location": str,
    "count": int,
    "notes": str
}
```

### list

Displays recorded bird sightings with optional filtering.

```bash
python -m birdwatch.cli list [OPTIONS]
```

#### Parameters

| Parameter | Required | Type | Default | Description |
|-----------|----------|------|---------|-------------|
| `--species` | No | string | None | Filter by species name (case-insensitive) |
| `--location` | No | string | None | Filter by location (case-insensitive) |

#### Output Format

```
N. [count] [species] at [location]
   Notes: [notes]  # Only shown if notes exist
```

### export

Exports sightings to CSV format.

```bash
python -m birdwatch.cli export [OPTIONS]
```

#### Parameters

| Parameter | Required | Type | Default | Description |
|-----------|----------|------|---------|-------------|
| `--filename` | No | string | "bird_sightings_[timestamp].csv" | Output filename |

#### CSV Format

The exported CSV file contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| species | string | Bird species name |
| location | string | Sighting location |
| count | integer | Number of individuals |
| notes | string | Additional observations |
| export_timestamp | string | ISO format timestamp of export |

## Data Storage

### Sightings File

Sightings are stored in `sightings.json` using the following format:

```json
[
    {
        "species": "American Robin",
        "location": "Central Park - Ramble",
        "count": 2,
        "notes": "Pair building nest in maple tree"
    },
    {
        "species": "Northern Cardinal",
        "location": "Backyard Feeder",
        "count": 1,
        "notes": "Female, eating sunflower seeds"
    }
]
```

### File Locations

| File | Location | Purpose |
|------|----------|---------|
| sightings.json | Working directory | Primary data storage |
| *.csv | User-specified | Data exports |

## Error Handling

### Common Error Messages

| Error Message | Cause | Solution |
|--------------|-------|----------|
| "No sightings logged yet." | Empty sightings file | Log some sightings first |
| "No sightings found for species: X" | No matches for species filter | Check species name spelling |
| "No sightings found for location: X" | No matches for location filter | Check location name spelling |
| "Error exporting sightings: [error]" | Export file write error | Check file permissions and disk space |

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Invalid command usage |

## Dependencies

- *click:* Command line interface creation
- *json:* Data storage
- *csv:* Data export
- *datetime:* Timestamp generation

## Environment Variables

Currently, Birdwatch does not use any environment variables.

## Limitations

- Maximum file size: No explicit limit (limited by system memory)
- Species name length: No explicit limit
- Notes length: No explicit limit
- Location name length: No explicit limit
- Number of sightings: No explicit limit

## Future Considerations

Potential future enhancements that may affect the API:

- Date/time filtering
- Tag-based filtering
- Weather integration
- Geographic coordinates
- Photo attachments

## Version Compatibility

Current version is compatible with:

- Python 3.6+
- Click 7.0+
- All major operating systems (Windows, macOS, Linux)
