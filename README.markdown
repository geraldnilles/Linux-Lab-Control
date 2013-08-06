Linux Lab Control
=================


# Goal
Use my Linux Lab PC to control and fetch data from my lab equipment.

# Progress

## Working
* Scope Screenshot and Identity

## ToDo
* Agilent PSU Control
* Proper Scope Reads without waiting for Timeout

# Interfaces

## GPIB
My PC is using a National Instruments PCI to GPIB adapter.  In order to get that working, i had to compile the linux-gpib kernel driver from source.  Asside from the standard build-essential packaage, i also needed to install gawk, flex, and bison before the compilation would work.

When completed, i saw 16 GPIB devices: /dev/gpib[0 to 15]

From there, i used the python bindings to talk to the devices

## USB
The Tek Scope i am using uses the USBTCM standard interface.  This driver for this is built into the linux kernel.

To Send/recv commands, simply use the echo/cat commands
	echo "*IDN?" > /dev/usbtmc0
	cat /dev/usbtmc0

## Permissions
In order to use this equipment as a non-root user, i had to change the udev rules.  Create a new rule file:

	vim /etc/udev/rules.d/70-gpib.rules

and add the following lines:

	KERNEL=="gpib[0-9]*", MODE="0666", GROUP="gpib"
	KERNEL=="usbtmc[0-9]*", MODE="0666", GROUP="gpib"

Now add your username to the gpib group
	sudo usermod -a -G gpib <username>
		
