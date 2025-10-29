#!/usr/bin/env python3

import logging

#logger with diff levels

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )
logging.debug("DEBUG level")
logging.warning("WARNING level")
logging.error("ERROR level")
logging.critical("critical level")
