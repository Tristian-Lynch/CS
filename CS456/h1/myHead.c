/*

implementing a version of the "head" command using standard C Library functions

head - prints the first 10 lines of a file, or a specified number of lines if a
           number is given

*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  // if not enough arguments provided, print usage statement and exit the
  // program
  if (argc < 2) {
    fprintf(stderr, "Usage: %s <file> <number of lines>\n", argv[0]);
    exit(1);
  }
  // declare file pointer and open the file for reading
  FILE *fd = fopen(argv[1], "r");

  // check return value of fopen
  if (fd == NULL) {
    // if it's NULL print usage statement and exit the program
    fprintf(stderr, "Usage: %s <file> <number of lines>\n", argv[0]);
    exit(1);
  }

  // declare variable for the number of lines we will print
  // if only the filename was specified, we will print 10 lines
  // hint: argc will be less than what?
  // else: we print however many lines specified
  int lines;
  if (argc < 3) {
    lines = 10;
  } else {
    lines = atoi(argv[2]);
  }

  char c;            // declaring a char
  int linecount = 0; // counting the number of lines so far
  while ((c = fgetc(fd)) != EOF) {
    // print a single character to the screen
    fprintf(stdout, "%c", c);
    // if we see a newline character, increment linecount
    if (c == '\n') {
      linecount++;
    }
    // if linecount equals the number of lines specified break the loop
    if (linecount == lines) {
      break;
    }
  }

  fclose(fd); // close the file

  return 0;
}