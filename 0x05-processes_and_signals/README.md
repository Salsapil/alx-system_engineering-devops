### Print parent ID -> echo $$   
   
### List of currently running processes:   
- ps: snapshot of the current processes on your system.   
- -a: Shows processes for all users.   
- -u: Displays detailed information in a user-oriented format.   
- -x: Lists processes without a controlling terminal (background processes).   
- -f: Provides a full-format listing with additional details.   
   
### Displays lines containing the bash word:   
- ps -auxf | grep "bash"   
   
### Displays To infinity and beyond indefinitely.
- pgrep: find and searches for process IDs based on given criteria.   
- -l: tells pgrep to show both the process name and its corresponding PID.   
   
### Write a Bash script that stops to_infinity_and_beyond process. -> kill "$(<PID>)"   
   
### SIGTERM signal   
- pkill: send signals to processes based on their names.   
- -f: the pattern should be matched against the entire command line.   
   
### Write a Bash script that kills the process 7-highlander.   
- The -9 option specifies the signal to send to the processes.   
- Signal number 9 corresponds to SIGKILL.   