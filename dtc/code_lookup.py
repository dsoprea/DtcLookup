import re

from os import listdir

from dtc.config.db.codes import DTC_FILES_PATH

_codes = None

def initialize():
    global _codes

    if _codes is not None:
        return

    files = listdir(DTC_FILES_PATH)
    name_matcher = re.compile('^codes-(.+)\..+$')
    code_matcher = re.compile('^([^ \t]+)\t(.+?)\r?\n?$')
    codes = {}
    
    for filename in files:
        filepath = ('%s/%s' % (DTC_FILES_PATH, filename))
        title = name_matcher.match(filename).group(1)

        print("Reading codes from [%s]." % (title))

        with file(filepath) as f:
            i = 0
            skipped = 0
            for row in f:
                result = code_matcher.match(row)

                if result is None:
                    skipped += 1
                    continue

                (code, description) = result.groups()
                code = code.upper()
                value = (title, description)

                try:
                    codes[code].append(value)
                except KeyError:
                    codes[code] = [value]

                i += 1

        print("\t(%d) codes loaded." % (i))
        print("\t(%d) rows skipped." % (skipped))

    _codes = codes

def lookup(code):
    return _codes[code.upper()]

