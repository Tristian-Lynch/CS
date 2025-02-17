/*

Given a file, we will print some information about this file

We will be using the stat function to get information

reading: man 2 stat, man 7 inode

stat takes two arguments, the name of the file, and the buffer 

*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>

void printFileType(int mode); // this function will be defined below main
                              // you will fill this out below the main function

int main (int argc, char **argv){

	//prints usage statement if file not provided
	if(argc < 2){
		fprintf(stderr, "Usage %s file\n", argv[0]);
		exit(1);
	}


	struct stat st; // this calls the stat structure
			// it is already defined for us in the <sys/stat.h> header file
			// so no need to define it here

	// call stat on the filename, store the data in st
	// make sure to check the return value for errors, 
	// if there are errors, print an error message then exit.

	
	
	// now, print the following
	printf("File Name: %s\n", argv[1]);     // file name
	printf("File Inode: %llu\n", st.st_ino);	// file inode
		// size of the file 
		// the mode (contains unix permissions) Print this value in octal, not decimal
		// number of hard links 
		// time of last access
		// time of last modification
	        // Note: if you use the %d format on most of these, the compiler will give you a warning
	        //       along with a suggested format. Use that format instead.

	printFileType(st.st_mode); // a function I wrote that prints the type of file
				   // you will finish this function
	return 0;

}

void printFileType(int mode){

	// here we will be using Macros to help us determine if a 
	// file is a regular file, a directory, or a symbolic link
	// read man 7 inode for more information on inodes and Macros
	// related to inodes

	//check if file is a regular file
	if(S_ISREG(mode))
		printf("This is a Regular File\n");

	//check if file is a directory


	// check if file is a symbolic link


}
