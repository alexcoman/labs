import sys
import os
import os.path
import shutil
import time
import filecmp

def copy_all(file_list, src, dest):
	for lfile in file_list:
		lfile_path = os.path.join(src, os.path.basename(lfile))
		if os.path.isdir(lfile_path):
			shutil.copytree(lfile_path, os.path.join(dest, os.path.basename(lfile)))
			print "Copied directory {} from {} to {}.".format(os.path.basename(lfile), 
				os.path.basename(src), os.path.basename(dest))
		else:
			shutil.copy2(lfile_path, dest)
			print "Copied file {} from {} to {}.".format(os.path.basename(lfile), 
				os.path.basename(src), os.path.basename(dest))

def check(dir1, dir2):
	comparison = filecmp.dircmp(dir1, dir2)
	if comparison.common_dirs:
		for ldir in comparison.common_dirs:
			check(os.path.join(dir1, ldir), os.path.join(dir2, ldir))
	if comparison.left_only:
		copy_all(comparison.left_only, dir1, dir2)
	if comparison.right_only:
		copy_all(comparison.right_only, dir2, dir1)
	dir1_newer = []
	dir2_newer = []
	if comparison.diff_files:
		for lfile in comparison.diff_files:
			if os.stat(os.path.join(dir1, lfile)).st_mtime > os.stat(os.path.join(dir2, lfile)).st_mtime:
				dir1_newer.append(lfile)
			else:
				dir2_newer.append(lfile)
	copy_all(dir1_newer, dir1, dir2)
	copy_all(dir2_newer, dir2, dir1)

def synchronize(dir1, dir2, ptime):
	print "   Synchronization between {} and {} was started! ({})\n".format(os.path.basename(dir1), os.path.basename(dir2), time.ctime())
	print " Source Directory Path: {}".format(dir1)
	print " Destination Directory Path: {}".format(dir2)
	print
	while True:
		print " Checking ... "
		check(dir1, dir2)
		print " Checking ... DONE\n"
		time.sleep(ptime)

if __name__ == "__main__":
	print

	if len(sys.argv) != 4:
		print "Too many/much arguments!"
		print " Usage: python {} <dir1> <dir2> <time>".format(sys.argv[0])
		exit()

	if not os.path.isdir(os.path.join(sys.argv[1])):
		print "{} is not a directory!".format(sys.argv[1])
		exit()

	if not os.path.isdir(os.path.join(sys.argv[2])):
		print "{} is not a directory!".format(sys.argv[2])
		exit()

	try:
		ptime = int(sys.argv[3])
	except ValueError:
		print "{} is not an integer!".format(sys.argv[3])
		exit()

	synchronize(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), ptime)