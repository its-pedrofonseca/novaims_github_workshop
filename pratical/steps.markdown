# Pratical steps

Open the terminal on your code editor and make sure you have git installed.
You can check it by running the command:
`git --version`

Run the command
`git config --list`

You probably going to be stuck in the terminal with ":    "
Just press 'q'.

Depending on the settings you have, check if you have the user.name and user.email configured.
If not, run the following commands:

`git config --global user.name "<your_name>"`
`git config --global user.email "<your_email_synced_to_git>"`


## Initial configuration

Then you can open a new window on your code editor, and select the pane for cloning a git repository
or you can run the command `git clone https://github.com/its-pedrofonseca/novaims_github_workshop.git`

On your terminal, just make sure you select a proper directory to store the code locally.
If any questions arise during this step call the instructor!


### 1st step:
Make sure you have the repository cloned and you are in the right directory.
You should be in the directory like:

 `../../novaims_github_workshop`


### 2nd step:
Now that you have cloned the repository and are in the right directory run the command:

`git pull origin`

Note: You should haven't changed no files until here.


### 3rd step:
Take some time to analyse the code and read the description.
Check the bottom left or right corner of your code editor and look for the branch you are currently on.
You should be on the main branch.

Change to the development branch by running the command:

`git checkout dev`


### 4th step:
Make sure you can run the exercise.py file, by running the command (according to the installed python version):

`python pratical/exercise.py`

or

`python3 pratical/exercise.py`

You should be able to see outputs until the breakpoint. You can now press CTRL + C to exit the breakpoint.


### 5th step:
Now that we have analysed the code and made sure we have python running as expected let's create a new branch!
You can do that by running the following command in the terminal:

`git checkout -b <name_of_branch>`

<name_of_branch> - the name of the branch typically implies some new development on the code.
Since we all are going to do the same try naming your branch something like <your_name>/remove_breakpoints.

Note: Check the bottom left or right corner of your code editor if the name you gave appears now instead of main.

You can check the the theory/2. git_branch.markdown file to check what this command is all about.
Normally, git directs to the newly created branch, but in case you are still not in the new branch, 
you can run the command:

`git checkout <name_of_branch>`


### 6th step
Now that we have created our working space, let's run the python file:

`python pratical/exercise.py`

or

`python3 pratical/exercise.py`

It should have popped out a window with a little exploratory analysis of the dataset.
You can close the window and...
Bummer! You should have stopped in the first breakpoint...

You can now write in the terminal:

cont - to proceed with the execution of the code.

Another graphic must have popped out! Close that window and write the command to continue the execution.
You can do that until the execution has finished!
The final print should be something like:

Movie: Monsters, Inc.
  Budget: $115,000,000
  Popularity: 106.815545
  Actual Revenue: $562,816,256.00
  Predicted Revenue: $676,482,764.73


### 7th step
Remove the lines that have:

`breakpoint()`


Extra points for using shortcuts! And execute the code again by running the command:

`python pratical/exercise.py`

or

`python3 pratical/exercise.py`

Smooth Sailing! The code ran without any interruption!


### 8th step
Since we have now removed all the breakpoints, it is time to add the file we have changed to the staging area.

We can now check in the source control for the files that were changed. For that check your source control tab on your code editor.

Now let's add a file to our staged changes. You can run the command:

`git add pratical/exercise.py`

We can now check in the source control for the files added to the staging area. It should only have one file!

In case you want to test and remove the file of the staging area try running the command: 

`git reset pratical/exercise.py`


### 9th step
Now that we have our files in the staging area, we can run the command to commit those files from local to our repository.

You can run the command:

`git commit -m "<message>"`

In the <message> body you should write a simple and descriptive text that reflect the changes made in the code.

### 10th step
Finally let's push these changes to the remote branch with the command:

`git push origin <name_of_branch>`

This command will probably pop out a window the request to enter your git password. If so, enter the password and if not, call the attention of the instructor!

### 11th step

To check the log of the repository workflow, you can try to run the command:

`git log`


or try these, whatever you like the most:

`git log --oneline` : Get a concise view of commits.

`git log --graph` : Visualize the commit tree.

`git log -p` : See the patch introduced by each commit.


Some of these commands will only exit if you press the key 'q'!


### 12th step
Let's open a Pull Request (PR). This part is very important, as it is where the code you just made joins the development branch and will be later move on to the main or production branch
To open a PR, go to the repository page on github.com and in the UI you should have a tab with "Pull Requests" - i'll guide you through.

1) Click on the tab of "Pull requests"
2) Click on the green button "New Pull Request"
3) On the grey bar you must select the source repository and the destination repository.
    Therefore you must select your branch <name_of_branch> as the compare (or source branch) 
    and the base (or destination repository) as the dev branch.
4) Add a short title in 3 to 5 words with the description of the changes you have made.
5) Add a one phrase description with the changes made.
6) Click on the green button "Create a Pull Request"


### 13th step 
Sit back and see what the instructor will be making next.

