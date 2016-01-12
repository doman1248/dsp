# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. ```vim /path/<filename>``` -> editor mode
> >   * Once in vim -> ```:set number``` -> numbers each line
> >   * Once in vim -> ```:%s/foo/bar/g``` -> find each occurrence of 'foo' and replace with 'bar'
> > 2. ```wc -l <filename>``` -> gives number lines in a file
> > 3. ```head <filename>``` -> see first 10 lines of file
> >   * ```head -n100 <filename>``` -> see first 100 lines of file
> > 4. ```chmod +x <filename>``` -> makes file executable
> > 5. ```history``` -> gives the history of all commands ran in terminal
> > 6. ```grep -i <pattern> <filename> > test.txt``` -> finds pattern (-i is for case insensitive) in file and saves to test.txt
> > 7. ```mv -i file1 file2``` -> rename file from file1 to file2, and if file2 exists prompt confirmation before overwriting
> > 8. ```less <filename>``` -> viewing large files
> > 9. ```scp /path1/file1 /path2/file1``` -> securely transfering file(s) between machines
> > 10. ```rm <filename>``` -> remove files  

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ```ls``` -> list all items in current directory
> > ```ls -a``` -> list all items including hidden files and directories in current directory
> > ```ls -l``` -> list all items including file/dir information including file size, read/write/executable status, etc.
> > ```ls -lh``` -> same as 'ls -l', but formats the file/dir size.
> > ```ls -la``` -> this combination is pretty meaningful because it gives total list of items as well as additional metadata

---


---

What does `xargs` do? Give an example of how to use it.

> > * 'xargs' is used to build and execute command lines from standard input. 
> > * example: ```find . -name "*.R" | xargs grep library(ggplot2)```
> > * output: It will generate list of .R files where 'library(ggplot2) appears. It will list the same file twice if 'library(ggplot2)' appears multipe times.

---

