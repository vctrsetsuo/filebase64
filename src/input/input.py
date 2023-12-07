import sys

from encode import encode
from split  import split

output_name = encode(sys.argv[1])

split(output_name, 'splitfolder_' + output_name, 52428800)