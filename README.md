# hack-program

The module and package snake returns a yes or no depending if the date today is the anniversary of the nokia game SNAKES released in 2005.
The first two options tells the same thing with different print statements. The options are there just to demonstrate the parse argument functionality. The third option
--celeb is the one that utilizes pandas.
The repo contains an init file and setup for it to be installed as a module and call functions between each other. 
Finally, if no options is entered in the command line, the system will prompt the user to choose 1.
Error-handling only if user inputs both options.



usage: snake [-h] [--today] [--yet] [--celeb]

optional arguments:
  -h, --help  show this help message and exit
  --today     print if today is the anniversay of snakes game
  --yet       print if it is the anniversay of snakes game yet
  --celeb     Asks for a sample size and returns a dataframe of celebrities and their relation to Snake

