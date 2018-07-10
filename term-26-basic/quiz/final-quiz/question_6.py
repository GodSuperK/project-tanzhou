"""
filename = question_6.py
author = 孔德成
"""
class Person(object):

    def __init__(self, name, old, job):
        self.name = name
        self.old = old
        self.job = job
        
    def __call__(self):
        print("<{}: [name={}, old={}, job={}]>".format(
            self.__class__.__name__, self.name, self.old, self.job))
    
    def __del__(self):
        print("name={}, old={}".format(self.name, self.old))

def main():
    abu = Person('abu', 20, 'programmer')
    abu()
    # del abu


if __name__ == "__main__":
    main()


