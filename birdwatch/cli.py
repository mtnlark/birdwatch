import click
from birdwatch import sightings

@click.group()
def cli():
    """Command line interface for birdwatch, a tool for logging and managing bird sightings.
    
    This CLI provides commands for logging new bird sightings, listing existing sightings, and filtering by species.
    """
    pass

@cli.command()
@click.argument('species')
@click.option('--location', prompt="Location", help="Location of the sighting")
@click.option('--count', default=1, help="Number of individuals seen", show_default=True)
@click.option('--notes', prompt="Notes (optional)", help="Additional notes about the sighting", 
              default='', show_default=False)
def log(species, location, count, notes): 
    """Log a new bird sighting in the system.
    
    Args:
        species (str): The species of bird observed
        location (str): The location where the bird was seen
        count (int): Number of individuals observed (default: 1)
        notes (str): Optional additional notes about the sighting
        
    Example:
        $ birdwatch log "American Robin" --location "Central Park" --count 2 --notes "Singing in tree"
    """
    sighting = sightings.log_sighting(species=species, location=location, notes=notes, count=count)


@cli.command()
@click.option('--species', help="Filter results by species name (optional)")
@click.option('--location', help="Filter results by location (optional)")
def list(species, location):
    """List recent bird sightings from the database.
    
    Args:
        species (str, optional): If provided, filter sightings to show only this species
        location (str, optional): If provided, filter sightings to show only this location
        
    Example:
        $ birdwatch list
        $ birdwatch list --species "American Robin"
        $ birdwatch list --location "Central Park"
        $ birdwatch list --species "American Robin" --location "Central Park"
    """
    sightings.list_sightings(species, location)

@cli.command()
def hello():
    """Display a welcome message from the birdwatch application.
    
    This is a simple test command that prints a friendly greeting.
    """
    click.echo("Hello from birdwatch! 🐦")

@cli.command()
@click.option('--filename', help="Name of the CSV file to create (optional)")
def export(filename):
    """Export all bird sightings to a CSV file.
    
    Args:
        filename (str, optional): Name of the CSV file to create. If not provided,
                                a default name with timestamp will be used.
                                
    Example:
        $ birdwatch export
        $ birdwatch export --filename my_sightings.csv
    """
    sightings.export_sightings_to_csv(filename)

if __name__ == "__main__":
    cli()