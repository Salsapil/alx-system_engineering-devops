### Print parent ID -> echo $$   
   
### List of currently running processes:   
- ps: snapshot of the current processes on your system.   
- -a: Shows processes for all users.   
- -u: Displays detailed information in a user-oriented format.   
- -x: Lists processes without a controlling terminal (background processes).   
- -f: Provides a full-format listing with additional details.   
   
### Displays lines containing the bash word:   
- ps -auxf | grep "bash"   
   
### 
- pgrep: find and searches for process IDs based on given criteria.   
- -l: tells pgrep to show both the process name and its corresponding PID.   
   
