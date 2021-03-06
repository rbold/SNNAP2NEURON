# This file is part of SNNAP2NEURON.
#
# Copyright (C) 2019 Jayalath A M M Abeywardhana, Jeffrey Gill, Reid Bolding,
# Peter Thomas
#
# SNNAP2NEURON is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# SNNAP2NEURON is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SNNAP2NEURON.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import print_function

import sys
import re
import os
import argparse

from simulation import Simulation as sim
from nrnModelPoint import NRNModelPoint
from nrnModelDist import NRNModelDist

def parse2Hoc(filename, cond):
    # create simulation object.
    snnapSim = sim(filename)

    # write model in NEURON
    if cond == 'p':
        nrnModel = NRNModelPoint(snnapSim)
    elif cond == 'd':
        nrnModel = NRNModelDist(snnapSim)
    return snnapSim

def printSim(sim):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path to SNNAP .smu file")
    parser.add_argument("-c", "--cond", choices=['p', 'd'], default='p',
                        help="representation of conductances (point 'p', or distributed 'd')")
    args = parser.parse_args()
    filePath = args.input

    cond = ''
    if args.cond == 'p':
        cond = 'p'
        print("Conductances will be represented as point mechanisms")
    elif args.cond == 'd':
        cond = 'd'
        print("Conductances will be represented as distributed mechanisms")
    else:
        print("choices for --cond are either 'p' or 'd'")

    # if len(sys.argv) > 1:
    #     filePath = sys.argv[1]
    # else:
    #     print("usage: parseSNNAP <simulationFile>")
    #     filePath = "model/hhNetwork.smu"

    splitedFilePath = filePath.split(os.sep)

    simFilePath = splitedFilePath[:-1]
    simFileName = splitedFilePath[len(splitedFilePath)-1]

    currSim = parse2Hoc(filePath, cond)
