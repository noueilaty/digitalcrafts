# You are responsible for creating a TODO list app. Here are the requested features for the TODO list app:
#
# - User should be able to add task by adding the title of the task
# - User should be able to view all the tasks
# - User should be able to remove the tasks
# - User should be able to quit the app when "q" is pressed
#
# HARD MODE:
# - User should be able to enter priority of the task
# - User should be able to sort the tasks based on priority

print("--TODO List App--")

class TODO(object):
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self):
        print('Enter the task you\'d like to add:')
        task_to_add = raw_input('> ')
        is_priority = raw_input('Is this task a priortiy? (y/n) > ')
        if is_priority == 'y':
            self.tasks.append('! {}'.format(task_to_add))
        else:
            self.tasks.append(task_to_add)

    def view_tasks(self):
        print('Here\'s the list of tasks:')
        print('{}'.format(self.title))
        counter = 1
        for task in self.tasks:
            print('{0}. {1}\n'.format(counter, task))
            counter += 1
        print("Note: '!' denotes a priority task")

    def remove_task(self):
        self.view_tasks()
        remove_index = raw_input('Enter the task number you want to remove >')
        del self.tasks[int(remove_index) + -1]
        print('Deleted task #{}.'.format(remove_index))

todo_list = TODO('Today\'s TODO List')

while True:
    try:
        print('\nWhat would you like TODO?')

    except:
        print("Error")

    print("-Press 'a' to add a task.\n-Press 'v' to view tasks.\n-Press 'r' to remove a task. \n-Press 'q' to quit.")
    choice = raw_input('> ')
    if choice == 'a':
        todo_list.add_task()
    elif choice == 'v':
        todo_list.view_tasks()
    elif choice == 'r':
        todo_list.remove_task()
    elif choice == "q":
        print('Quitting the program')
        break
    else:
        print('{} is an invalid command.'.format(choice))
