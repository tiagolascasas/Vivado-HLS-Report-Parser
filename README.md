# Vivado-HLS-Report-Parser

## Fair warning: this parser has been validated using Vivado HLS 2019.x. After this version, Vivado HLS was rebranded as Vitis HLS, and the format of the synthesis report was changed. This parser has not yet been updated to accomodate these changes, and will most likely not work.

Parser for Vivado HLS synthesis reports. It collects features and adds them to a CSV file. Current features are: part number, clock speed (target and estimated), latency (average, worst and best), and hardware resources (FFs, LUTs, BRAMs and DSPs). The parser may be expanded to extract more features as needed.

Requires python 3.x to run. No other dependencies are used. Usage is as follows:

`python hlsparse.py <path to report> <name of input code> <optimizations>`

To test the parser, run:

`python test.py`

An executable that does not require python is also provided for Windows. See [releases](https://github.com/tiagolascasas/Vivado-HLS-Report-Parser/releases/tag/1.0).
