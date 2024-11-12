# Development Setup

## Environment Setup
This project uses a virtual environment to manage dependencies. Follow these steps to set up your development environment:

1. Ensure you have Python 3.x installed on your system
   ```bash
   python --version  # Should show Python 3.x
   ```

2. Clone the repository
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

3. Create a virtual environment
   ```bash
   # Create the virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Adding New Dependencies
When you need to add new packages to the project:

1. Ensure your virtual environment is activated
2. Install the package using pip:
   ```bash
   pip install package_name
   ```
3. Update requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```
4. Commit the updated requirements.txt to the repository

## Deactivating the Environment
When you're done working on the project:
```bash
deactivate
```

## Common Issues
- If you see "command not found: pip", try using `python -m pip` instead
- If you're having permission issues, don't use `sudo` with pip. Instead, check that your virtual environment is activated
- If you're getting errors about missing packages, make sure your virtual environment is activated and you've installed all requirements

## Notes
- Never commit your virtual environment directory (venv/) to git
- Always activate the virtual environment before working on the project
- Make sure to update requirements.txt whenever you add new dependencies


## PyCharm Configuration
If using PyCharm:
1. Open the project in PyCharm
2. Go to Settings/Preferences → Project → Python Interpreter
3. Click the gear icon → Add
4. Select "Existing Environment"
5. Browse to `venv/bin/python3` (Mac/Linux) or `venv\Scripts\python.exe` (Windows)
6. Click Apply/OK