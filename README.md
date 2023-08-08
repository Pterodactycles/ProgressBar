# ProgressBar
Simple progress bar for python.

Should be able to drop the ProgressBar folder directly into your site-packages folder. The location of this folder depends on your installation of python and how you are running it. To find this location, you should be able to run the command [^1]

> python -c "import site; print(site.getsitepackages()[0])"

in your terminal, and the output should show the path. Placing the ProgressBar folder directly into this folder should allow importing as usual:

> from ProgressBar.ProgressBar import ProgressBar

Should then be able to use as usual.

In the main folder, 'color-option-tester.py' is a script to show what colors / fonts / styles your terminal or console can display.
'example-progress-bar.py' is a script demonstrating the usage of the ProgressBar class.


[^1]: see [this stackoverflow qestion](https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory) for other tips for finding the location.
