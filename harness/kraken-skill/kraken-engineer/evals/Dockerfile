FROM ubuntu:24.04

# Install Python 3.12, curl, and git
RUN apt-get update -qq && \
    apt-get install -y -qq python3 python3-pip python3-venv curl git && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/python3 /usr/local/bin/python && \
    python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip

ENV PATH="/opt/venv/bin:$PATH"
