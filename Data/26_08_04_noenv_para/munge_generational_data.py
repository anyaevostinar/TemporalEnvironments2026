import os.path
import gzip

folder = '../../Data/26_08_04_noenv_para/'

treatment_folders = ["run_parasites_changing"]
reps = range(100,130)
header = "uid treatment rep update mean_generations variance_generations parent_num_task_sets parent_entropy_task_sets current_num_task_sets current_entropy_task_sets partner\n"

outputFileName = "munged_generational_data.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for t in treatment_folders:
    for r in reps:
        fname = folder +t+"/" + str(r) + "/output/CurrentUpdateInfo_data.csv"
        uid = t + "_" + str(r)
        curFile = open(fname, 'r')
        for line in curFile:
            if (line[0] != "u"):
                splitline = line.strip().split(',')
                
                outstring1 = "{} {} {} {} {} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0], splitline[1], splitline[2], splitline[79],splitline[80],splitline[81],splitline[82],"Host")
                outFile.write(outstring1)
                outstring2 = "{} {} {} {} {} {} {} {} {} {} {}\n".format(uid, t, r, splitline[0], splitline[3], splitline[4], splitline[83],splitline[84],splitline[85],splitline[86],"Sym")
                outFile.write(outstring2)
        curFile.close()
outFile.close()
