import subprocess

# Run the first Python script
file_name = input("filename : ")
# output_file = input("output_filename : ")
subprocess.run(["python", "get_links.py",file_name])

# Run the second Python script
subprocess.run(["python", "main2.py",file_name,file_name])


# Add more subprocess.run() calls for additional scripts if needed
