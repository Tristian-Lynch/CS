/*

implementing a version of the "head" command using standard C Library functions

head - prints the first 10 lines of a file, or a specified number of lines if a 
	   number is given

*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){

	//if not enough arguments provided, print usage statement and exit the program
	if(argc < 2){  
		fprintf(stderr,"Usage: %s <file> <number of lines>\n", argv[0]);
		exit(1);
	}


	
	FILE *fd;  //declare file pointer
			  // open the file specified by the user

	// check return value of fopen
	// if it's NULL print usage statement and exit the program


	int lines;  //declare variable for the number of lines we will print

	// if only the filename was specified, we will print 10 lines
		//hint: argc will be less than what?
	// else: we print however many lines specified



	
	char c; 				//declaring a char
	int linecount = 0; 		//counting the number of lines so far
	while((c=fgetc(fd))){

		//check if we've reached the end of file, if so break the loop
		
		//print a single character to the screen

		//if we see a newline character, increment linecount

		//if linecount equals the number of lines specified break the loop

	}

	fclose(fd); //close the file

	return 0;

}