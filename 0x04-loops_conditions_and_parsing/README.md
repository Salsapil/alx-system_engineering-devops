## Loops, conditions and parsing
**1. How to Create SSH Keys.**
***On Linux and macOS:***
- Open a terminal window.   
- Run the following command:   
```bash
ssh-keygen
```
- Press Enter to accept the default file location   
(~/.ssh/id_rsa for the private key and ~/.ssh/id_rsa.pub for the public key).   
- Optionally, enter a secure passphrase when prompted.
- Type the passphrase again to confirm.   
****
**2. What is the advantage of using #!/usr/bin/env bash over #!/bin/bash.**   
- Ensures the script runs using the first available bash interpreter in the system's PATH, making it more portable across different environments.   
- Avoids potential security issues that might arise if a malicious program replaces the system's default bash binary.   
****
**3. How to use while, until and for loops.**   
***while Loop:***
```bash
while condition; do
  # Statements to execute while the condition is true
done
```   
***until Loop:***
```bash
until condition; do
  # Statements to execute until the condition is true
done
```   
***for Loop:***
```bash
for variable in list; do
  # Statements to execute for each item in the list
done
```   
****   
**4. How to use if, else, elif and case condition statements.**
***if, else and elif Statements:***
```bash
if condition; then
  # Statements to execute if the condition1 is true
elif condition2; then
  # Statements to execute if condition2 is true
else
  # Statements to execute if neither condition is true
fi
```   
***case Statement:***
```bash
case variable in
  value1)
    # Statements to execute if variable matches value1
    ;;
  value2)
    # Statements to execute if variable matches value2
    ;;
  *)
    # Default case
    ;;
esac
```   
****   
**5- How to use the cut command.**   
***Options:***
- -b: Selects characters by byte position.   
- -c: Selects characters by column position.   
- -d DELIMITER: Specifies the delimiter (default is tab).   
- -f FIELD: Selects specific fields (numbered from 1, starting from the left).   
- -n: Prints only the first N characters of each line.   
- -s: Suppresses lines not containing the delimiter.   

```bash
cut [OPTIONS] [FILE]
```   
****   
**6- What are files and other comparison operators, and how to use them.**   
***File Operators:***   
These operators check the existence, type, and permissions of files:   
- -e: Checks if a file exists.   
- -f: Checks if a file is a regular file.   
- -d: Checks if a file is a directory.   
- -s: Checks if a file is empty (has zero size).   
- -x: Checks if a file is executable.   
- -r: Checks if a file is readable.   
- -w: Checks if a file is writable.   
   
***Comparison Operators:***
These operators compare values and return true or false:   
- ==: Equal to.   
- !=: Not equal to.   
- -lt: Less than.   
- -gt: Greater than.   
- -le: Less than or equal to.   
- -ge: Greater than or equal to.   
****