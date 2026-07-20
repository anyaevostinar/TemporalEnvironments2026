import os.path
import gzip

folder = '../../Data/26_07_17_mut_interval_5000'

treatment_folders = ["run_parasites_changing"]
reps = range(100,130)
header = "uid treatment rep update task task_count poison_or_not partner\n"
task_names = {1:"NAND", 2:"NOT", 3:"OR_NOT", 4:"AND", 5:"OR", 6:"AND_NOT", 
    7:"NOR", 8:"XOR", 9:"EQU"}

outputFileName = "munged_basic_tasks.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)
count = 0
poison = -1
neutral = 0
reward = 1 
poison_or_not = 0

for t in treatment_folders:
    for r in reps:
        fname = folder + "/"+t+"/" + str(r) + "/output/Tasks_data.csv"
        uid = t + "_" + str(r)
        curFile = open(fname, 'r')
        for line in curFile:
            if (line[0] != "u"):
                count +=1
                splitline = line.strip().split(',')

                for task in range(1,10): # nine logic tasks
                    if (task_names[task] in ("AND", "OR", "NOT")):
                        poison_or_not = poison
                    elif (task_names[task] in ("NAND", "OR_NOT", "AND_NOT")):
                        poison_or_not = reward
                    else:
                        poison_or_not = neutral
                    outstring1 = "{} {} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0], task_names[task], splitline[task], poison_or_not, "Host")
                    outFile.write(outstring1)
                for task in range(10,19): # nine logic tasks
                    if (task_names[task-9] in ("AND", "OR", "NOT")):
                        poison_or_not = poison
                    elif (task_names[task-9] in ("NAND", "OR_NOT", "AND_NOT")):
                        poison_or_not = reward
                    else:
                        poison_or_not = neutral
                    outstring1 = "{} {} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0], task_names[task-9], splitline[task], poison_or_not, "Sym")
                    outFile.write(outstring1)
            
                if ((int(splitline[0]) % 5000 == 0) and (int(splitline[0])!= 0)):
                    reward, poison = poison, reward
        poison = -1
        neutral = 0
        reward = 1    
            
        curFile.close()
outFile.close()
