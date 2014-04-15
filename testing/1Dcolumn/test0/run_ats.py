import os, sys, subprocess
from shutil import rmtree

def run_ats(input_file, nproc=1, directory=None):
    if directory is None:
        directory = os.getcwd()

    CWD =os.getcwd()
    run_directory= os.path.join(CWD,"amanzi-output")


    if os.path.isdir(run_directory):
        rmtree(run_directory)
    os.mkdir(run_directory) 
    os.chdir(run_directory)
    
    # ensure that ATS's executable exists
    try:
        path = os.path.join(os.environ['ATS_DIR'],'bin')
    except KeyError:
        raise RunTimeError("Missing ATS installation, please set the ATS_DIR environmental variable.")
    executable = os.path.join(path, "ats")

    if not os.path.isfile(executable):
        raise RunTimeError("Missing ATS installation, please build and install Amanzi.")

    try:
        stdout_file = open("stdout.out", "w")
        ierr = subprocess.call([executable, "--xml_file="+input_file], stdout=stdout_file, stderr= subprocess.STDOUT)
        
    finally:
        os.chdir(CWD)

        return ierr

if __name__=='__main__':

    if len(sys.argv) < 2:
        sys.stderr.write('\nUsage: python '+sys.argv[0]+' input_file_name\n\n')
        sys.exit(1)

    ierr = run_ats(sys.argv[1])
