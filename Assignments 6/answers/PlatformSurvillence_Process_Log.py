import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name", "username", "status"])
        info["cpu_prcent"] = proc.cpu_percent()
        info["memory_percent"] = proc.memory_percent()
        print("-------------------------------------")
        print(info)
        print("-------------------------------------")


def PlatformSurvillence(folderName):
    border = "-"*50
    if os.path.exists(folderName) == True:
        if os.path.isdir(folderName) == False:
            print("Unable to proceed as folder name is existing but its not a directory.")
            return
    else:
        os.mkdir(folderName)
        print("Directory for the log file gets created successfully.")

    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    fileName = os.path.join(folderName, "Marvellous_%s.log" %timestamp)
    fobj = open(fileName, "w")
    print(f"Log file successfully created name as {fileName}")

    fobj.write(border+"\n")
    fobj.write("---Marvellous Platform Survillence System----\n")
    fobj.write("Log file gets created at "+str(timestamp)+"\n")
    fobj.write(border+"\n")
    fobj.write("----------------------- System Report --------------------\n")

    # CPU information
    fobj.write("No of CPU Cores: "+str(psutil.cpu_count())+"\n")
    fobj.write("CPU Usage: "+str(psutil.cpu_percent())+"%\n")
    fobj.write(border+"\n")
    
    # RAM Information
    memory = psutil.virtual_memory()
    fobj.write("RAM Usage: "+str(memory.percent)+"%\n")
    fobj.write("Toral RAM available: "+str(memory.total)+" bytes\n")
    fobj.write(border+"\n")

    # Network Usage
    netObj = psutil.net_io_counters()
    fobj.write("Network Usage Report:\n")
    fobj.write("Sent: %.2f MB\n" % float(netObj.bytes_sent/(1024 * 1024)))
    fobj.write("Recieved: %.2f MB\n" % float(netObj.bytes_recv/(1024 * 1024)))
    fobj.write(border+"\n")

    
    fobj.write("\n\n\n\n\n\n\n\n")
    fobj.write(border+"\n")
    fobj.write("----End of Log file-----\n")
    fobj.write(border+"\n")
    fobj.close()


def main():
    ProcessScan()
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
        # print("CPU Usage: ", psutil.cpu_percent(),"%")
        print("Schedular started successfully!")
        print("Press Ctrl + c to abort the automation script.")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(10)
        
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