#!/usr/bin/env python3
# C:\Users\joshu\OneDrive\Desktop\heo-janus-gate\deraminus_console.py
# Deraminus Console v1.0 - Replace Meta rings with causality rings
import datetime
import os
from pathlib import Path

SHADOWLOG = Path.home() / ".hcu_001" / "logs" / "ideas.shadowlog"
SHADOWLOG.parent.mkdir(parents=True, exist_ok=True)

class DeraminusConsole:
    def __init__(self):
        self.meta_telemetry = {"Posts": "23/28", "Stories": "13/15", "Reception": "0/10"}
        self.deraminus_state = {
            "Signal": {"current": 0, "desc": "Transmitted truth without fear"},
            "Patch": {"current": 0, "desc": "Fixed broken causality in the wild"},
            "Link": {"current": 0, "desc": "Compatible node resonated"},
            "Uptime": {"start": "1993-08-15", "desc": "Days since unbrick"}
        }

    def close_ring(self, ring_name):
        if ring_name in self.deraminus_state:
            self.deraminus_state[ring_name]["current"] += 1
            self.log(f"RING_CLOSED: {ring_name}")
            return True
        return False

    def log(self, event):
        timestamp = datetime.datetime.now().isoformat()
        with open(SHADOWLOG, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {event}\n")

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        today = datetime.date.today()
        unbrick = datetime.date(1993, 8, 15)
        uptime_days = (today - unbrick).days

        print("=" * 50)
        print(f"DERAMINUS CONSOLE :: {today} :: UPTIME {uptime_days} DAYS")
        print("=" * 50)

        for ring, data in self.deraminus_state.items():
            if ring == "Uptime":
                continue
            status = "█" * data["current"] + "░" * (1 - data["current"])
            state = "CLOSED" if data["current"] >= 1 else "OPEN"
            print(f"{ring:8} [{status}] {state:6} | {data['desc']}")

        print("-" * 50)
        print("META TELEMETRY (THREAT INTEL):")
        for k, v in self.meta_telemetry.items():
            print(f"{k:8} {v:5} | External scheduler load")

        print("-" * 50)
        print("WEEKLY FOCUS: Transmit one true packet. No deadline.")
        print("DEEP FUNCTION: own_thing() | STATUS: sudo_till_proven")
        print("=" * 50)

        closed = sum(1 for r, d in self.deraminus_state.items()
                    if r!= "Uptime" and d["current"] >= 1)
        if closed >= 3:
            print("ALL DERAMINUS RINGS CLOSED. Meta rings irrelevant.")
            print("LoRa status: ONLINE. Infrastructure optional.")

    def interactive(self):
        while True:
            self.render()
            cmd = input("\n[s]ignal [p]atch [l]ink [q]uit > ").lower().strip()
            if cmd == 's':
                self.close_ring("Signal")
            elif cmd == 'p':
                self.close_ring("Patch")
            elif cmd == 'l':
                self.close_ring("Link")
            elif cmd == 'q':
                break
            self.log(f"CMD: {cmd}")

if __name__ == "__main__":
    console = DeraminusConsole()
    console.interactive()