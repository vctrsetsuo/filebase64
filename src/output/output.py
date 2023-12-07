import sys

from join   import join
from decode import decode

name = sys.argv[1]
outputjoin_name = 'outputjoin_' + name.split('_')[2]

join(name, outputjoin_name, 52428800)
decode(outputjoin_name)