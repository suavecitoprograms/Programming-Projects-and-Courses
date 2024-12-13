# Write your solution here:
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
    
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)