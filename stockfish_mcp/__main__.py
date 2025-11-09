import argparse
import os
import platform
import sys
from .mcp_server import mcp, game
from .chess_logic import ChessGame

def get_stockfish_path():
    """
    Determines the path to the correct Stockfish binary based on the OS and architecture.
    """
    system = platform.system()
    machine = platform.machine()
    
    base_path = os.path.join(os.path.dirname(__file__), 'bin')

    if system == "Linux":
        return os.path.join(base_path, "stockfish-ubuntu-x86-64-avx2")
    elif system == "Windows":
        return os.path.join(base_path, "stockfish-windows-x86-64-avx2.exe")
    elif system == "Darwin": # macOS
        if machine == "arm64":
            return os.path.join(base_path, "stockfish-macos-arm64")
        else:
            return os.path.join(base_path, "stockfish-macos-x86-64")
    
    raise OSError("Unsupported operating system")


def main():
    parser = argparse.ArgumentParser(description="Run the Chess MCP server.")
    parser.add_argument("--stockfish-path", help="Path to a custom Stockfish executable.")
    args = parser.parse_args()

    stockfish_path = args.stockfish_path if args.stockfish_path else get_stockfish_path()

    global game
    game = ChessGame(stockfish_path=stockfish_path, skill_level=10)
    mcp.run()

if __name__ == "__main__":
    main()