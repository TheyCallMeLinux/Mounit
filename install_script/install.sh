edit_env_file() {
  # Open .env file with nano
  nano .env
}

while true; do
  # Welcome menu
  echo "Welcome to Mounit"
  echo "Please select an option:"
  echo "1. Enter Discord Bot token, Discord admin ID, channel ID, and NEWS_API_KEY"
  echo "2. Install required packages"
  echo "3. Run Mounit in a screen"
  echo "3b. Re-attach Mounit screen"
  echo "4. Exit"

  # Read user input
  read -p "Enter your choice: " choice

  case $choice in
    1)  # Check if .env file exists
        if ls .env > /dev/null 2>&1; then
          # .env file exists, ask user if they want to inspect it
          read -p ".env file already exists. Do you want to inspect it with nano? (y/n) " choice

          case $choice in
            y|Y)  # Edit .env file
                  edit_env_file
                  # Return to main menu
                  break
                  ;;
            n|N)  # Do not edit .env file
                  ;;
            *)  # Invalid input
                echo "Invalid choice. Please try again."
                ;;
          esac
        fi

        # Ask user for input
        read -p "Enter Discord Bot token: " discord_bot_token
        read -p "Enter Discord admin ID: " discord_admin_id
        read -p "Enter channel ID: " channel_id
        read -p "Enter NEWS_API_KEY: " news_api_key

        # Save input to .env file
        echo "TOKEN=$discord_bot_token" > .env
        echo "ADMINID=$discord_admin_id" >> .env
        echo "CHANNELID=$channel_id" >> .env
        echo "NEWS_API_KEY=$news_api_key" >> .env
        ;;
    2)  # Install required packages
        pip3 install -U discord
        pip3 install -U discord.py
        pip3 install -U python-dotenv
        pip3 install -U aiohttp
        pip3 install -U beautifulsoup4
        ;;
    3)  # Check if mounit.py is present in the current folder
        if ls mounit.py > /dev/null 2>&1; then
          # Kill the existing 'mounit' screen, if any
          screen -X -S mounit kill
          # Run Mounit in a screen
          screen -S mounit -d -m python3 mounit.py
          screen -r mounit
        else
          # Prompt user to run the script in the same folder as mounit.py
          echo "Unable to find mounit.py. Please run the script in the same folder as mounit.py."
        fi
        ;;

    3b)  # Re-attach Mounit screen
        screen -r mounit
        ;;
    4)  # Exit
        exit 0
        ;;
    *)  # Invalid input
        echo "Invalid choice. Please try again."
        ;;
  esac
done
