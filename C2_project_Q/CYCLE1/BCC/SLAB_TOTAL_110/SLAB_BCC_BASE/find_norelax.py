import glob

files=glob.glob("*_NOMAG/*/output.*/0/1/stdout.1.0")
find_lines="The maximum number of steps has been reached."
#find_lines="maximum"


for path in files:
    with open(path) as f:
        lines=f.readlines()
#        print(lines)

    lines_strip = [line.strip() for line in lines]
    l_XXX = [line for line in lines_strip if find_lines in line]
    if len(l_XXX)>0:
        print(path.split("/")[0]+("/")+path.split("/")[1])
