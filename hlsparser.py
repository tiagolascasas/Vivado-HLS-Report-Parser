#!/usr/bin/python

import sys
import csv
import xml.etree.ElementTree as ET
from os import path

usage = '''
Usage:
\tpython hlsparse.py <path to report> <name of input code> <optimizations>
'''

def main():
    if len(sys.argv) != 4:
        print(usage)
        return 1

    report = {}

    try:
        root = ET.parse(sys.argv[1]).getroot()
    except OSError:
        print("Unable to read specified report file \"" + sys.argv[1] + "\", aborting...")
        return 1

    print(root)

    user_assign = root.find('UserAssignments')
    perf_estim = root.find('PerformanceEstimates')
    area_estim = root.find('AreaEstimates/Resources')

    report['input'] = sys.argv[2]
    report['optimizations'] = sys.argv[3]

    report['part'] = user_assign.find('Part').text
    report['target_clock'] = user_assign.find('TargetClockPeriod').text

    report['estim_clock'] = perf_estim.find('SummaryOfTimingAnalysis/EstimatedClockPeriod').text
    report['lat_worst'] = perf_estim.find('SummaryOfOverallLatency/Worst-caseLatency').text
    report['lat_avg'] = perf_estim.find('SummaryOfOverallLatency/Average-caseLatency').text
    report['lat_best'] = perf_estim.find('SummaryOfOverallLatency/Best-caseLatency').text

    report['FF'] = area_estim.find('FF').text
    report['LUT'] = area_estim.find('LUT').text
    report['BRAM'] = area_estim.find('BRAM_18K').text
    report['DSP'] = area_estim.find('DSP48E').text

    fieldnames = report.keys()
    if path.exists('reports.csv'):
        print("reports.csv found in current directory, adding...")
        with open('reports.csv', 'a', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writerow(report)
    else:
        with open('reports.csv', 'w', newline='') as output:
            print("reports.csv not found, creating...")
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(report)
    print("Report for \"" + report['input'] + "\" successfully added to reports.csv") 

if __name__ == "__main__":
    main()