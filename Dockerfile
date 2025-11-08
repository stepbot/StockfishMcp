# Stage 1: Build stage to download and extract Stockfish
FROM ubuntu:22.04 AS stockfish_builder

# Install curl and tar
RUN apt-get update && apt-get install -y curl tar

# Download and extract Stockfish
WORKDIR /app
RUN curl -sL https://github.com/official-stockfish/Stockfish/releases/latest/download/stockfish-ubuntu-x86-64-avx2.tar | tar -x

# Stage 2: Final stage
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy Stockfish binary from the build stage
COPY --from=stockfish_builder /app/stockfish/stockfish-ubuntu-x86-64-avx2 /usr/local/bin/stockfish

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install uv && uv pip install --no-cache-dir -r requirements.txt


# Add MCP server name label
LABEL io.modelcontextprotocol.server.name="io.github.stepbot/stockfish-mcp"

# Command to run the server
CMD ["uv", "run", "--host", "0.0.0.0", "--port", "8080", "--", "python", "mcp_server.py", "--stockfish-path", "/usr/local/bin/stockfish"]