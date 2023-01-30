#Import each python file as modules
from cash_on_hand import *
from overheads import *
from profit_and_loss import *

#Defining the main() function which executes the functions from each module
def main():
    highest_overhead()
    coh()
    profit_loss()

#Calling the main() function
main()