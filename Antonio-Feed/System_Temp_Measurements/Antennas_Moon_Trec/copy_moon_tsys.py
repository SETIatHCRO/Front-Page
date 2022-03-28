#!/usr/bin/python3
"""
Run on obs-node1 with caluser account
"""

import glob
import sys,os
import shutil


todir = "/home/caluser/Front-Page/Antonio-Feed/System_Temp_Measurements/Antennas_Moon_Trec"

results_dir = glob.glob("/home/caluser/Results/*")
results_dir = [rdir for rdir in results_dir if "moon_" in rdir]
results_dir = sorted(results_dir)

for rdir in results_dir:
    # rdir = "/home/caluser/Results/moon_2022-03-17-04:58:50_1647555453"

    # basename = "moon_2022-03-17-04:58:50_1647555453"
    basename = os.path.basename(rdir)

    # ants_results = ["/home/caluser/Results/moon_2022-03-17-04:58:50_1647555453/1c_Results.csv",
    #  "..."]
    ants_results = glob.glob(os.path.join(rdir, "*"))

    for result in ants_results:
        # result = "/home/caluser/Results/moon_2022-03-17-04:58:50_1647555453/1c_Results.csv"

        # rname = "1c_Results.csv"
        rname = os.path.basename(result)
        ant = rname[:2]

        # todir_ant = $todir + "/moon_2022-03-17-04:58:50_1647555453/1c"
        todir_ant = os.path.join(todir, basename, ant)

        print(todir_ant)
        # if data exist, then skip to next
        if os.path.exists(todir_ant):
            continue

        # otherwise create directory
        os.makedirs(todir_ant)

        # result_github = $todir + "/moon_2022-03-17-04:58:50_1647555453/1c/1c_Results.csv"
        result_github = os.path.join(todir_ant, rname)

        shutil.copyfile(result, result_github)
