#!/usr/bin/env python3
#
# weeman.py - HTTP server for phishing
#
#  Weeman is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  Weeman is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2015 Hypsurus <hypsurus@mail.ru>
#

import sys
import optparse
from core.misc import printt
from core.config import quiet_mode

def tests_pyver():
    if "3" in sys.version[:3]:
        pass # All good
    elif "2" in sys.version[:3]:
        printt(1,"This is a Python 3 version for weeman.")
    else:
        printt(1, "Your Python version is very old ..")

def tests_platform():
    if "linux" in sys.platform:
        #printt(3, "Running Weeman on linux ... (All good)")
        pass
    elif "darwin" in sys.platform:
        #printt(3, "Running Weeman on \'Mac\' (All good)")
        pass
    elif "win" in sys.platform:
        printt(3, "Running Weeman on \'Windows\' (Not tested)")
    else:
        printt(3, "If \'Weeman\' runs sucsessfuly on your platform %s\nPlease let me (@Hypsurus) know!" %sys.platform)

def main():
    tests_pyver()
    tests_platform()
    try:
        from bs4 import BeautifulSoup as bs
    except ImportError:
        printt(1, "Please install Python 3 beautifulsoup 4 to continue ...")

    parser = optparse.OptionParser()
    parser.add_option("-q", "--quiet", 
            dest="quiet_mode_opt", action="store_true", 
            default=False, help="Runs without displaying the banner.")

    options,r = parser.parse_args()
    mode = options.quiet_mode_opt

    from core.shell import shell
    shell(mode)

if __name__ == '__main__':
    main()
