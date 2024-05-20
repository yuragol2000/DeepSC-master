import subprocess

# subprocess.run(['python', 'performance.py','--channel','AWGN','--n-gramm','4'])
# subprocess.run(['python', 'performance.py','--channel','Rician','--n-gramm','2'])
subprocess.run(['python', 'performance.py','--channel','Rician','--n-gramm','1'])
# subprocess.run(['python', 'performance.py','--channel','Rician','--n-gramm','4'])
# subprocess.run(['python', 'performance.py','--channel','Rayleigh','--n-gramm','2'])
# subprocess.run(['python', 'performance.py','--channel','Rayleigh','--n-gramm','3'])
# subprocess.run(['python', 'performance.py','--channel','Rayleigh','--n-gramm','4'])
# subprocess.run(['python', 'Plot_maker.py'])