import re

def match_ips(file_list):
  ip_list = []
  for filepath in file_list:
    with open(filepath, "r") as f:
      for line in f:
        ip = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
        if ip:
          ip_list.append(ip.group(0))

  return ip_list

def write_ips(ip_list, output_file):
  with open(output_file, "w") as f:
    for ip in ip_list:
      f.write(ip + "\n")

def main (file_list):
    output_file = "full-IP-list.txt"
    ip_list = match_ips(file_list)
    write_ips(ip_list, output_file)


if __name__ == "__main__":
  main()