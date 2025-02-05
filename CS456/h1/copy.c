/*

implementing a version of the "cp" command using standard C Library functions

cp - copies a file

*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

  if (argc < 3) { // prints usage statement if not enough arguments
    fprintf(stderr, "Usage: %s <src> <dst>\n", argv[0]);
    exit(1); // exits the program
  }

  // declare file pointers
  FILE *src, *dst;
  //  open the source fiile for reading
  src = fopen(argv[1], "r");
  //  open the destination file for writing
  dst = fopen(argv[2], "w");

  // check return value of fopen for the source file
  // if it's NULL print usage statement and exit the program
  if (src == NULL) {
    fprintf(stderr, "Usage: %s <src> <dst>\n", argv[0]);
    exit(1);
  }

  // if we get here, we then read every character in the source file,
  // and then write the character to the destination file
  char c;
  while ((c = fgetc(src)) != EOF) {
    // write the character to the destination file.
    fputc(c, dst);
  }

  // close the source file
  fclose(src);
  // close the destination file
  fclose(dst);

  return 0;
}