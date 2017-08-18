# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

`pwd` - show current working directory path  
`mkdir` - creating a directory  
`rm -r dir` deletes a directory and its files  
`touch file.txt` creates a file with the `touch` command  
`rm file.txt` deletes a file  
`mv file.txt new_file.txt` renaming a file  
`ls -a` lists all files, including hidden files  
`cp ~/path/file.txt ~/new_path` copies a file from one directory to another  
`cd ~` returns to the home directory  
`sort file.txt` and `uniq file.txt` can be used to sort entries in a file and filter out duplicate entries  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls` lists the contents of a directory  
`ls -a` lists all contents, even hidden files  
`ls -l`long lists files and directories as a table and includes access rights, number of hard links, username of file's owner, group that owns the file, size of the file in bytes, last modified date, and the name of the file  
`ls -lh` long lists with human readable file sizes  
`ls -lah`long lists with human readable file sizes and hidden files included  
`ls -t` orders contents based on their last modified date  
`ls -Glp` makes a long list but does not print group names and appends '/' to directories  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -m` displays names as a comma separated list  
`ls -d` displays only directories  
`ls -c` displays files by file timestamp  
`ls -F` flags filenames  
`ls -r` displays files in reverse order  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` is used to remove or perform an operation on a list of one or more comma/space separated results produced by a `grep` or `find` command, for example. The following is an example: `find . -name '*.py' | xargs grep 'word'` where all .py files are located in the current directory and the files with 'word' are displayed.  

 

