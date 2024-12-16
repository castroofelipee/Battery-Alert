import psutil  # type: ignore
import time
import logging
from plyer import notification

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def check_battery(low_threshold, high_threshold, interval):
    alerted_low = False
    alerted_high = False

    while True:
        battery = psutil.sensors_battery()
        if not battery:
            logging.error("No battery detected or sensors not available.")
            break

        percent = battery.percent
        charging = battery.power_plugged

        if percent <= low_threshold and not charging and not alerted_low:
            notification.notify(
                title="⚠️ Low Battery",
                message=f"Battery at {percent}%. Connect to charger!",
                timeout=10
            )
            logging.info("Low battery notification sent.")
            alerted_low = True
            alerted_high = False

        elif percent >= high_threshold and charging and not alerted_high:
            notification.notify(
                title="⚡ Battery Charged",
                message=f"Battery at {percent}%. Disconnect from charger!",
                timeout=10
            )
            logging.info("Charged notification sent.")
            alerted_high = True
            alerted_low = False

        if percent > low_threshold and not charging:
            alerted_low = False
        if percent < high_threshold and charging:
            alerted_high = False

        time.sleep(interval)
