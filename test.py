import unittest
import os
import hlsparser
import io

class TestParser(unittest.TestCase):

    def test_parser(self):
        try:
            os.remove("reports.csv")
        except OSError:
            pass
        res = hlsparser.main(["", "examples/array_addition_csynth.xml", "array_addition", "No directives"])
        self.assertEqual(res, 0)
        res = hlsparser.main(["", "examples/array_addition_csynth_optim.xml", "array_addition", "Pipeline factor 2 + full unroll"])
        self.assertEqual(res, 0)

    def test_csv_file(self):
        self.assertListEqual(
            list(io.open("reports.csv")),
            list(io.open("examples/reports_test.csv")))


if __name__ == '__main__':
    unittest.main()