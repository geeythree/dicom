from services import DicomNet


dn = DicomNet()

dn.setAddress('127.0.0.1')
dn.setPort(4242)
dn.setCallerAET('MYPACS')

dn.setAssociation()

dn.cecho()

dn.releaseAssociation()