class ToDoList(object):
    def __init__(self, title):
        self.title = title

    def add_task(self):
        print('Enter the task you\'d like to add:')
        task_to_add = raw_input('> ')
        with open('todos.txt', 'a') as file_object:
            file_object.write(task_to_add)
            file_object.write('\n')

    def view_tasks(self):
        print('Here\'s the list of tasks:')
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)

    # remove_task is still in progress:
    def remove_task(self):
        task_to_remove = raw_input('Enter type task you want to remove > ')
        with open(filename, 'r') as input:
            with open(filename, 'wb') as output:
                for line in input:
                    if line != task_to_remove + '\n':
                        filename.write(line)
        print('Deleted task : {}.'.format(task_to_remove))

todo_list = ToDoList('Today\'s TODO List')
filename = 'todos.txt'

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
