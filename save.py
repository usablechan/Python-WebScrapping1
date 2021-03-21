import csv

def save_to_file(jobs):
  file = open("jobs.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["titlte", "company", "loacation", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return
