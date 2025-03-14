# Anthropic Labs

A simple sandbox environment for exploring and experimenting with Anthropic's Claude AI models and API capabilities.

## Overview

This repository provides a clean, minimal environment for testing various Anthropic API features and capabilities. The included examples demonstrate how to interact with Claude models for different use cases.

## Features

- Clean environment for experimenting with Anthropic's Claude models
- Simple example scripts demonstrating API usage patterns
- Environment variable management for API keys
- Support for Claude's advanced features (tools, function calling, etc.)

## Requirements

- Python 3.8+
- Anthropic API key

## Dependencies

- `anthropic` - Anthropic API client library
- `python-dotenv` - For loading environment variables from a .env file

## Setup

1. Clone this repository
2. Install the required packages using uv (recommended):
   ```
   uv pip install -r requirements.txt
   ```
   Or using pip:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

The repository contains example scripts that showcase different Anthropic API capabilities:

```
python anthropic_simple.py
```

Feel free to modify the examples or create your own scripts to explore specific capabilities:

- Different Claude model versions
- Temperature and other parameter tuning
- System prompts and specialized assistants
- Tool usage and function calling
- Response formatting and structured outputs

## Customization

You can use this environment as a starting point for:
- Testing new Claude models as they become available
- Prototyping AI features for your applications
- Comparing model behaviors with different prompting strategies
- Experimenting with advanced features like tool use

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com/en/docs/welcome)
- [Claude Prompt Design Guide](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)

## License

MIT