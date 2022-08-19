import os
import subprocess

# Containers # Containers # Containers # Containers # Containers # Containers 

def delete_container():
    print("-> All Containers:")
    os.system("docker ps -a")
    containerName = input("-> Enter Container Name: ")
    containerName = "docker rm -f {}".format(containerName)
    os.system(containerName)
    print("-> Container Deleted, Returning to Main.")
    __main__()

def create_container():
    ports = input("-> Do You Want to Expose The Containers Port [Y/N]: ").casefold()
    if ports == "y":
        if check_if_port_used() == True:
            print("-> Container Currently Using the Avaliable Port, Stopping the Active Port.")
            deleteContainer = 'docker rm -f {}'.format(find_container_by_port())
            try:
                os.system(deleteContainer)
                print("-> Container Successfully Deleted, Returning to Main.")
                __main__()
            except:
                print("-> Error Deleting Container, Returning to Main.")
                __main__()
        elif check_if_port_used() == False:
            containerName = input("-> Enter Container Name: ")
            containerName = "docker run --name {} -d -p 8080:80 nginx:latest".format(containerName)
            os.system(containerName)
            __main__()
    elif ports == "n":
        containerName = input("-> Enter Container Name: ")
        containerName = "docker create --name {} nginx".format(containerName)
        os.system(containerName)
        __main__()
    else:
        print("Neither Selected, Returning")
        __main__()

def view_all_containers():
    try:
        print("-> All Containers.")
        os.system("docker ps -a")
        __main__()
    except:
        print("-> Error Printing all Containers, Returning to Main.")
        __main__()

def delete_all_containers():
    try:
        os.system("docker system prune -a")
        print("-> All Containers Deleted Successfully, Returning to Main.")
        __main__()
    except:
        print("-> Deleting all Containers Failed, Returning to Main.")
        __main__()

def rename_container():
    print("-> All Containers:")
    os.system('docker container ls -a --format "table {{.Names}}"')
    oldContainer = input("\n-> Enter Container You Want To Rename: ")
    newContainer = input("-> Enter New Container Name: ")
    a = 'docker rename {} {}'.format(oldContainer, newContainer)
    try:
        os.system(a)
        print("Container Successfully Renamed, Returning to Main.")
    except:
        print("Error Renaming Container, Returning to Main.")
        
# Volumes # Volumes # Volumes # Volumes # Volumes # Volumes # Volumes # Volumes 

def copy_volumes_between_containers():
    newContainer = input('-> Enter New Container Name, You Want to Create: ')
    oldContainer = input('-> Enter Old Container Name, You Want to Copy From: ')
    port = input('-> Enter Port You Want to Host Copied Volume On: [i.e. 8081:80]: ')
    copyVolumes = 'docker run --name {newContainer}-copy --volumes-from {oldContainer} -d -p {port} nginx'.format(newContainer, oldContainer, port)
    os.system(copyVolumes)
    __main__()

def create_container_with_volume():
    # docker run --name testing-container -v C:\Users\aiden\devops-project2021:/usr/share/nginx/html/ -d -p 8081:80 nginx:latest
    # to get path, CD into folder and type 'pwd'
    newContainer = input("-> Type New Container Name: ")
    projectPath = input("-> Type Path of Desired Volume Contents: ")
    port = input("-> Type Port: ")
    a = 'docker run --name {} -v {}:/usr/share/nginx/html/ -d -p {} nginx:latest'.format(newContainer, projectPath, port)
    try:
        os.system(a)
        print("-> Container with Volume Successfully Created!")
        __main__()
    except:
        print("-> Error! Failed, Returning to Main.")
        __main__()

# Ports # Ports # Ports # Ports # Ports # Ports # Ports # Ports # Ports # Ports 

def check_if_port_used():
    # Checks if the port is being used
    phrase = "0.0.0.0:8080->80/tcp"
    a = subprocess.check_output("docker ps -a")
    a = str(a)
    return '0.0.0.0:8080->80/tcp' in a

def find_container_by_port():
    a = subprocess.check_output('docker container ls --format="{{.ID}}\t{{.Ports}}"', shell=True, universal_newlines=True).strip()
    word_list = a.split()
    return word_list[0]

# Images # Images # Images # Images # Images # Images # Images # Images # Images 

def build_image():
    # . refers to the file location
    # docker build . -f Dockerfile.base -t imagename
    imageName = input("-> Type Image Name: ")
    a = 'docker build . -f Dockerfile.txt -t {}'.format(imageName)
    try:
        os.system(a)
        print("-> Image Successfully Created!")
        print("-> All Images")
        os.system('docker images')
        __main__()
    except:
        print("-> Error Creating Image, Returning to Main.")
        __main__()

def rename_image():
    print("-> All Images:")
    os.system('docker images --format "table {{.Repository}}\t{{.Tag}}"')
    oldContainer = input("\n-> Enter Container You Want To Rename: ")
    newContainer = input("-> Enter New Container Name: ")
    a = 'docker tag {}:latest {}:latest'.format(oldContainer, newContainer)
    b = 'docker image rm -f {}'.format(oldContainer)
    try:
        os.system(a)
        os.system(b)
        print("Image Successfully Renamed, Returning to Main.")
    except:
        print("Error Renaming Image, Returning to Main.")

# Misc # Misc # Misc # Misc # Misc # Misc # Misc # Misc # Misc # Misc # Misc # Misc 

def __main__():
    print("\n-> Main <-")





# Ignore # Ignore # Ignore # Ignore # Ignore # Ignore # Ignore # Ignore # Ignore