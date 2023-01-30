#Import data from different modules
from cash_on_hand import *
from overheads import *
from profit_and_loss import *

#Defining the main() function which calls all the functions from the different modules
def main():
    highest_overhead()
    coh()
    profit_loss()

#Calling the main() function
main()
