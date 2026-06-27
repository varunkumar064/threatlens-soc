from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class LogHandler(FileSystemEventHandler):

    def on_modified(self, event):

        if event.src_path.endswith("auth.log"):

            print("[+] New log detected:", event.src_path)

            try:

                from core.alert_processor import process_alerts

                process_alerts()

                print("[+] Alerts processed successfully")

            except Exception as e:

                print("[!] Error:", e)


def start_monitor():

    observer = Observer()

    observer.schedule(
        LogHandler(),
        path="logs",
        recursive=False
    )

    observer.start()

    print(
        "[+] Real-time monitor started"
    )

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()