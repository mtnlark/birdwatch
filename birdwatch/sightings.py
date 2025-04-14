# birdwatch/sightings.py

import json
import os
import click
import csv
from datetime import datetime

SIGHTINGS_FILE = "sightings.json"

def load_sightings():
    """Load bird sightings from the JSON storage file.
    
    Returns:
        list: A list of dictionaries containing sighting data. Returns an empty list
              if the storage file doesn't exist.
    """
    if not os.path.exists(SIGHTINGS_FILE):
        return []
    with open(SIGHTINGS_FILE, 'r') as f:   
        return json.load(f)
    
def save_sightings(sightings):
    """Save bird sightings to the JSON storage file.
    
    Args:
        sightings (list): List of dictionaries containing sighting data to be saved
    """
    with open(SIGHTINGS_FILE, 'w') as f:
        json.dump(sightings, f, indent=2)

def log_sighting(species, location, notes, count=1):
    """Log a new bird sighting and save it to the storage file.
    
    Args:
        species (str): The species of bird observed
        location (str): The location where the bird was seen
        notes (str): Additional notes about the sighting
        count (int, optional): Number of individuals observed. Defaults to 1.
        
    Returns:
        dict: The newly created sighting record
        
    Example:
        >>> log_sighting("American Robin", "Central Park", "Singing in tree", 2)
        Sighting logged: 2 American Robin at Central Park
    """
    sightings = load_sightings()
    sighting = {
        "species": species,
        "location": location,
        "notes": notes,
        "count": count
    }
    sightings.append(sighting)
    save_sightings(sightings)
    click.echo(f"Sighting logged: {sighting['count']} {sighting['species']} at {sighting['location']}")
    return sighting

def list_sightings(species_filter=None, location_filter=None):
    """Display all logged bird sightings, optionally filtered by species and/or location.
    
    Args:
        species_filter (str, optional): If provided, only show sightings for this species.
                                      Case-insensitive matching is used.
        location_filter (str, optional): If provided, only show sightings from this location.
                                       Case-insensitive matching is used.
    
    The function will display a formatted list of sightings, including:
    - Species name
    - Location
    - Number of individuals
    - Any additional notes
    
    If no sightings are found (either in total or matching the filters),
    an appropriate message will be displayed.
    """
    sightings = load_sightings()
    if not sightings:
        click.echo("No sightings logged yet.")
        return
    
    # Apply filters if provided
    if species_filter or location_filter:
        filtered_sightings = sightings
        if species_filter:
            filtered_sightings = [s for s in filtered_sightings 
                                if s['species'].lower() == species_filter.lower()]
        if location_filter:
            filtered_sightings = [s for s in filtered_sightings 
                                if s['location'].lower() == location_filter.lower()]
        
        if not filtered_sightings:
            filter_msg = []
            if species_filter:
                filter_msg.append(f"species: {species_filter}")
            if location_filter:
                filter_msg.append(f"location: {location_filter}")
            click.echo(f"No sightings found for {' and '.join(filter_msg)}")
            return
            
        sightings = filtered_sightings
        
    click.echo("Logged sightings:")
    for i, s in enumerate(sightings, start=1):
        count = s.get('count', 1)
        click.echo(f"{i}. {s['count']} {s['species']} at {s['location']}")
        if s['notes']:
            click.echo(f"   Notes: {s['notes']}")

def export_sightings_to_csv(filename=None):
    """Export all bird sightings to a CSV file.
    
    Args:
        filename (str, optional): Name of the CSV file to create. If not provided,
                                a default name with timestamp will be used.
    
    Returns:
        str: The name of the created CSV file
        
    The CSV file will contain the following columns:
    - Species
    - Location
    - Count
    - Notes
    - Timestamp (of export)
    """
    sightings = load_sightings()
    if not sightings:
        click.echo("No sightings to export.")
        return None
        
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bird_sightings_{timestamp}.csv"
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['species', 'location', 'count', 'notes', 'export_timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for sighting in sightings:
                # Create a copy of the sighting to add timestamp without modifying original
                row = sighting.copy()
                row['export_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow(row)
                
        click.echo(f"Successfully exported {len(sightings)} sightings to {filename}")
        return filename
    except Exception as e:
        click.echo(f"Error exporting sightings: {str(e)}")
        return None
