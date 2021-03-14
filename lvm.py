
import os 

while(True):

    print("**************************************************************************************")
    print((LVM Script for Automation")
    print("**************************************************************************************")
    print("1) Check available disks ")
    print("2) Create a Physical Volume")
    print("3) Create a Volume Group")
    print("4) Create a Logical Volume")
    print("5) Extend Logical Volume")
    print("6) Exit")
    print()
    ch = input("Select task to be done ")
    if(ch == "1"):
        os.system("fdisk -l")
    elif(ch == "2"):
        disk = input("Enter disk name: ")
        os.system(f"pvcreate {disk}")
    elif(ch == "3"):
        vg = input("Enter name of the Volume Group: ")
        disks = input("Enter disk names with space between names: ")
        os.system(f"vgcreate {vg} {disks}")
    elif(ch == "4"):
        vg = input("Enter name of Volume Group: ")
        lv = input("Enter name of the Logical Volume: ")
        size = input("Enter size you want for Logical Volume: ")
        dir = input("Enter directory name to mount storage: ")
        os.system(f"mkdir /{dir}")
        os.system(f"lvcreate --size {size} --name {lv} {vg}")
        os.system(f"mkfs.ext4 /dev/{vg}/{lv}")
        os.system(f"mount /dev/{vg}/{lv} /{dir}")
    elif(ch == "5"):
        vg = input("Enter name of Volume Group: ")
        lv = input("Enter name of LVM: ")
        size = input("Size to increase: ")
        os.system(f"lvextend --size +{size} /dev/{vg}/{lv}")
        os.system(f"resize2fs /dev/{vg}/{lv}")
    elif(ch == "6"):
        print("------------------------------------------------Good Bye----------------------------------------------------")
        break
