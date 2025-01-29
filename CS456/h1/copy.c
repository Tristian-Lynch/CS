/*

implementing a version of the "cp" command using standard C Library functions

cp - copies a file

*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){

	if(argc < 3){   //prints usage statement if not enough arguments
		fprintf(stderr,"Usage: %s <src> <dst>\n", argv[0]);
		exit(1); //exits the program 
	}


	
	FILE *src, *dst;  //declare file pointers
			          // open the source fiile for reading
					  // open the destination file for writing

					  // check return value of fopen for the source file
					  // if it's NULL print usage statement and exit the program

	// if we get here, we then read every character in the source file, 
	// and then write the character to the destination file
	char c;
	while((c=fgetc(src))){

		 //if we reach the end of file, break the loop

		 //write the character to the destination file.
		 //what function would you use to write a character to a file?
	}

	//close the source file
	//close the destination file

	return 0;


}