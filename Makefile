# Install Python dependencies and Playwright browsers
install:
	pip install -r requirements.txt
	playwright install

# Run tests using pytest
test:
	.venv/bin/pytest

# Clean up .pyc files
clean:
	find . -name "*.pyc" -exec rm -f {} \;

# Example command for running tests in headless mode
test-headless:
	pytest --headless
