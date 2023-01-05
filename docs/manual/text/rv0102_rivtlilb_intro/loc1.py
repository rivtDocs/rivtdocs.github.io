#!/usr/bin/env python
import os
import fnmatch

#directory1 = "C:/Anaconda/lib/site-packages/once/"
directory1 = ("D:/Egnyte/Shared/01_General/03_Engineering/05_Tracker"
               "/05_DesignTestManufacture/14_StructuralAnalysis"
               "/final_struct_docs/asce_tracker60/")

def Walk(root='', recurse=True, pattern='*'):
    """
        Generator for walking a directory tree.
        Starts at specified root folder, returning files
        that match our pattern. Optionally will also
        recurse through sub-folders.
    """
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)
        if not recurse:
            break

def LOC(root='', recurse=True, match1='*.py'):
    """
        Counts lines of code in two ways:
            maximal size (source LOC) with blank lines and comments
            minimal size (logical LOC) stripping same

        Sums all Python files in the specified folder.
        By default recurses through subfolders.
    """
    count_mini, count_maxi = 0, 0
    for fspec in Walk(root, recurse, match1):
        skip = False
        for line in open(fspec).readlines():
            count_maxi += 1
            line = line.strip()
            if line:
                if line.startswith('#'):
                    continue
                if line.startswith('"""'):
                    skip = not skip
                    continue
                if not skip:
                    count_mini += 1

    return count_mini, count_maxi

ftype = '*.txt'
count1 = LOC(directory1,False, ftype)
print("directory, type : ", directory1, ftype)
print("min count: ", count1[0])
print("max count: ", count1[1])


