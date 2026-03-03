import subprocess
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

RESOLVER_FILE = "resolvers.txt"
SLIPSTREAM_BIN = "./slipstream-client-linux-amd64"

# Default values
DEFAULT_TIMEOUT = 5
DEFAULT_THREADS = 10


def ping_resolver(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2", ip],
            capture_output=True, text=True
        )
        for line in result.stdout.splitlines():
            if "time=" in line:
                time_ms = line.split("time=")[1].split()[0]
                return time_ms
    except:
        pass
    return None


def test_resolver(resolver_ip, target_domain, timeout):
    port = random.randint(10025, 65535)
    cmd = [
        SLIPSTREAM_BIN,
        "--resolver", f"{resolver_ip}:53",
        "--domain", target_domain,
        "--tcp-listen-host", "0.0.0.0",
        "-l", str(port),
        "-t", str(timeout)
    ]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    status = "NO"
    start_time = time.time()

    while True:
        line = proc.stdout.readline()
        if not line:
            if proc.poll() is not None:
                break
            continue

        line = line.strip()

        if "WARN" in line or "Connection closed" in line:
            continue

        if "Connection ready" in line:
            status = "OK"
            break

        if "ERROR picoquic_prepare_packet_ex failed" in line:
            status = "NO"
            break

        if time.time() - start_time > timeout:
            break

    proc.kill()
    proc.wait()

    ping_time = ping_resolver(resolver_ip) if status == "OK" else None

    if ping_time:
        print(f"{resolver_ip}: {status} ({ping_time} ms)")
    else:
        print(f"{resolver_ip}: {status}")

    return {"resolver": resolver_ip, "status": status, "ping": ping_time}


def main():
    print("\n✅ Valid DNS-Scanner(SlipStream/DNStt) | By : https://github.com/realrevenant\n")

    # ===== User Inputs =====
    target_domain = input("Enter Target Domain(SlipStream NameServer | s.example.com): ").strip()
    while not target_domain:
        target_domain = input("Target Domain cannot be empty. Enter again: ").strip()

    timeout_input = input(f"Enter SLIPSTREAM_TIMEOUT (default {DEFAULT_TIMEOUT}): ").strip()
    timeout = int(timeout_input) if timeout_input else DEFAULT_TIMEOUT

    threads_input = input(f"Enter MAX_THREADS (default {DEFAULT_THREADS}): ").strip()
    max_threads = int(threads_input) if threads_input else DEFAULT_THREADS
    # ========================

    with open(RESOLVER_FILE) as f:
        resolvers = [line.strip() for line in f if line.strip()]

    results = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [
            executor.submit(test_resolver, r, target_domain, timeout)
            for r in resolvers
        ]

        for future in as_completed(futures):
            results.append(future.result())

    valid = [r for r in results if r["status"] == "OK"]

    if valid:
        print("\nBy : https://github.com/realrevenant | ✅ Valid resolvers:")
        for v in valid:
            if v["ping"]:
                print(f"{v['resolver']} ({v['ping']} ms)")
            else:
                print(v["resolver"])
    else:
        print("\nBy : https://github.com/realrevenant | ❌ No valid resolver found")


if __name__ == "__main__":
    main()