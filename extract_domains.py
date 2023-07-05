import re

def extract_domains(text):

  # The regular expression to match a domain name.
  mat = r"(?P<domain>[\w\-]+\.[a-z\.]{2,6})"

  # Open the `full-list.txt` file in append mode.
  with open("full-domains-list.txt", "a") as file:

    # Iterate over the matches found by the regular expression.
    for match in re.finditer(mat, text):

      # Write the match to the `full-list.txt` file, replacing the `.c` and the trailing dot with nothing.
      file.write(match.group().replace(".com",".com \n"))

def main(text_files):


  # Extract all the domains from the text files.
  for text_file in text_files:

    # Open the text file and read the contents.
    with open(text_file, "r") as f:
      text = f.read()

      # Extract the domains from the text.
      extract_domains(text)

if __name__ == "__main__":
  main()
