# Read the .env file in the current directory and export its contents as environment variables
if [ -f .env ]; then
    set -a
    source .env
    set +a
    echo "Environment variables from .env have been exported."
else
    echo ".env file not found in the current directory."
fi
