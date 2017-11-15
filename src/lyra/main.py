"""
Lyra Static Program Analyzer
============================
"""

import argparse

import sys

from lyra.engine.liveness.liveness_analysis import StrongLivenessAnalysis
from lyra.engine.numerical.interval_analysis import ForwardIntervalAnalysis
from lyra.engine.usage.usage_analysis import UsageAnalysis


def main():
    """Static analyzer entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'python_file',
        help='Python file to analyze')
    parser.add_argument(
        '--analysis',
        help='analysis to be used (interval, liveness, or usage)',
        default='usageOLD')
    args = parser.parse_args()

    if args.analysis == 'intervals':
        ForwardIntervalAnalysis().main(args.python_file)
    if args.analysis == 'liveness':
        StrongLivenessAnalysis().main(args.python_file)
    if args.analysis == 'usage':
        UsageAnalysis().main(args.python_file)


if __name__ == '__main__':
    main()
