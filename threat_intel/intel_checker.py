def is_malicious(ip):

    try:

        with open(
            "threat_intel/malicious_ips.txt",
            "r"
        ) as file:

            malicious_ips = file.read().splitlines()

        return ip in malicious_ips

    except:

        return False
