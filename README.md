# Vivado-HLS-Report-Parser

Parser for Vivado HLS synthesis reports. It collects features and adds them to a CSV file. Current features are: part number, clock speed (target and estimated), latency (average, worst and best), and hardware resources (FFs, LUTs, BRAMs and DSPs). The parser may be expanded to extract more features as needed.

Requires python 3.x to run. No other dependencies are used. Usage is as follows:

`python hlsparse.py <path to report> <name of input code> <optimizations>`

To test the parser, run:

`python test.py`

An executable that does not require python is also provided for Windows.  