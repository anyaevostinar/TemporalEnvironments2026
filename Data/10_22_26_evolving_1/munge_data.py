import os.path
import gzip

folder = '../../Data/10_22_26_evolving_1'

treatment_folders = ["run_parasites_changing"]
reps = range(100,130)
header = "uid treatment rep update task task_count partner\n"
task_names = {1:"NAND", 2:"NOT", 3:"OR_NOT", 4:"AND", 5:"OR", 6:"AND_NOT", 
    7:"NOR", 8:"XOR", 9:"EQU"}

outputFileName = "munged_basic_tasks.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for t in treatment_folders:
    for r in reps:
        fname = folder + "/"+t+"/" + str(r) + "/output/TransmissionRates_data.csv"
        uid = t + "_" + str(r)
        curFile = open(fname, 'r')
        for line in curFile:
            if (line[0] != "u"):
                splitline = line.strip().split(',')
                for task in range(1,11): # nine logic tasks
                    outstring1 = "{} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0], task, splitline[task], "horiz_attempt")
                    outFile.write(outstring1)
                    
                for task in range(11,21): # nine logic tasks
                    outstring1 = "{} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0], task, splitline[task], "horiz_success")
                    outFile.write(outstring1)
                    
                for task in range(21,31): # nine logic tasks
                    outstring1 = "{} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0],task, splitline[task], "vert_attempt")
                    outFile.write(outstring1)
                    
                for task in range(31,41): # nine logic tasks
                    outstring1 = "{} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0], task, splitline[task], "vert_success")
                    outFile.write(outstring1)
                    
        curFile.close()
outFile.close()
