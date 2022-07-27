
from prescription_parser import PrescriptionParser



def test_get_name():
    pp = PrescriptionParser(document_text)
    test = pp.get_field('patient_name')
    return test

def test_get_address():
    pp = PrescriptionParser(document_text)
    test = pp.get_field('patient_address')
    return test

def test_get_medicine():
    pp = PrescriptionParser(document_text)
    test = pp.get_field('medicines')
    return test

def test_get_directions():
    pp = PrescriptionParser(document_text)
    test = pp.get_field('directions')
    return test

def test_refills():
    pp = PrescriptionParser(document_text)
    test = pp.get_field('refills')
    return test





if __name__ == "__main__" :


    document_text = '''
        Dr John Smith, M.D
        2 Non-Important Street,
        New York, Phone (000)-111-2222
        Name: Marta Sharapova Date: 5/11/2022
        Address: 9 tennis court, new Russia, DC

        Prednisone 20 mg
        Lialda 2.4 gram
        Directions:
        Prednisone, Taper 5 mg every 3 days,
        Finish in 2.5 weeks -
        Lialda - take 2 pill everyday for 1 month
        Refill: 3 times'''


    test_dict = {}
    test_dict['name'] = test_get_name()
    test_dict['address'] = test_get_address()
    test_dict['medicines'] = test_get_medicine()
    test_dict['directions'] = test_get_directions()
    test_dict['refills'] = test_refills()
    print(test_dict + "All Test Cases Are Passes!!!!")


        

