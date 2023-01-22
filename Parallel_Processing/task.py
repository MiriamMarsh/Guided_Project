import multiprocessing
import time

def mutli_task(list, message_print):
      for task in list:
        print(message_print + " I'll do this task now: " + task)

list = ['Sweep the floor', 'Clean the windows', 'Soothe the baby', 'make lunch', 'put kinderlach to sleep', " laundry time",   "do HMWK" ,'supper time', 'pack ticks', 'get kinderlach ready for school']
start_first_tasks = multiprocessing.Process(target=mutli_task, args=[list[:5], '1st half completed!'])
start_second_tasks = multiprocessing.Process(target=mutli_task, args=[list[6:], '2nd half completed!'])

if __name__ == '__main__':
    start_first_tasks.start()
    start_second_tasks.start()

    start_first_tasks.join()
    start_second_tasks.join()    