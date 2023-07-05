import os
import extract_domains
import extract_ip
import remove_duplication

def get_file_names_in_folder():
  folder_name= "data"
  """Gets all the file names in a folder and stores them in an array."""
  file_names = []
  for file_name in os.listdir(folder_name):
    if os.path.isfile(os.path.join(folder_name, file_name)):
      file_names.append(os.path.join(folder_name, file_name))
  return file_names

def main():
  list = get_file_names_in_folder()
  extract_domains.main(list)
  extract_ip.main(list)
  remove_duplication.main()

if __name__ == "__main__":
  main()
