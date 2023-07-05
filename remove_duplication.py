import os
import sys

def remove_duplicates(input_file, output_file):
    lines_seen = set()
    with open(input_file, "r") as f:
        for line in f:
            if line not in lines_seen:
                lines_seen.add(line)
                with open(output_file, "a") as fw:
                    fw.write(line)

def collect(input_file):
        input_file
        output_file = "unique-" + input_file
        remove_duplicates(input_file, output_file)
        
def main():
          collect("full-domains-list.txt")
          collect("full-IP-list.txt")
     


if __name__ == "__main__":
     main()