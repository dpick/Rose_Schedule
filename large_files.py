import os

largest_files = []
MAX_FILES = 10

def add_to_array(item):
  if len(largest_files) < MAX_FILES:
    largest_files.append(item)
  else:
    if os.path.getsize(item) > os.path.getsize(largest_files[-1:][0]):
      insert_item(item, os.path.getsize(item))

def insert_item(item, size):
  for counter, path in enumerate(largest_files):
    if size > os.path.getsize(path):
      largest_files.insert(counter, item)
      return largest_files[:-1]

def get_files(dirpath):
  a = [s for s in os.listdir(dirpath)
       if os.path.isfile(os.path.join(dirpath, s))]
  return a


for filename in get_files("/home/david"):
    print filename
    add_to_array(filename)

print largest_files
