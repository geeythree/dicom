from services import DicomNet


dn = DicomNet()

dn.setAddress('127.0.0.1')
dn.setPort(4242)
dn.setCallerAET('MYPACS')

dn.create_association()

dn.cecho()

dn.release_association()