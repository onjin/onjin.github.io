#!/usr/bin/env python
import subprocess
import signal
import os
from pathlib import Path
from threading import Thread
from typing import Final, override
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent


class MkDocsBuildHandler(FileSystemEventHandler):
    def __init__(self, config: str, build_dir: str):
        self.config: Final = config
        self.build_dir: Final = build_dir

    @override
    def on_any_event(self, event: FileSystemEvent):
        if event.event_type in ["opened", "closed_no_write"] or event.is_directory:
            return
        print(f"[{event.event_type}]({event.src_path})", end=" : ")
        if event.event_type in {"closed"}:
            print("handled")
            self.build_site()
        else:
            print("skipped")

    def build_site(self):
        print(f"Building site for {self.config}...")
        _ = subprocess.run(["mkdocs", "build", "-f", self.config], check=True)


def run_http_server(directory: str, port: int):
    os.chdir(directory)
    _ = subprocess.run(["python", "-m", "http.server", str(port)])


def watch_and_build(config_path: str | Path, watch_dir: str):
    event_handler = MkDocsBuildHandler(config=str(config_path), build_dir="./site")
    observer = Observer()
    _ = observer.schedule(event_handler, watch_dir, recursive=True)
    observer.start()
    return observer


def main():
    # Determine paths
    current_dir = Path(__file__).parent.resolve()
    config_pl = current_dir / "mkdocs.pl.yaml"
    config_en = current_dir / "mkdocs.en.yaml"
    docs_pl = current_dir / "src/pl"
    docs_en = current_dir / "src/en"
    site_dir = current_dir / "docs"
    overrides_dir = current_dir / "overrides"
    port = 8000

    # Start watchers
    observers = [
        watch_and_build(config_path=config_pl, watch_dir=str(docs_pl)),
        watch_and_build(config_path=config_en, watch_dir=str(docs_en)),
        watch_and_build(config_path=config_pl, watch_dir=str(overrides_dir)),
        watch_and_build(config_path=config_en, watch_dir=str(overrides_dir)),
    ]

    # Build sites initially
    _ = subprocess.run(["mkdocs", "build", "-f", config_pl], check=True)
    _ = subprocess.run(["mkdocs", "build", "-f", config_en], check=True)

    # Start HTTP server in a thread
    server_thread = Thread(target=run_http_server, args=(site_dir, port), daemon=True)
    server_thread.start()

    print(f"Serving at http://localhost:{port}")

    # Wait for CTRL+C to clean up
    try:
        signal.pause()
    except KeyboardInterrupt:
        print("Shutting down...")

        # Stop watchers
        for observer in observers:
            observer.stop()
            observer.join()

        # Stop HTTP server
        print("Stopping HTTP server...")
        server_thread.join()


if __name__ == "__main__":
    main()
