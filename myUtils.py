class MyUtils():
    def __init__(self):
        pass
    def strToFloat(self, string):
        return float(string)
    def calculate_age(self, born):
        '''Calculates age from date of birth'''

        today = date.today()
        years_difference = today.year - born.year
        is_before_birthday = (today.month, today.day) <(born.month, born.day)
        elapsed_years = years_difference - int(is_before_birthday)        
    def getnum(minmax,minnum=0,maxnum=0): #function structure with internal variable names
    while True: #a loop that repeats till the correct input is given
        usr=input() #gets the supposesd number
        try: #--------------V
            usr=int(usr)#will try for if the number is an intiger
            if minmax==False or minmax==True and minnum<maxnum and minnum<=usr and maxnum>=usr: #checks if its within the paramiters defined above
                break #this takes it out of the while loop only when the number is correctly inputted 
            else:
                print("invalid input")
        except: #if it is not an intiger will give out 'invalid input' and prompt for a retry of the intiger
            print("invalid input")
    return usr; #returns the inputted number
