from blocklist import *

if blocktime["start"] < dt.now() < blocktime["end"] or False :
    # to know our current mode
    print("Time to focus ...")

    # read the `host` file to check the list
    with open(hostpath, "r+") as file:
        content = file.read()

        for website in websitelist:
            # if your website is not in the `host` file, add the website
            if website not in content:
                with open(hostpath, "a") as writefile:
                    writefile.write(redirect + " " + website + "\n")

else:
    print("Enjoy your free time ...")

    # If the current time is not between working time, remove the websites
    with open(hostpath, "r+") as file:
        content = file.readlines()
        file.seek(0)

        for line in content:
            if not any(website in line for website in websitelist):
                file.write(line)
        # removing websites from the `host` file
        file.truncate()
