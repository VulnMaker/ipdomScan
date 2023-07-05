import os

def get_file_names_in_folder(folder_name):
  """Gets all the file names in a folder and stores them in an array."""
  file_names = []
  for file_name in os.listdir(folder_name):
    if os.path.isfile(os.path.join(folder_name, file_name)):
      file_names.append(file_name)
  return file_names

def main():
  """The main function."""
  file_names = get_file_names_in_folder("data")

if __name__ == "__main__":
  main()
