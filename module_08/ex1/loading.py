import importlib
from importlib.metadata import version, PackageNotFoundError
from typing import Tuple


def check_dependency(module_name: str) -> Tuple[bool, str]:
    """
    Check whether a module can be imported and return (is_installed, version_str).

    - importlib.import_module(): tries a real import (will fail if not installed).
    - importlib.metadata.version(): reads installed package version (no heavy import).
    """
    try:
        importlib.import_module(module_name)
        return True, version(module_name)
    except (ModuleNotFoundError, PackageNotFoundError):
        return False, ""


def print_install_instructions() -> None:
    """Print of necessary instructions for virtual environments"""
    print("\nMissing dependencies detected.")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Or install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def run_analysis() -> None:
    """
    Minimal analysis to demonstrate that numpy/pandas/matplotlib work:
    - create sample data
    - plot it
    - save to matrix_analysis.png
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data.")
    n = 1000
    print("Processing 1000 data points.")
    print("Generating visualization.")

    df = pd.DataFrame({"x": np.arange(n), "y": np.arange(n)})
    plt.figure()
    plt.plot(df["x"], df["y"])
    plt.savefig("matrix_analysis.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    deps = [
            ("pandas", "Data manipulation ready"),
            ("requests", "Network access ready"),
            ("matplotlib", "Visualization ready"),
            ("numpy", "Numerical computations ready"),
        ]

    missing_any = False
    for module_name, msg in deps:
        ok, ver = check_dependency(module_name)
        if ok:
            print(f"[OK] {module_name} ({ver}) - {msg}")
        else:
            missing_any = True
            print(f"[MISSING] {module_name} - Install required")

    if missing_any:
        print_install_instructions()
        return

    run_analysis()


if __name__ == "__main__":
    main()
