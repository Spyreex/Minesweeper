import os
rough = 'C:/Users/'
list = []
for entry in os.scandir(rough):
    print(entry.name)
    if not entry.name.startswith('.') and not entry.is_file() and not entry.name.startswith('Default') and not entry.name == 'Public' and not entry.name == 'All Users':
        print()
        for entry2 in os.scandir(rough+entry.name+'/'):
            print(entry2.name)
            if not entry2.name.startswith('.'):
                for path, dirs, files in os.walk(rough+entry.name+'/'+'Appdata/Local/Programs/Python'):
                    for name in files:
                        if 'python.exe' in name:
                            list.append(path)
                            print(list)
                            location = os.path.dirname(os.path.abspath(__file__))+'/minesweeperv2.py'
                            start = open('newgame.bat','w')
                            start.write(list[0]+'/python.exe '+location)
                            start.close()

                            exit()
print(list)