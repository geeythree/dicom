from pynetdicom import AE
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind, Verification
from pydicom.dataset import Dataset


class DicomNet:
    def __init__(self) -> None:
        self.address = str()
        self.port = int()
        self.callerAET = str('MYPACS')
        self.calledAET = str()

    def setAddress(self, remote_host):
        self.address = remote_host

    def setPort(self, remote_port):
        self.port = remote_port

    def setCallerAET(self, callerAET):
        if callerAET != '':
            # cannot have empty string as AE Ttile
            self.callerAET = callerAET

    def setCalledAET(self, calledAET):
        if calledAET != '':
            # cannot have empty string as AE Ttile
            self.calledAET = calledAET

    def setAssociation(self) -> None:
        if not self.address == '' and not self.port == '':
            assoc_entity = AE()
            assoc_entity.add_requested_context(Verification)
        else:
            print("Address or Port is empty")
        try:
            self.assoc = assoc_entity.associate(addr=self.address, 
                                                port=self.port, 
                                                ae_title=self.callerAET)
        except Exception as e:
            print(f"Creating Association: {e}")
        print("Association created successfully")

    def releaseAssociation(self) -> None:
        try:
            self.assoc.release()        
        except Exception as e:
            print(e)
            print("Association not released")
            exit()
        print("Association released successfully")


    def cecho(self):
        try:
            if self.assoc.is_established:
                status = self.assoc.send_c_echo()
                if status:
                    # If the verification request succeeded this will be 0x0000
                    print('C-ECHO request status: PASSED \nStatus code: 0x{0:04x}'.format(status.Status))
                    return 1
                else:
                    print('Connection timed out, was aborted or received invalid response')
            else:
                print("No association has been established")
        except:
            print("Association not set, please create an association first")
        return 0

    def writeQuery(self, patient_name, patient_id, study_instance_uid):
        self.patientName = patient_name
        self.patientID = patient_id
        self.studyInstanceUID = study_instance_uid

    def cfind(self):
        self.assoc.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

        ds=Dataset()
        if self.patientName != '':
            ds.PatientName = self.patientName
        


