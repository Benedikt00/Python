import os
import shutil
import subprocess

def sync_folders(master_folder, phone_folder):
	# Get a list of folders in the master folder on the PC
	master_folders = set(os.listdir(master_folder))
	# Get a list of folders in the phone's folder using ADB
	adb_command = f"adb shell ls {phone_folder}"
	process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate()

	phone_folders = set(out.decode().split("\r"))
	cleaned_list = [item.strip() for item in phone_folders if item.strip()]

	print(cleaned_list)
	# Calculate the missing folders on the phone
	missing_folders = master_folders - set(cleaned_list)

	print(missing_folders, " ---------------")
	# Copy missing folders from the PC to the phone using ADB
	for folder in missing_folders:
		src_path = os.path.join(master_folder, folder).replace(" ", "\ ")
		dest_path = f"{phone_folder}/{folder}".replace(" ", "\ ")
		print(f"adb push {src_path} {dest_path}")
		adb_push_command = f"adb push {src_path} {dest_path}"
		subprocess.run(adb_push_command, shell=True)
		print(f"Folder '{folder}' copied to phone.")


if __name__ == "__main__":
	# Replace these paths with your actual paths
	master_folder_path = R"C:\Users\bsimb\Music\Musik"
	phone_folder_path = R"/storage/5AD4-151C/Musik"
	sync_folders(master_folder_path, phone_folder_path)