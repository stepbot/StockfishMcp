# Stockfish MCP Server

This project implements a simple MCP (Model Context Protocol) server that allows an LLM to play chess against the Stockfish engine.

## Features

- Play a game of chess against Stockfish.
- Get the board state in FEN and Markdown format.
- Make moves using UCI notation.
- Reset the game with a specific skill level for the engine.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd StockfishMcp
    ```

2.  **Install `uv`:**
    If you don't have `uv` installed, you can install it with:
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    After installation, you may need to add the installation directory (usually `C:\Users\<YourUser>\.local\bin` on Windows) to your system's PATH and restart your terminal.

3.  **Download Stockfish:**
    You need to download the Stockfish engine separately. You can find it on the [official Stockfish website](https://stockfishchess.org/download/).

4.  **Configure the MCP Server:**
    To use this server, you must add an entry for it in your global `mcp_settings.json` file. This file tells your MCP client how to launch the server.

    An example configuration is provided in `mcp_settings.example.json`. You should copy this configuration into your `mcp_settings.json` file and update the following paths:
    - The path to the `mcp_server.py` script in this project.
    - The path to your downloaded Stockfish executable for the `--stockfish-path` argument.

## Usage

The server is managed by your MCP client and will be launched using `uv`. `uv` will automatically handle the virtual environment and dependencies from `requirements.txt`. The MCP client will pass the `--stockfish-path` argument to the server on startup.

## Available Tools

- `get_board_state()`: Get the current board state.
- `make_move(move_uci: str)`: Make a move (e.g., "e2e4").
- `is_game_over()`: Check if the game has ended.
- `get_game_result()`: Get the result if the game is over.
- `reset_game(skill_level: int = 10)`: Start a new game.