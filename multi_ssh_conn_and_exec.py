import os
"""
multi_ssh_conn_and_exec

script given below create the stable connection via scp(ssh) protocol(with the use of key authentication) and after that
perform the script.sh on-site, for example - with preparing the work environment after installation of the system

the server given as parameter, for the better security should have the enabled key auth as the only auth option
for the connections on ssh sessions

private key file and script file must be putted inside catalogue of the script

"""




def multi_ssh_conn_and_exec(ip_addr, user, priv_key, file):
    os.system('scp -i '+priv_key+' '+file+' '+user+'@'+ip_addr+':/tmp/')
    os.system('ssh '+user+'@'+ip_addr+' -i '+priv_key+' " sudo chmod +x /tmp/'+file+' | sh -x /tmp/'+file+'"')



multi_ssh_conn_and_exec('sample ip address', 'user', 'private key file', 'script file')