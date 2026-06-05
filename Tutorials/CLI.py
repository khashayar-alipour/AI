

#   ================================================================
#   ============         Command Line Interface         ============
#   ============           Ali Pilehvar Meybodi         ============
#   ============             Khashayar Alipour          ============
#   ============              License MIT               ============
#   ============                  2025                  ============
#   ================================================================




'''

unix
linux = kernel



GUI vs CLI
CLI -> faster - powerful


SHELL:
    a programm type that reads your command, understands it and executes it.
    bash, zsh, fish, powershell, CMD, ...

    Bash ( Bourne Again Shell):
        A famous default shell on Mac and linux.
        - Windows -> install Git Bash or WSL (Windows Subsystem for Linux)
        

    
    ====================
    ==   Navigation   ==  
    ====================

- pwd
- ls


    ============================
    ==   Change directories   ==  
    ============================

- cd folder_name    # move into folder
- cd ..             # move back one folder
- cd~               # go to home
- cd/               # go to root (before Users folder)


    =================================
    ==   Create folder and files   ==  
    =================================

mkdir my_project     # make folder
touch file.txt       # make empty file



    ===========================
    ==   View file content   ==  
    ===========================

- cat file.txt
- less
- more

    
    ============================
    ==   Quit/exit terminal   ==  
    ============================

- exit


     ====================
     ==   Copy files   ==  
     ====================

- cp source_file destination_folder    # copy file
- cp source_file destFolder/destFile    # copy file to a folder


    ===========================
    ==   Rename/Move files   ==  
    ===========================
    
- mv old_name.txt  new_name.txt   # rename a file
- mv file.txt  folder/            # move file into a folder


    ============================
    ==   Delete file/folder   ==  
    ============================

- rm file.txt            # remove a file
- rm -r folder_name      # remove a folder


    =========================
    ==   File permission   ==  
    =========================

- ls -l

    
    ===========================
    ==   Change permission   ==  
    ===========================

- chmod +x script.sh     # make file executable
- chmod 644 file.txt     # set read/write permissions
- chown
- chgrp


    ========================
    ==   searching text   ==  
    ========================
    search for text in files
    
- grep
- find    


    ===================
    ==   File Info   ==  
    ===================
    get file information
    
- file
- wc
- stat
- du
- df


    =====================
    ==   System Info   ==  
    =====================
    get system information

- whoami
- uname
- date
- uptime


    =====================
    ==   Compression   ==  
    =====================
    compress files

- tar
- gzip
- gunzip
- zip
- unzip


    ======================
    ==   Networking     ==  
    ======================

- ping      # ping www.google.com
- curl      # sends request to a direct url
- wget      # downloads a file using a direct url
- ssh


    =========================
    ==   Text editting     ==  
    =========================

- nano
- vi
- vim


    ======================
    ==   Enviroment     ==  
    ======================
    manage enviroments

- echo
- export
- env
- alias








=================================================================
===================                        ======================
===================       CLI Tools        ======================
===================                        ======================
=================================================================


    ======== vim ========

- i            # insert a text
- ESC          # back to normal mode
- :w           # save file    
- :q           # quit
- :wq          # save and quit
- u            # undo
- ctrl + r     # redo
- x            # cut
- y            # copy
- p            # paste
- /pattern     # search - press n for next, N for previous



    ======== nano ========

- ctrl + o     # save file
- ctrl + x     # quit
- ctrl + w     # search
- ctrl + k     # cut text
- ctrl + c     # copy text
- ctrl + v     # paste text



    ======== git ========

git config --global user.name 'Khashayar Alipour'
git config --global user.email 'khashayar.alipour111@gmail.com'
git config --global --list


git restore --staged file.py
git restore --staged .


git log
git log -5
git log --author="your name"


[connect local to remote]
git remote add origin https://github.com/khashayar_alipour/repo


[to memorize user and password in github]
git config --global credential.helper store
git config --global credential.helper manager


[push]
git push -u origin main    #use this when your pushing for the first time
git push origin main
git push origin



'''