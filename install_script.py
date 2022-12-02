import paramiko


pvt_key = "//Users/abprusty/.aws/Abinash_us_east_1.pem"
host = "3.237.11.159"
username = "ec2-user"
versions = ["14.11.15"]

def execute_script(script, host, username, pvt_key):

    key  = paramiko.RSAKey.from_private_key_file(pvt_key)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Connecting to the host {host}")
    try:
        client.connect(hostname=host, username=username, pkey=key)
        print('Host Connected Succefully')
    except Exception as e:
        print("###########################  Exception Occured ###########################")
        print(f"There is an error while connecting the host {host} \n {e}")
        

    stdin, stdout, stderr = client.exec_command(script)
    print("############################ Execution Output ###########################")
    print(stdout.read())

    if stderr:
        print("########################## Error in Exectuion of script on host #######################################")
        print(stderr.read())
    client.close()

def replace_all(file, dic):
    with open(file) as f:
        file_data = f.read()

    for i, j in dic.items():
        file_data = file_data.replace(i, j)
    return file_data



for v in versions:
    tag_replace_dict = {
        "@@@@chef-version@@@@": v
    }

    config_script = replace_all ("script_exec.sh", tag_replace_dict)

    execute_script(config_script, host, username, pvt_key )


