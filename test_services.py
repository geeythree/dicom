import unittest
from unittest.mock import patch
from io import StringIO
from pynetdicom import AE
from pynetdicom.sop_class import Verification
from services import DicomNet


class TestDicomNet(unittest.TestCase):

    def setUp(self):
        self.dicom_net = DicomNet()
        self.dicom_net.setAddress("127.0.0.1")
        self.dicom_net.setPort(11112)
        self.dicom_net.setCallerAET("TESTSCU")
        self.dicom_net.setCalledAET("TESTSCP")

    def test_create_association(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.dicom_net.create_association()
            self.assertIn("Association created successfully", fake_output.getvalue().strip())

    def test_cecho(self):
        self.dicom_net.create_association()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.dicom_net.cecho()
            self.assertIn("C-ECHO request status: PASSED \nStatus code: 0x000", fake_output.getvalue().strip())

    def test_cfind(self):
        self.dicom_net.create_association()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.dicom_net.cfind()
            self.assertIn("This method has not been implemented yet", fake_output.getvalue().strip())
    
    def test_release_association(self):
        self.dicom_net.create_association()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.dicom_net.release_association()
            self.assertIn("Association released successfully", fake_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
