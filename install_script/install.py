from os import path
import subprocess

def edit_env_file():
  subprocess.run(["nano", ".env"])

while True:
  print("Welcome to Mounit")
  print("Please select an option:")
  print("1. Enter Discord Bot token, Discord admin ID, channel ID, and NEWS_API_KEY")
  print("2. Install required packages")
  print("3. Run Mounit in a screen")
  print("3b. Re-attach Mounit screen")
  print("4. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    if path.exists(".env"):
      choice = input(".env file already exists. Do you want to inspect it with nano? (y/n) ")

      if choice in ("y", "Y"):
        edit_env_file()
      else:
        pass
    else:
      discord_bot_token = input("Enter Discord Bot token: ")
      discord_admin_id = input("Enter Discord admin ID: ")
      channel_id = input("Enter channel ID: ")
      news_api_key = input("Enter NEWS_API_KEY: ")

      with open(".env", "w") as file:
        file.write(f"TOKEN={discord_bot_token}\n")
        file.write(f"ADMINID={discord_admin_id}\n")
        file.write(f"CHANNELID={channel_id}\n")
        file.write(f"NEWS_API_KEY={news_api_key}\n")
  elif choice == "2":
    subprocess.run(["pip3", "install", "-U", "discord"])
    subprocess.run(["pip3", "install", "-U", "discord.py"])
    subprocess.run(["pip3", "install", "-U", "python-dotenv"])
    subprocess.run(["pip3", "install", "-U", "aiohttp"])
    subprocess.run(["pip3", "install", "-U", "beautifulsoup4"])
  elif choice == "3":
    if path.exists("mounit.py"):
      subprocess.run(["screen", "-X", "-S", "mounit", "kill"])
      subprocess.run(["screen", "-S", "mounit", "-d", "-m", "python3", "mounit.py"])
      subprocess.run(["screen", "-r", "mounit"])
    else:
      print("Unable to find mounit.py. Please run the script in the same folder as mounit.py.")
  elif choice == "3b":
      subprocess.run(["screen", "-r", "mounit"])
  elif choice == "4":
    break
  else:
    print("Invalid choice. Please try again.")
