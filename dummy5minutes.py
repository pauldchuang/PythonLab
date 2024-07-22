import time
import logging
# Configure logging
logging.basicConfig(filename='dummy_script.log', level=logging.INFO, format='%(asctime)s - %(message)s')

logging.info("Script started. It will run for 5 minutes and logging.info a message every 1 seconds.")

# Total duration in seconds
total_duration = 300
# Interval in seconds
interval = 1
# Calculate the number of iterations needed
iterations = total_duration // interval

for i in range(iterations):
    logging.info(f"Elapsed time: {i * interval} seconds")
    time.sleep(interval)

logging.info("Script finished.")