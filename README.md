# Disclaimer

The implementation work of the discipline of Operational Systems (UNB), shown below was developed in a group (Boris Marinho, Guilherme Andreúce, Pedro Henrique and Roberta Costa).

# Guidelines
## Problem
Implementation of a multiprogrammed pseudo-SO, composed of a Process Manager, a Memory Manager and an Input / Output Manager.
The process manager must be able to apply the scheduling algorithm defined by parameter by the OS user.

The memory manager must ensure that one process does not access the memory regions of another process, and that the page replacement algorithm is used properly. 

The input / output must be responsible for administering the algorithm specified for the disk search.

Each module will be tested according to the specifications determined in the example files. 

In addition, the pseudo-SO must receive as an parameter an integer and a text file, for example $1 processes.txt. The integer determines which module should be activated (in the example given it means that the process module will be activated, as it was the integer 1), and the text file (with .txt extension) passes on the necessary input data for the execution of the chosen module. 

The details for implementing this pseudo-SO are described in the following sections.

### Process Management Module
In this module, the team must implement a set of CPU scheduling algorithms and write a program that calculates a series of statistics based on these algorithms. The algorithms for scheduling to be implemented are as follows:

- FIFO: First-In, First-Out
- SJF: Shortest Job First
- RR: Round Robin (with quantum = 2)

The process management module should read from the standard input a list of processes with their arrival times and duration, and a table containing the values ​​for the following metrics:

- Average total process execution time - turnaround;
- Average response time;
- Average waiting time.

Total process execution time is the amount of time needed to fully execute a process, that is, the total time between the creation of a process and its completion. 

Response time is the amount of time between a program's execution request (when it is placed in the ready queue) and its time to go to execution (time sharing system), this means that it is the time that the process takes time to produce each response to a request (so, let's assume it's the time elapsed between one trip and the other to the CPU. This metric is important for interactive processes).

Waiting time is the total amount of time that a process waited in the ready queue waiting to be scheduled, that is, it is the time that the process waited in the ready queue.

#### Description of the Process Management Module Entry
The text file consists of a series of pairs of whole numbers separated by a blank space indicating the time of arrival and the duration of each process. The entry ends with the end of the file. The activation of this module must be with the parameters $ <executable> 1 <textTextName.txt>
#### Description of the Process Management Module Output
The output consists of lines containing the acronym for each of the three algorithms and the values of the three metrics requested. Each line shows the acronym of the algorithm and the average values (with one decimal place) for total execution time, response time and waiting time, exactly in that order, separated by a blank space.

#### Memory Management Module
In this module, the team must write a program to simulate the functioning of the main page replacement algorithms studied in the discipline. The page replacement algorithms to be implemented are as follows:

- FIFO (First In, First Out);
- Second Chance (with the R bit being reset after every 3 references to memory);
- LRU: (Least Recently Used or Least Recently Used).

The program should read from the standard input a set of integers, of which the first number represents the number of memory frames available in RAM and the others represent the sequence of references to the pages, always one number per line.

In addition, the program must print on the output the number of missing pages obtained with the use of each of the algorithms.

#### Description of the Entry for the Memory Management Module
The entry consists of a series of integers, one per line, indicating, first, the number of frames (frames) available in the RAM memory, and then the sequence of references to the memory. The activation of this module must be with the parameters $ <executable> 2 <textFileName.txt>
#### Output Description for the Memory Management Module
The output consists of lines containing the acronym for each of the three algorithms and the number of page faults obtained using each of them.

#### Input / Output Management Module
In this module, the team must write a program to simulate the operation of the main disk scheduling algorithms studied in the discipline. The disk scheduling algorithms to be implemented are as follows:

- FCFS (First Come, First Serve);
- SSF (or SSTF - arm initially downwards);
- SCAN.

The program should read from the standard input a set of integers, in which the first number represents the number of cylinders on the disk, the second number represents the cylinder on which the disk's reading head is initially positioned, and the others represent a sequence of access requests to be answered, always one number per line.

The program should print at the output the total number of cylinders traveled by the reading head to meet all the requested requests using each of the algorithms.
#### Input / Output Module Input Description
The entry consists of a series of integers, one per line, indicating, first, the number of the last cylinder on the disk (the cylinders vary from 0 to this number), the cylinder on which the reading head is initially positioned and the sequence of access requests. The activation of this module must be with the parameters $ <executable> 3 <textFileName.txt>

#### Input / Output Module Output Description
The output consists of lines containing the acronym for each of the three algorithms and the total number of cylinders traveled by the read head to meet all requests for access to the disk.

### Program Structure
The program is expected to be structured in at least four major modules: kernel, process, memory and input / output. These models should be:

- Kernel module - contains the calls for the other modules.
- Process Module - classes and data structures related to the process. Basically, it keeps information specific to the process.
- Memory Module - provides a RAM memory abstraction interface.
- Input / Output Module - deals with the allocation of the disk arm for writing / reading in the disk blocks for the processes.

It is also important to emphasize that other modules can be used, if necessary.

# Build instructions
python version: 3.9.2
python kernel.py $1 $path/file

$1 = module  $path = "test file path"
module: 1 = process, 2 = memory, 3 = in/out