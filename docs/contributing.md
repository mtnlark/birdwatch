# Contributing to Birdwatch

Hi there! 👋 As mentioned on the main page, Birdwatch is primarily a solo demo project I built to play around with tracking my own bird sightings locally and to serve as an example of Python CLI development with documentation.

## Quick Links
- [Project Repository](https://github.com/mtnlark/birdwatch)
- [Usage Documentation](usage.md)
- [Technical Reference](reference.md)

## Ways to Contribute

### Using Birdwatch
The best way to contribute is honestly just to use Birdwatch! If you find it helpful for logging your own bird sightings, that's awesome. And if you're using it as inspiration or reference for your own projects, even better!

### Reporting Issues
If you run into any problems, feel free to [open an issue](https://github.com/mtnlark/birdwatch/issues) on GitHub. When reporting issues:

1. Check if the issue already exists
2. Include your Python version (`python --version`)
3. Describe what you were trying to do
4. Include any error messages
5. If possible, include steps to reproduce the issue

### Code Contributions
While this is mainly a personal project, I'm open to pull requests that:

- Fix bugs
- Improve documentation
- Add useful error messages
- Enhance code comments
- Fix typos

If you're thinking about adding new features, please open an issue first to discuss!

## Development Setup

1. Fork and clone the repository:
```bash
git clone https://github.com/yourusername/birdwatch.git
cd birdwatch
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

To run the documentation site locally:
```bash
mkdocs serve
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include comments for complex logic
- Keep functions focused and small

## Documentation

If you're updating documentation:

- Keep the friendly, conversational tone
- Include practical examples
- Update both the relevant .md file and docstrings if applicable
- Check that all links work
- Preview your changes locally, if possible

## Commit Messages

Write clear commit messages that explain:

- What changes you made
- Why you made them
- Any special considerations

Example:
```
Add error message for invalid species names

- Improves user experience by providing clear feedback
- Helps users catch typos in species names
- Includes suggestion for common misspellings
```

## A Note on Scope

Remember, Birdwatch is intentionally simple! It's meant to be:
- A personal bird sighting logger
- An example of Python CLI development
- A documentation reference

If you're a dedicated birder who wants more comprehensive features, like adding media or tracking sightings in detail over the long term, you'll probably be better served [eBird](https://ebird.org), [iNaturalist](https://www.inaturalist.org), and similarly full-featured birding apps.

## Questions?

Feel free to [open an issue](https://github.com/mtnlark/birdwatch/issues) if you have any questions. Happy birding! 🐦
