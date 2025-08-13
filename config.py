"""Configuration for the seamless interaction project."""
from pathlib import Path
from seamless_interaction.fs import DatasetConfig

# Project root directory
PROJECT_ROOT = Path(__file__).parent.resolve()

# Directory structure
DATA_DIR = PROJECT_ROOT / "data"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks" 
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
RESULTS_DIR = ANALYSIS_DIR / "results"
SCRIPTS_DIR = ANALYSIS_DIR / "scripts"

# Sample Set configuration
SAMPLE_CONFIG = DatasetConfig(
    label='improvised',
    split='dev',
    preferred_vendors_only=True,
    local_dir=DATA_DIR / 'sample_set'
)

# Session Groups configuration
SESSION_CONFIG = DatasetConfig(
    label='improvised',
    split='dev',
    preferred_vendors_only=True,
    local_dir=DATA_DIR / 'session_groups'
)
