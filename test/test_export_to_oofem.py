__copyright__ = "Copyright (C) 2013 Kristoffer Carlsson"

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import unittest
import os

from phon.io.read.read_from_neper_inp import read_from_neper_inp
from phon.io.write.export_to_oofem import export_to_oofem
from phon.mesh_tools.create_cohesive_elements import create_cohesive_elements


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Test(unittest.TestCase):
    """Unit tests for export_to_oofem."""

    def setUp(self):
        self.mesh = read_from_neper_inp(os.path.join(__location__, "n10-id1.inp"))

    def test_export_to_oofem(self):
        """Test Phons exporter for oofem files."""
        export_to_oofem("test_file.in", self.mesh, write_2d_elements=True)
        export_to_oofem("test_file.in", self.mesh, write_2d_elements=False)

        create_cohesive_elements(self.mesh)
        export_to_oofem("test_file.in", self.mesh, write_2d_elements=True)
        export_to_oofem("test_file.in", self.mesh, write_2d_elements=False)

    def tearDown(self):
        if os.path.isfile("test_file.in"):
            os.remove("test_file.in")


if __name__ == "__main__":
    unittest.main()
