from setuptools import setup, find_packages

setup(
    name="CyCAD",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # Add runtime dependencies here (if any)
    extras_require={
        "dev": [
            "pytest",      # For testing
            "flake8",      # For linting
            "black",       # For code formatting
            "isort",       # For sorting imports
            "mypy",        # For type checking
            "pre-commit"   # For git pre-commit hooks
        ],
    },
)
