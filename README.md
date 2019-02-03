# installSynApps

A collection of scripts meant to install all of epics and synApps with one command

### Included scripts

Script name                    | Script Function
------------------- | ------------------------------------------------------
installSynApps.sh | top level bash script that runs the remaining scripts sequentially
clone_and_checkout.py | Clones all required repositories and checks out correct versions
read_install_config.py | Script that reads the data in the INSTALL_CONFIG file
update_release_file.py | Script that updates the release files in support and area detector
ad_config_setup.py | Script based on adConfigSetup, that replaces area detector configuration files
dependencyInstall.sh | bash script that installs all required packages for EPICS and synApps
script_generator.py | script that creates bash scripts for installing and uninstalling, so that compilation for other operating systems is simplified.

### Usage

There are only 2 files that need to be edited before running the script. These are the `configure/INSTALL_CONFIG` file, and the `scripts/dependencyInstall.sh` file. In the first, edit the install configuration for your installation. In most cases, you may simply change the `MODULE_INSTALL` tag for the modules you wish to build and those you don't wish to build, and you must also edit the line
```
INSTALL=/epics
```
to point to the top level directory in which you wish to install EPICS and synApps. In the other file that you must edit, once again set `INSTALL` to the same as in the previous file. In addition, if there are any other dependencies for your build of EPICS and synApps, add them here. For example, to auto-build the ADUVC driver, libuvc must be built, so I added a condition for building and installing libuvc.

From here, you are ready to run the script, and this is done simply by running:
```
./installSynApps.sh
```
from the /scripts directory. Note that you will be prompted for a sudo password to install the dependency packages. Once the script completes, a new directory `autogenerated` is created, and `install.sh` and `uninstall.sh` files are placed within each. Run the appropriate file to uninstall or recompile the packages appropriately. This should simplify building the same sources on multiple operating systems.