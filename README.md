this version support xlsx writer to reader.xlsx file. To write all posts to different csv files with weight 1-2 GB you need
to uncomment:
filename = str(iterater) + ".csv"   # line 208 in add_numbers function
subprocess.call(['touch', filepath])  # line 210 in add_numbers function
write_csv(good, filename) # line 254 in post_searcher function
