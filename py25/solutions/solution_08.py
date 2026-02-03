from math import sqrt

class Circuit:
    def __init__(self, id):
        self.id = id
        self.size = 0
        self.junction_boxes = []
        self.connections = []
    def get_id(self):
        return self.id
    def get_junction_boxes(self):
        return self.junction_boxes
    def _add_junction_box(self, junction_box_id):
        if junction_box_id not in self.junction_boxes:
            self.junction_boxes.append(junction_box_id)
            self.size += 1
    def get_size(self):
        return self.size
    def _contains_junction_box(self, junction_box_id):
        return junction_box_id in self.junction_boxes
    def get_connections(self):
        return self.connections
    def add_connection(self, junction_a, junction_b):
        if self._contains_junction_box(junction_a) and self._contains_junction_box(junction_b):
            return
        self.connections.append((junction_a, junction_b))
        self._add_junction_box(junction_a)
        self._add_junction_box(junction_b)
    def join(self, other_circuit):
        for conn in other_circuit.connections:
            self.add_connection(conn[0], conn[1])

class JunctionBox:
    def __init__(self, x, y, z, id):
        self.id = id
        self.circuit_id = None
        self.pos = (x, y, z)
    def get_id(self):
        return self.id
    def _get_position(self):
        return self.pos
    def _get_circuit_id(self):
        return self.circuit_id
    def _set_circuit(self, circuit):
        self.circuit_id = circuit.get_id()
    def _is_same_circuit(self, other_box):
        if self.circuit_id and other_box._get_circuit_id():
            return self.circuit_id == other_box._get_circuit_id()
        return False
    def get_distance(self, other_box):
        x1, y1, z1 = self.pos
        x2, y2, z2 = other_box._get_position()
        return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    def connect(self, other_box, boxes, circuits):
        if self.circuit_id == None:
            if other_box._get_circuit_id() == None:
                new_circuit = Circuit(self.id)
                self._set_circuit(new_circuit)
                other_box._set_circuit(new_circuit)
                new_circuit.add_connection(self.id, other_box.id)
                circuits[new_circuit.id] = new_circuit
            else:
                other_circuit = circuits[other_box._get_circuit_id()]
                self._set_circuit(other_circuit)
                other_circuit.add_connection(self.id, other_box.id)
        else:
            self_circuit = circuits[self.circuit_id]
            if other_box._get_circuit_id() == None:
                other_box._set_circuit(self_circuit)
                self_circuit.add_connection(self.id, other_box.id)
            else:
                if self_circuit.get_id() == other_box._get_circuit_id():
                    return False
                old_circuit_id = other_box._get_circuit_id()
                # Merge circuits
                other_circuit = circuits[old_circuit_id]
                self_circuit.add_connection(self.id, other_box.id)
                self_circuit.join(other_circuit)
                for jb_id in other_circuit.get_junction_boxes():
                    jb = boxes[jb_id]
                    jb._set_circuit(self_circuit)
                del circuits[old_circuit_id]
        return True

def read_input(filename):
    boxes = []
    with open(filename, 'r') as file:
        for id, line in enumerate(file):
            parts = line.strip().split(',')
            box = JunctionBox(int(parts[0]), int(parts[1]), int(parts[2]), id)
            boxes.append(box)
    return boxes

def bin_search(sorted_distances, target):
    low = 0
    high = len(sorted_distances) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_distances[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

def sorted_add(sorted_distances, new_distance):
    index = bin_search(sorted_distances, new_distance[0])
    sorted_distances.insert(index, new_distance)

def sort_n_smallest_distances(boxes, limit):
    box_pairs = []
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            dist = boxes[i].get_distance(boxes[j])
            if len(box_pairs) < limit:
                sorted_add(box_pairs, (dist, i, j))
            else:
                if dist < box_pairs[-1][0]:
                    box_pairs.pop()
                    sorted_add(box_pairs, (dist, i, j))
    return box_pairs

def solve_a(filename, limit):
    boxes = read_input(filename)
    circuits = {}
    box_pairs = sort_n_smallest_distances(boxes, limit)
    for _, i, j in box_pairs:
        box_a = boxes[i]
        box_b = boxes[j]
        _= box_a.connect(box_b, boxes, circuits)
    sizes = sorted([circuit.get_size() for circuit in circuits.values()])
    return sizes[-1] * sizes[-2] * sizes[-3] if len(sizes) >= 3 else 0

def solve_b(filename, limit):
    boxes = read_input(filename)
    circuits = {}
    box_pairs = sort_n_smallest_distances(boxes, limit)
    for _, i, j in box_pairs:
        box_a = boxes[i]
        box_b = boxes[j]
        _= box_a.connect(box_b, boxes, circuits)
        if len(circuits) == 1 and circuits[list(circuits.keys())[0]].get_size() == len(boxes):
            return box_a._get_position()[0] * box_b._get_position()[0]
    print("Warning: Not all boxes connected within limit.")
    return -1

if __name__ == "__main__":
    print("A) Product of sizes of largest circuits:", solve_a('inputs/input_08.txt', 1000))
    print("B) Product of coordinates of last connected boxes:", solve_b('inputs/input_08.txt', 10000))