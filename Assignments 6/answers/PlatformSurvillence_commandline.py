# python3 processsurvillence.py <time_interval> <folder_name>
import psutil
import sys
import os

def main():
    border = "-"*50
    print(border)
    print("---Marvellous Platform Survillence System----")
    print(border)

    # --h and --u handling
    if(len(sys.argv) == 2):
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as:")
            print(f"python3 {sys.argv[0]} time_interval folder_name")
            print("time_interval: time in minutes for periodic execution")
            print("folder_name: Name of folder for the log file creation.")
        elif sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is use to perform:\n")
            print("1.It fetch the information of running processes.")
            print("2.It fetch the information about the primary stprage as RAM.")
            print("3.It fetch the information about the Secondary storage as HDD.")
            print("4.It fetch the information about the Microprocessor.")
            print("5.It will maintian the records")
            print("6. It sends log file to the mail periodically.")


        else:
            print("Unable to proceed, argument are not matching. Please use --u or --h for more details.")
    # actual project code
    elif len(sys.argv) == 3:
        pass
    else:
        print("Invalid number of arguments.")
        print("Unable to proceed argument are not matching. Please use --u or --h for more details.")





    print(border)
    print("Thank you for using our Automation System")
    print(border)
    print("---Marvellous Platform Survillence System----")
    print(border)


if __name__ == "__main__":
    main()