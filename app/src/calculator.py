#############################
# create  a calculator class
#############################

class Calculator:
    def __init__(self):
        """Mathematics, four operators: Add, subtract, multiply, divide"""
        pass


    def add(self, num1, num2):
        return num1 + num2
                    

    def subtract(self,num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return 0
        return num1 / num2




if __name__ == "__main__":
    cal = Calculator()
    result = ""
    result = cal.add(2,2)
