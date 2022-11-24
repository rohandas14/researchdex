from goblet import Goblet

discovery = Goblet()

DISCOVERY_RUN_SCHEDULE = "* 23 * * *"

@discovery.schedule(DISCOVERY_RUN_SCHEDULE)
def run_discovery():
    discovery.log.info("running discovery service")
    return 'discovery run completed!'