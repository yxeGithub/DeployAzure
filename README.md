# Original Repo is Pat's SE's, which I had as a private Repo, due to popular (maybe) demand I have opened it up so it can be more easily maintained, and hopefully others will contribute to making it more better (yes, I meant to say it that way, cause it will be a more better repo if other help me make it more better :) .)
To showcase Pat's SE's great talent for ..... stuff ?

you need ansible 2.5 - period, don't try with something lower than that.

You will need to edit and rename the /../../inventory/vault_azure_creds.sample and save it as ../../inventory/vault_azure_creds.yml

This is the file that will hold your Azure credentials that will allow you to pass these as variables that are needed for Azure tasks.

you will also need to edit the /DeployAzure/Vagrant/Vagrant/deployAzure/Vagrantfile and edit the $playbooks_path to be where you have your GitHub Repo.

I have removed the f5 specific modules from the ./library folder as it isn't needed anymore as ansible 2.5 has these - so far I don't need any custom modules.

To be done:

I should test without the Azure libraries as well, as they are likely in ansible 2.5.

Also need to finish the WebServer auto creation and should create two webservers, and maybe use a container for the second one.

Should clean up and add some real code to the f5-mgmt-config, it is pretty static and basic.
