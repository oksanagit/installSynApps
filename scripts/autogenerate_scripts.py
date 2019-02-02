#
# Script that auto-generates install and uninstall bash
# scripts based on specified INSTALL_CONFIG file
#
# Author: Jakub Wlodek
# Created on: 2-Feb-2019
#


import os
import read_install_config


auto_generated_message="# This script was autogenerated for use with the local install of EPICS and synApps\n"


#
# Order of compilation:
# EPICS_BASE
# EPICS_SUPPORT
# ADSupport
# ADCore
# ADPlugins
# ADDrivers
#
def generate_install_script(modules_to_install):
    install_file = open("autogenerated/install.sh", "w+")
    install_file.write(auto_generated_message)
    install_file.write("\n")
    
    for module in modules_to_install:
        install_file.write(module[0]+"="+module[2]+"\n")
    
    for module in modules_to_install:
        install_file.write("cd $"+module[0]+"\n")
        install_file.write("make -sj\n")
    
    install_file.close()


def generate_uninstall_script(modules_to_uninstall):
    uninstall_file = open("autogenerated/uninstall.sh", "w+")
    uninstall_file.write(auto_generated_message)
    uninstall_file.write("\n")
    
    for module in modules_to_uninstall:
        uninstall_file.write(module[0]+"="+module[2]+"\n")
    
    for module in modules_to_uninstall:
        uninstall_file.write("cd $"+module[0]+"\n")
        uninstall_file.write("make clean uninstall\n")
        uninstall_file.write("make clean uninstall\n")  

    uninstall_file.close()


def create_scripts():
    module_list, install_location = read_install_config.read_install_config_file()
    modules_to_install = []
    for module in module_list:
        if module[4] == "YES" and module[0] != "CONFIGURE" and module[0] != "DOCUMENTATION" and module[0] != "UTILS":
            modules_to_install.append(module)

    if os.path.exists("autogenerated"):
        for file in os.listdir("autogenerated"):
            os.remove("autogenerated/"+file)
    else:
        os.mkdir("autogenerated")

    generate_install_script(modules_to_install)
    generate_uninstall_script(modules_to_install)


create_scripts()