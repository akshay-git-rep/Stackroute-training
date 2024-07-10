from abc import ABC, abstractmethod        #importing abstract

class InsurancePolicy:                  #Defining InsurancePolicy for base variable
   
    def __init__(self, policy_holder_name, policy_type, coverage_amount):
        self.policy_holder_name = policy_holder_name
        self.policy_type = policy_type
        self.coverage_amount = coverage_amount
 
    @abstractmethod
    def calculate_premium(self):
        raise NotImplementedError("Method not implementes as premium calculation varies for different policy types.")
 
 
class CarInsurance(InsurancePolicy):
    def __init__(self, policy_holder_name, policy_type, coverage_amount, year_of_manufacture, driving_record ):
        super().__init__(policy_holder_name, policy_type, coverage_amount)
        self.year_of_manufacture = year_of_manufacture
        self.driving_record  = driving_record
 
    def calculate_premium(self):                #Calculating premium amount
        base_premium = self.coverage_amount * 0.1
        if int(self.year_of_manufacture) < 2010:
                age_factor = 0.1 
        else:
            age_factor = 0
        if self.driving_record != "CLean":
            driving_record_factor = 0.2
        else:
            driving_record_factor = 0
        final_premium_amount = base_premium * (1 + age_factor + driving_record_factor)
        return final_premium_amount
 
def calculate_and_write_premiums(policies, filename):
    try:
        with open(filename, 'w') as file:
            file.write("Policy Holder,Policy Type,Premium\n")
            for p in policies:
                file.write(f"{p.policy_holder_name},{p.policy_type},${p.calculate_premium()}\n")
    except FileNotFoundError:
        print("File {filname} not found")
    except NotImplementedError as e:
        print(e)
    except TypeError:
        print("Invalid input entered for coverage amount")
    except Exception:
        print("Some error occured")
       
# Input data

def main():
    policies = [
    CarInsurance("Akshay", "Car", 80000, "2022", "Clean"),
    CarInsurance("Amruth", "Car", 70000, "2015", "Clean"),
    CarInsurance("Akshay Pawar", "Car", 65000, "2010", "Accidents"),
    CarInsurance("Pawar", "Car", 50000, "2018", "Accidents") ]
 
    calculate_and_write_premiums(policies, "insurance_premiums_output.csv")
 
if __name__ == "__main__":
    main()