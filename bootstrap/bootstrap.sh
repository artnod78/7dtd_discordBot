#!/bin/bash
VERSION=1

if [ `id -u` -ne 0 ]; then
	echo "This script has to be run as root!"
	exit 1
fi
RUNINSTALL=0
APTDEPENDENCIES="python3 python3-pip"
PIPDEPENDENCIES="discord lxml requests"
if [ -n "$(command -v apt-get)" ]; then
	ISDEBIAN=1
else
	ISDEBIAN=0
fi

showHelp() {
	echo "7dtd Discord Bot bootstrapper version $VERSION"
	echo
	echo "Usage: ./bootstrap.sh [-h] -i"
	echo "Parameters:"
	echo "  -h   Print this help screen and exit"
	echo "  -i   Required to actually start the installation"
}

intro() {
	echo
	echo "7dtd Discord Bot bootstrapper"
	echo
	echo "This will install a 7dtd Discord Bot according to the information"
	echo "given on:"
	echo "   https://github.com/artnod78/7dtd_discordBot"
	echo
	read -p "Press enter to continue"
	echo -e "\n=============================================================\n"
}

nonDebianWarning() {
	if [ $ISDEBIAN -eq 0 ]; then
		echo "NOTE: It seems like this system is not based on Debian."
		echo "Although installation of the scripts"
		echo "will work the bot scripts will probably"
		echo "fail because of missing dependencies. Make sure you check"
		echo "the website regarding the prerequisites"
		echo "(https://github.com/artnod78/7dtd_discordBot)."
		echo
		echo "Do you want to continue anyway?"
		select yn in "Yes" "No"; do
			case $yn in
				Yes)
					echo "Continuing..."
					break;;
				No)
					echo "Aborting."
					exit 0
					;;
			esac
		done
		echo -e "\n=============================================================\n"
	fi
}

installAptDeps() {
	echo -e "Installing dependencies\n"
	apt-get update -y
	apt-get install -y $APTDEPENDENCIES
	echo -e "\n=============================================================\n"
}

installPipDeps() {
	echo -e "Installing optional dependencies\n"
	pip3 install $PIPDEPENDENCIES
	echo -e "\n=============================================================\n"
}

checkSetupDeps() {
	for DEP in screen python3 python3-pip; do
		which $DEP > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "\"$DEP\" not installed. Please install it and run this script again."
			exit 1
		fi
	done
	
}

check7dtdDeps() {
	if [ ! -d /usr/local/lib/7dtd ]; then
		echo "7dtd Linux management script not installed."
		echo "Please install it (https://7dtd.illy.bz/)"
		exit 1
	fi
}

installBotScripts() {
	echo -e "Downloading and installing bot scripts"
	echo "  - Download scripts"
	wget -nv -q --show-progress https://github.com/artnod78/7dtd_discordBot/archive/master.zip -O /tmp/DiscordBot.zip

	echo "  - Extract scripts"
	TMPPATH=`mktemp -d`
	unzip -q /tmp/DiscordBot.zip -d $TMPPATH
	cp -R $TMPPATH/7dtd_discordBot-master/scripts/* /

	chown root.root /usr/local/bin/sdtdbot/discord_bot.py
	chmod 0755 /usr/local/bin/sdtdbot/discord_bot.py
	chown root.root /etc/init.d/discord_bot
	chmod 0755 /etc/init.d/discord_bot
	
	chown root.root /usr/local/bin/sdtdbot/discord_hook.py
	chmod 0755 /usr/local/bin/sdtdbot/discord_hook.py
	chown root.root /etc/init.d/discord_hook
	chmod 0755 /etc/init.d/discord_hook

	rm -R $TMPPATH
	rm /tmp/DiscordBot.zip

	echo "  - Enable deamon"
	systemctl daemon-reload
	update-rc.d discord_bot defaults
	update-rc.d discord_hook defaults
	echo -e "\n=============================================================\n"
}

finish() {
	if [ $ISDEBIAN -eq 0 ]; then
		echo
		echo "You are not running a Debian based distribution."
		echo "The following things should manually be checked:"
		echo " - Existence of prerequsities"
		echo " - Running the init-script on boot"
	else
		echo -e "ALL DONE"
	fi

	echo
	echo -e "For further configuration options check:"
	echo -e "  /etc/lmm.conf"
	echo
	echo -e "For feedback, suggestions, problems please visit the github:"
	echo -e "  https://github.com/artnod78/7dtd_discordBot"
	echo
}

main() {
	intro
	nonDebianWarning
	check7dtdDeps
	if [ $ISDEBIAN -eq 1 ]; then
		installAptDeps
		installPipDeps
	else
		checkSetupDeps
	fi
	installBotScripts
	finish
}

if [ -z $1 ]; then
	showHelp
	exit 0
fi
while getopts "hcoi" opt; do
	case "$opt" in
		h)
			showHelp
			exit 0
			;;
		i)
			RUNINSTALL=1
			;;
	esac
done
if [ $RUNINSTALL -eq 1 ]; then
	main
fi