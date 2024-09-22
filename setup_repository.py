import os
import sys

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)
    print(f"Created file: {path}")

def setup_repository():
    # Create directories
    directories = [
        "data/raw",
        "data/processed",
        "notebooks",
        "scripts",
        "results/figures"
    ]
    for directory in directories:
        create_directory(directory)

    # Create README.md
    readme_content = """# Diversity in STEM Data Analysis

This repository contains our team's work on analyzing diversity in STEM at Berea College.

## Setup

1. Run the setup script:
   ```
   python setup_repository.py
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Start Jupyter Notebook:
   ```
   jupyter notebook
   ```

## Repository Structure

- `notebooks/`: Jupyter notebooks for analysis
- `scripts/`: Python scripts for reusable functions
- `data/`: Raw and processed data files
- `results/figures/`: Generated visualizations

## Contributing

1. Create a new branch for your work
2. Make your changes and commit them
3. Push your branch and create a pull request for review

Please ensure all sensitive data is properly anonymized before committing.
"""
    create_file("README.md", readme_content)

    # Create requirements.txt
    requirements_content = """pandas==1.3.3
matplotlib==3.4.3
seaborn==0.11.2
jupyter==1.0.0
numpy==1.21.2
"""
    create_file("requirements.txt", requirements_content)

    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class

# Jupyter Notebook
.ipynb_checkpoints

# VS Code
.vscode/

# PyCharm
.idea/

# Virtual Environment
venv/

# Data files (uncomment if you don't want to track data files)
# data/

# Results
results/figures/*
!results/figures/.gitkeep

# Environment
.env
.venv
env/
ENV/
"""
    create_file(".gitignore", gitignore_content)

    # Create a sample Jupyter notebook
    notebook_content = """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Diversity in STEM Data Analysis\n",
    "\n",
    "This notebook is a starting point for our analysis of diversity in STEM at Berea College."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Set style for plots\n",
    "plt.style.use('seaborn')\n",
    "sns.set_palette('deep')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Loading\n",
    "\n",
    "Here we'll load our data. Replace 'your_data.csv' with the actual filename."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load data\n",
    "# df = pd.read_csv('data/raw/your_data.csv')\n",
    "# df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Exploration\n",
    "\n",
    "Next, we'll do some basic exploration of our data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Basic info about the dataset\n",
    "# df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Visualization\n",
    "\n",
    "Here we'll create some visualizations to better understand our data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example visualization (uncomment and modify as needed)\n",
    "# plt.figure(figsize=(10, 6))\n",
    "# sns.countplot(x='column_name', data=df)\n",
    "# plt.title('Your Chart Title')\n",
    "# plt.xlabel('X-axis Label')\n",
    "# plt.ylabel('Count')\n",
    "# plt.xticks(rotation=45)\n",
    "# plt.tight_layout()\n",
    "# plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
"""
    create_file("notebooks/01_data_exploration.ipynb", notebook_content)

    # Create an empty .gitkeep file in results/figures
    create_file("results/figures/.gitkeep")

    print("Repository setup complete!")

if __name__ == "__main__":
    setup_repository()
