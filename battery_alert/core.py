import psutil  # type: ignore
import time
from plyer import notification
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Battery monitoring")
    parser.add_argument("--low", type=int, default=20, help="Low battery level (%)")
    parser.add_argument("--high", type=int, default=82, help="High battery level (%)")
    return parser.parse_args()

def check_battery(low_threshold, high_threshold):
    alerted_low = False
    alerted_high = False

    while True:
        battery = psutil.sensors_battery()
        if not battery:
            print("No battery detected or sensors not available.")
            break

        percent = battery.percent
        charging = battery.power_plugged

        if percent <= low_threshold and not charging and not alerted_low:
            notification.notify(
                title="⚠️ Low Battery",
                message=f"Battery at {percent}%. Connect to charger!",
                timeout=10
            )
            alerted_low = True
            alerted_high = False

        elif percent >= high_threshold and charging and not alerted_high:
            notification.notify(
                title="⚡ Battery Charged",
                message=f"Battery at {percent}%. Disconnect from charger!",
                timeout=10
            )
            alerted_high = True
            alerted_low = False


        if percent > low_threshold and not charging:
            alerted_low = False
        if percent < high_threshold and charging:
            alerted_high = False

        time.sleep(60)  

if __name__ == "__main__":
    args = parse_args()
    check_battery(args.low, args.high)
