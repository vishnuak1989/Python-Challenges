#Function to convert any number under 1000 to its words
def numbertowords(number):
    numbers = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve"
    ,13:"thirteen",14:"forteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen",20:"twenty",30:"thirty",40:"forty",
    50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred"}
    digits=[]
    n = number
    while n>0 :
        digits.insert(0, n%10)
        n = int(n/10)
    if number>100 and number<1000:
        if digits[1]>1:
            print(numbers[digits[0]]+" hundred "+numbers[digits[1]*10]+" "+numbers[digits[2]])
        else:
            print(numbers[digits[0]]+" hundred "+numbers[digits[1]*10+digits[2]])
    elif number<100 and number >19:
        print(numbers[digits[0]*10]+" "+numbers[digits[1]])
    elif number<=19:
        print(numbers[number])
    else:
        print("Number should be less than 1000 and greater than 0")

# TestCases
# numbertowords(23)
# numbertowords(111)
# numbertowords(212)
# numbertowords(313)
# numbertowords(200)
# numbertowords(300)
# numbertowords(123)
# numbertowords(999)
# numbertowords(19)
# numbertowords(20)
# numbertowords(21)
# numbertowords(65)
# numbertowords(33)
# numbertowords(23)
# numbertowords(15)
# numbertowords(1000)

number=int(input("Enter a number under 1000"))
numbertowords(number)