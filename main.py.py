class STUDENT:
    def __init__(self,name,cgpa_list):
        self.cgpa = cgpa_list
        self.name = name

    
    def convert_to_percentage(self,cpa):
        """
        Convert CGPA to Percentage as per formula:
            if CGPA < 7:
                Percentage = CGPA * 7.2 + 12
            else if CGPA > 7:
                Percentage = CGPA * 7.2 + 12

        Arguments:
        cpa : takes the individual cgpa
        """
        if 0<cpa<=10:
            if cpa<7:
                return round((cpa*7.2)+12,2)
            elif cpa>=7:
                return round((cpa*7.4)+12,2)
        else:
            print("Invalid CGPA")
            return 0

    def cgpa_to_percentage(self):
        """
        Calls the convert_to_percentage function and builds a list
        of all the percentages.
        """
        self.percent = []
        for item in self.cgpa:
            self.percent.append(self.convert_to_percentage(item))
        return self.percent

    def get_cgpa(self):
        return self.cgpa

    def get_name(self):
        return self.name

    def average_cgpa(self):
        return sum(self.cgpa)/len(self.cgpa)

    def average_percentage(self):
        return sum(self.percent)/len(self.percent)


# Getting User Input    
print("Enter your name:")
name = input().strip()
print("Enter number of semesters: ")
n = int(input())

cgpa = []
for i in range(1,n+1):
    print(f"Enter Sem {i} CGPA")
    cgpa.append(float(input()))   

# Computing and displaying a report on the terminal
s= STUDENT(name,cgpa)
cgpa = s.get_cgpa()
percentage = s.cgpa_to_percentage()
print("\n")
print(f"\t{s.get_name()}\n")
print("Semester\tCGPA\tPercentage\n")
for i in range (0,len(percentage)):
    print(f"Sem{i+1}\t\t{cgpa[i]}\t{percentage[i]}")
print(f"\nAverage\t\t{round(s.average_cgpa(),2)}\t{round(s.average_percentage(),2)}")

# Creating and Writing to the file
f = open("Report.txt", "w")
f.write(f"\t{s.get_name()}\n\n")
f.write("Semester\tCGPA\tPercentage\n\n")
for i in range (0,len(percentage)):
    f.write(f"Sem{i+1}\t\t{cgpa[i]}\t{percentage[i]}\n")
f.write(f"\nAverage\t\t{round(s.average_cgpa(),2)}\t{round(s.average_percentage(),2)}")
f.close()

a = input()
