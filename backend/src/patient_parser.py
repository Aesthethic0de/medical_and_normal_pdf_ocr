import re

from main_parser import MedicalDoc

class PatientParser(MedicalDoc):

    def __init__(self, text):
        MedicalDoc.__init__(self,text)
    

    def combined_dict(self):
        return {
            'patient_name' : self.patient_name(),
            'phone_number' : self.get_patient_phone_number(),
            'vaccine' : self.vaccine(),
            'medical_problem' : self.get_medical_problem()


        }
    
    def patient_name(self):

        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = " "
        if matches:
            name = self.remove_noise_from_name(matches[0])
        
        return name

    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', '').strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_patient_phone_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern,self.text, flags=re.DOTALL)
        if matches:
            return matches[0][-1]

    
    def get_medical_problem(self):
        pattern = 'List any Medical Problems .*?:(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()
    
    def vaccine(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()
    

    


    

    


    
# if __name__ == "__main__":


#     document_text = '''
#     Patient Medical Record . : :

#     Patient Information


#     Birth Date
#     Kathy Crawford May 6 1972
#     (737) 988-0851 Weight:
#     9264 Ash Dr 95
#     New York City, 10005 a
#     United States Height:
#     190
#     In Case of Emergency
#     ee oe
#     Simeone Crawford 9266 Ash Dr
#     New York City, New York, 10005
#     Home phone United States
#     (990) 375-4621
#     Work phone
#     Genera! Medical History
#     I i
#     Chicken Pox (Varicella): Measies:
#     IMMUNE IMMUNE

#     Have you had the Hepatitis B vaccination?

#     No

#     List any Medical Problems (asthma, seizures, headaches):

#     Migraine'''



            
# test_class = PatientParser(document_text)

# print(test_class.combined_dict())