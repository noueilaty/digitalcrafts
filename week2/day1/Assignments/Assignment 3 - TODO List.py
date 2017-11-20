# You are responsible for creating a TODO list app. Here are the requested features for the TODO list app:
#
# - User should be able to add task by adding the title of the task
# - User should be able to view all the tasks
# - User should be able to remove the tasks
# - User should be able to quit the app when "q" is pressed
#
#
#
# HARD MODE:
#
# - User should be able to enter priority of the task
# - User should be able to sort the tasks based on priority

while True:
    try:
        class TODO(object):
            def __init__(self):
                self.tasks = []

            def add_task(self, task):
                self.tasks.append(task)

            def view_tasks(self):
                print('Here\'s the list of tasks:')
                for task in self.tasks:
                    print('{}\n'.format(task))

            def remove_task():
                print('Removing task')

            def quit():
                print('Quitting the program')

    choice = raw_input("Press q to quit \nPress any other key to continue\n> ")
    if choice == "q":
        break

today = TODO()
