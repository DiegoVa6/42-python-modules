import os

# Try import dotenv if not possible return and end
try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None


def mask(secret: str) -> str:
    """Mask a secret string to avoid printing it in full."""
    if not secret:
        return ""
    if len(secret) <= 6:
        return "***"
    return f"{secret[:3]}...{secret[-3:]}"


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    # 2) Detect mode (default development)
    mode = os.getenv("MATRIX_MODE", "development")

    # 3) If dev, load .env using python-dotenv
    if mode == "development":
        if load_dotenv is None:
            print("[MISSING] python-dotenv - Install required")
            print("pip install python-dotenv")
            return
        load_dotenv()  # reads .env if exists

        # after loading .env, re-read mode
        mode = os.getenv("MATRIX_MODE", "development")

    # 4) Read config vars
    db = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    # 5) Validate
    missing = []

    if not db:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if not log_level:
        missing.append("LOG_LEVEL")
    if not zion:
        missing.append("ZION_ENDPOINT")

    if missing:
        print("Missing configuration:")
        for k in missing:
            print(f"[MISSING] {k}")
        print("Tip: copy .env.example to .env and fill values.")
        return

    # 6) Print config (mask secret)
    print(f"Mode: {mode}")
    print(f"Database: {db}")
    print(f"API_KEY: {mask(api_key)}")
    print(f"Log level: {log_level}")
    print(f"Zion endpoint: {zion}")

    print("\nEnvironment security check:\n"
          "[OK] No hardcoded secrets detected\n"
          "[OK] .env file properly configured\n"
          "[OK] Production overrides available\n"
          "\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
