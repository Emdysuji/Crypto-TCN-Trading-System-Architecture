import time
import threading
import requests

BINANCE_TIME_URL = "https://fapi.binance.com/fapi/v1/time"

class BinanceTimeSync:
    def __init__(self, sync_interval=300):
        self.sync_interval = sync_interval
        self.offset_ns = 0
        self._lock = threading.Lock()
        self._sync_once()
        self._start_background_sync()

    def _sync_once(self):
        try:
            t0 = time.time_ns()
            server_ms = requests.get(
                BINANCE_TIME_URL, timeout=1
            ).json()["serverTime"]
            t1 = time.time_ns()

            server_ns = server_ms * 1_000_000
            local_ns = (t0 + t1) // 2
            offset = server_ns - local_ns

            with self._lock:
                self.offset_ns = offset

        except Exception:
            # keep last good offset
            pass

    def _start_background_sync(self):
        def loop():
            while True:
                self._sync_once()
                time.sleep(self.sync_interval)

        threading.Thread(
            target=loop, daemon=True
        ).start()

    def now_ns(self):
        with self._lock:
            return time.time_ns() + self.offset_ns

    def now_ms(self):
        return self.now_ns() // 1_000_000
