class Course:
    def __init__(self, department, number, title):
        self.department = department
        self.number = number
        self.title = title


class CSCourse(Course):
    def __init__(self, department, number, title, recorded=False):
        super().__init__(department, number, title)
        self.is_recorded = recorded


# type(a)
#     #<class 'courses.Course'>
# isinstance(a, Course)
#     #True
# isinstance(b, Course)
#     #True
# type(a) == type(b)
#     #False
# a == b
#     #False



#
#Simple Graph
#

class Vertex:
    def __init__(self, name="", edges={}):
        self.name = name
        self.edges = set(edges)

class Edge:
    def __init__(self, start, end, cost=1, visited=False):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = visited

class SimpleGraph:
    def __init__(self, verts={}, edges=[]):
        self.verts = set(verts)
        self.edges = edges

    def add_vertex(self, v):
        if type(v) is Vertex:
            self.verts.add(v)
        else:
            print("To nie jest wierzchołek!")

    def add_edge(self, v_1, v_2):
        if type(v_1) and type(v_2) is Vertex:
            if self.verts.__contains__(v_1) and self.verts.__contains__(v_2) is True:
                self.edges.append(Edge(v_1, v_2))
            else:
                if self.verts.__contains__(v_1) is True:
                    self.add_vertex(v_2)
                else:
                    self.verts.__contains__(v_1)
            self.edges.append(Edge(v_1, v_2))
        else:
            print("To nie wierzchołek!")

    def contains_vertex(self, v):
        if type(v) is Vertex:
            return self.verts.__contains__(v)
        else:
            print("To nie wierzchołek!")

    def contains_edge(self, v_1, v_2):
        if type(v_1) and type(v_2) is Vertex:
            for x in self.edges:
                if x.start == v_1 and x.end == v_2:
                    return True
            return False
        else:
            print("To nie wierzchołek!")

    def get_neighbors(self, v):
        ngbh = []
        if type(v) is Vertex:
            for x in self.edges:
                if x.start == v:
                    ngbh.append(x.end.name)
                elif x.end == v:
                    ngbh.append(x.start.name)
            return ngbh
        else:
            print("To nie wierzchołek!")

    def is_empty(self):
        if self.edges.__len__() and self.verts.__len__() is 0:
            return True
        else:
            return False

    def size(self):
        return self.verts.__len__()

    def remove_vertex(self, v):
        if type(v) is Vertex:
            if self.verts.__contains__(v):
                self.verts.remove(v)
                for x in self.edges:
                    if x.start or x.end == v:
                        self.edges.remove(x)
        else:
            print("To nie wierzchołek!")

    def remove_edge(self, v_1, v_2):
        if type(v_1) and type(v_2) is Vertex:
            for x in self.edges:
                if x.start == v_1 and x.end == v_2:
                    self.edges.remove(x)
        else:
            print("To nie wierzchołek!")

    def is_neighbor(self, v1, v2):
        if type(v1) and type(v2) is Vertex:
            for x in self.edges:
                if x.start == v1 and x.end == v2:
                    return True
                elif x.end == v1 and x.start == v2:
                    return True
            return False
        else:
            print("To nie wierzchołek!")

    def is_reachable(self, v1, v2):
        for x in self.edges:
            if x.start == v1:
                if x.start == v1 and x.end == v2:
                    print("znaleziono połączenie")
                    return True
                else:
                    print("wejscie do petli:","x",x.start.name,"v2",v2.name,"x.end",x.end.name)
                    self.is_reachable(x.end, v2)


    def clear_all(self):
        self.edges.clear()
        self.verts.clear()

sg = SimpleGraph()
pustygraf = SimpleGraph()
vt = Vertex("xp")
vz = Vertex()
x = Vertex()
sg.add_vertex(vt)
sg.add_edge(vt, vz)
print(sg.contains_edge(vt, vz))
print(sg.contains_vertex(x))
print(sg.get_neighbors(vz))
print(sg.is_empty())
print(pustygraf.is_empty())
print(sg.size())
sg.remove_vertex(vz)
print(sg.size())
sg.remove_vertex(vt)
print(sg.size())
sg.add_vertex(vt)
sg.add_edge(vt, vz)

print(sg.contains_edge(vt, vz))
sg.remove_edge(vt, vz)
print(sg.contains_edge(vt, vz))
sg.add_edge(vt, vz)
print(sg.contains_edge(vt, vz))
print(sg.is_neighbor(vt, vz))

sg.clear_all()
a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")
f = Vertex("f")

sg.add_edge(a,b)
sg.add_edge(b,c)
sg.add_edge(b,f)
sg.add_edge(c,d)
sg.add_edge(c,e)

print("----------------")
print(sg.is_reachable(a,f))



###############


class Transportation:
    wheels = 0

    def __init__(self):
        self.wheels = -1

    def travel_one(self):
        print("Travelling on generic transportation")

    def travel(self, distance):
        for _ in range(distance):
            self.travel_one()

    def is_auto(self):
        return self.wheels == 4

class Bike(Transportation):

    def travel_one(self):
        print("Biking one mile")

class Car(Transportation):
    wheels = 4

    def travel_one(self):
        print("Driving one mile")

    def make_sound(self):
        print("VROOM")

class Ferrari(Car):
    pass

t = Transportation()
b = Bike()
c = Car()
f = Ferrari()


isinstance(t, Transportation)

isinstance(b, Bike)
isinstance(b, Transportation)
isinstance(b, Car)
#isinstance(b, t) isinstance() arg 2 must be a type or tuple of types

isinstance(c, Car)
isinstance(c, Transportation)

isinstance(f, Ferrari)
isinstance(f, Car)
isinstance(f, Transportation)

issubclass(Bike, Transportation)
issubclass(Car, Transportation)
issubclass(Ferrari, Car)
issubclass(Ferrari, Transportation)
issubclass(Transportation, Transportation)

b.travel(5)
print(c.is_auto())
print(f.is_auto())
print(b.is_auto())
#b.make_sound()  'Bike' object has no attribute 'make_sound'
c.travel(10)
print("------------------------------")
f.travel(4)






###
#Exceptions
###



class OutOfRangeError(ValueError):
    pass

def get_age():
    while True:
        try:
            age = input("How old are you?")
            if age.isdigit() and int(age) in range(0, 123):
                print(age)
            else:
                raise OutOfRangeError
        except OutOfRangeError:
            print("Invalid integer input.")
        else:
            print("Valid input.")
            break

get_age()
