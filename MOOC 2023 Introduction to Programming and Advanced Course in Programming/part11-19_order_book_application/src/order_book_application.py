# Write your solution here
class OrderBookApplication():
    def __init__(self) -> None:
        self.__orderbook = OrderBook()
    
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        print()
    
    def error_handle(self):
        print("erroneous input")
        
    def add_order(self):
        description = input("description: ")
        info = input("programmer and workload estimate: ")
        info = info.split()
        
        if len(info) != 2:
            self.error_handle()
            return
        
        programmer, workload = tuple(info)
        
        try:
            int(workload)
        except:
            self.error_handle()
            return

        self.__orderbook.add_order(description, programmer, int(workload))
        print("added!")

    def finished_tasks(self):
        finished_orders = self.__orderbook.finished_orders()
        if finished_orders:
            for order in finished_orders:
                print(order)
        else:
            print("no finished tasks")
    
    def unfinished_tasks(self):
        unfinished_orders = self.__orderbook.unfinished_orders()
        if unfinished_orders:
            for order in unfinished_orders:
                print(order)
        else:
            print("no unfinished tasks")
    
    def mark_finished(self):
        id = input("id: ")
        
        try:
            int(id)
        except:
            self.error_handle()
            return
        
        try:
            self.__orderbook.mark_finished(int(id))
        except:
            self.error_handle()
            return

        print("marked as finished")
    
    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            finished, unfinished, f_workload, u_workload = self.__orderbook.status_of_programmer(programmer)
        except:
            self.error_handle()
            return
        print(f"tasks: finished {finished} not finished {unfinished}, hours: done {f_workload} scheduled {u_workload}")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            
            if command == "1": ## add order
                self.add_order()
            elif command == "2":
                self.finished_tasks()
            elif command == "3":
                self.unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()
            elif command == "0":
                print("goodbye!")
                break
            else:
                print(f"no such commands exists!")
            print()
            

# If you use the classes made in the previous exercise, copy them here
class Task():
    id = 0
    @classmethod
    def new_id(cls):
        Task.id += 1
        return Task.id #increment by 1 the new id for next person
    
    def __init__(self, description:str, programmer:str, workload:int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = False
        self.id = Task.new_id() #refer to class method
        
    def is_finished(self):
        return self.status 
    
    def mark_finished(self):
        self.status = True
        
    def __str__(self) -> str:
        status = "FINISHED" if self.status else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
    
class OrderBook():
    def __init__(self) -> None:
        self.__orderbook = {}
    
    def add_order(self, description:str, programmer:str, workload:int):
        task = Task(description, programmer, workload)
        self.__orderbook[task.id] = task
    
    def all_orders(self):
        return [task for task in self.__orderbook.values()]

    def programmers(self):
        return list(set([task.programmer for task in self.all_orders()]))
    
    def mark_finished(self, id: int):
        try:
            self.__orderbook[id]
        except:
            raise ValueError(f"There are no tasks with the id:{id}")
        return self.__orderbook[id].mark_finished()
    
    def finished_orders(self):
        return [task for task in self.all_orders() if task.status]
    
    def unfinished_orders(self):
        return [task for task in self.all_orders() if not task.status]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f"There is no programmer in the orderbook with the name: {programmer}")
        programmer_tasks = [task for task in self.all_orders() if task.programmer == programmer]
        
        unfinished = [task for task in self.all_orders() if task.programmer == programmer and not task.status]
        u_workload = sum(task.workload for task in unfinished)
        
        finished = [task for task in self.all_orders() if task.programmer == programmer and task.status]
        f_workload = sum(task.workload for task in finished)
  
        return (len(finished), len(unfinished), f_workload, u_workload)
    
application = OrderBookApplication()
application.execute()