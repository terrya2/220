## writeFile.py
# If the file does not exist, opening it for writing will cause it
# to be created in the local folder.  If it does exist, the open
# function will cause the file to be wiped clean.

def main():
    print("Executing read_write_file_test.py")

    # Choose the input file name. Open the input file to be read.
    in_file_name = "input.txt"
    in_file = open(in_file_name, "r")

    # Choose the output file name. Open the output file to be written.    
    out_file_name = "output.txt"
    out_file = open(out_file_name, "w")

    # Loop to read lines from the input file and write these to the
    # output file. Note that the "reading" is done by the for loop.
    for line in in_file:
        print(line.rstrip('\n'), file=out_file)

    print("The files have been processed.")

    out_file.close()


main()
