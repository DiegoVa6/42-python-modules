import os
import site
import sys


def main() -> None:
    try:
        #  Detect virtual environment:
        # In a global Python install: sys.prefix == sys.base_prefix
        # In a venv: sys.prefix points to the venv folder and differs from base_prefix
        is_venv = sys.prefix != sys.base_prefix
        current_python = sys.executable

        if not is_venv:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {current_python}")
            print("Virtual Environment: None detected\n")
            print(
                "WARNING: You're in the global environment!\n"
                "The machines can see everything you install.\n\n"
                "To enter the construct, run:\n"
                "python -m venv matrix_env\n"
                "source matrix_env/bin/activate # On Unix\n"
                "matrix_env\n"
                "Scripts\n"
                "activate # On Windows\n\n"
                "Then run this program again."
            )
        else:
            venv_name = os.path.basename(sys.prefix)
            env_path = sys.prefix

            try:
                install_path = site.getsitepackages()[0]
            except (AttributeError, IndexError):
                install_path = "Unknown"

            print("MATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {current_python}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {env_path}\n")
            print(
                "SUCCESS: You're in an isolated environment!\n"
                "Safe to install packages without affecting\n"
                "the global system.\n\n"
                f"Package installation path:\n{install_path}"
            )
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
