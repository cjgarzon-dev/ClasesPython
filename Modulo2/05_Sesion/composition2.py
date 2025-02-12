class Employee:
    def __init__(self, name):
        self.name = name
        self.works = []
    
    def assignWork(self, work):
        self.works.append(work)
    
    def realiceWork(self):
        print(f'{self.name} esta desarrollando las siguientes tareas: ')
        for work in self.works:
            print(f'- {work.execute()}')
        
class Work:
    def __init__(self):
        pass
    
    def execute(self):
        pass

class ProjectWork(Work):
    def __init__(self):
        pass
    
    def execute(self):
        return 'Trabajando en un proyecto'

class Capacitation(Work):
    def __init__(self):
        pass
    
    def execute(self):
        return 'Tomando una capacitación'

class Evaluation(Work):
    def __init__(self):
        pass
    
    def execute(self):
        return 'Realizando una evaluación'

project1 = ProjectWork()
capacitation1 = Capacitation()
evaluation1 = Evaluation()

employee1 = Employee('Pepe')
employee1.assignWork(project1)
employee1.assignWork(capacitation1)
employee1.assignWork(evaluation1)

employee1.realiceWork()