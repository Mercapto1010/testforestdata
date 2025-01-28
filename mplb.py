# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [1,4,9,16,25]

# # creating aline plot
# z = plt.plot(x,y)
# print(z)

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
