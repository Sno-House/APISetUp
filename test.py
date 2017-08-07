import random
import os

import cassiopeia as cass
import sys

summoner = cass.get_summoner(name="BubblyBryan")
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region))