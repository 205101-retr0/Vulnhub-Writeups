## BACKDOOR USING SSH-KEYGEN

`ssh-keygen -f username`

This will give us two keys: 1 private key and 1 public key

permissions for the public key are 660.
permissions for the private key are 600.

Now we need to copy both private and public key to the user's /.ssh folder.

After that change the name of public key to authorized_keys. (((THIS ONE IS THE MOST IMPORTANT POINT TO WORK)))

And then login into the shell using `ssh -i id_rsa user@host -p456`.