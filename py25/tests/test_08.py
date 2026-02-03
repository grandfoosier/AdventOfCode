from ..solutions import solution_08

def test_read_input():
    boxes = solution_08.read_input('test_inputs/test_input_08.txt')
    expected_count = 20
    assert len(boxes) == expected_count
    assert boxes[0]._get_position() == (162, 817, 812)
    assert boxes[-1]._get_position() == (425, 690, 689)

def test_junction_box_methods():
    boxes, circuits = [], {}
    box1 = solution_08.JunctionBox(0, 0, 0, 0)
    boxes.append(box1)
    box2 = solution_08.JunctionBox(3, 4, 5, 1)
    boxes.append(box2)
    assert box1.get_id() == 0
    assert box2.get_id() == 1
    assert box1._get_position() == (0, 0, 0)
    assert box2._get_position() == (3, 4, 5)
    assert box1.get_distance(box2) == 7.0710678118654755
    assert box1._get_circuit_id() is None
    assert box2._get_circuit_id() is None

    success = box1.connect(box2, boxes, circuits)
    assert success == True
    assert box1._get_circuit_id() == box1.get_id()
    assert box1._get_circuit_id() == box2._get_circuit_id()
    box1._set_circuit(solution_08.Circuit(1))
    assert box1._get_circuit_id() != box2._get_circuit_id()
    box1._set_circuit(circuits[0])

    box3 = solution_08.JunctionBox(10, 10, 10, 2)
    boxes.append(box3)
    success = box2.connect(box3, boxes, circuits)
    assert success == True
    assert box2._get_circuit_id() == box3._get_circuit_id()
    assert box3._get_circuit_id() == box1._get_circuit_id()
    success = box3.connect(box1, boxes, circuits)
    assert success == False

    box4 = solution_08.JunctionBox(20, 20, 20, 3)
    boxes.append(box4)
    box5 = solution_08.JunctionBox(30, 30, 30, 4)
    boxes.append(box5)
    success = box4.connect(box5, boxes, circuits)
    assert success == True
    assert box4._get_circuit_id() != box1._get_circuit_id()

    success = box2.connect(box4, boxes, circuits)
    assert success == True
    assert box5._get_circuit_id() == box1._get_circuit_id()

    box6 = solution_08.JunctionBox(100, 100, 100, 5)
    boxes.append(box6)
    box7 = solution_08.JunctionBox(200, 200, 200, 6)
    boxes.append(box7)
    box6.connect(box7, boxes, circuits)
    assert box6._get_circuit_id() != box1._get_circuit_id()
    assert len(circuits) == 2

# def test_circuit_methods():
#     box

def test_bin_search():
    sorted_distances = [[1], [3], [5], [7], [9], [11], [13]]
    assert solution_08.bin_search(sorted_distances, 7) == 3
    assert solution_08.bin_search(sorted_distances, 1) == 0
    assert solution_08.bin_search(sorted_distances, 13) == 6
    assert solution_08.bin_search(sorted_distances, 4) == 2

def test_sorted_add():
    sorted_list = [[2], [4], [6], [8]]
    solution_08.sorted_add(sorted_list, [5])
    assert sorted_list == [[2], [4], [5], [6], [8]]
    solution_08.sorted_add(sorted_list, [1])
    assert sorted_list == [[1], [2], [4], [5], [6], [8]]
    solution_08.sorted_add(sorted_list, [9])
    assert sorted_list == [[1], [2], [4], [5], [6], [8], [9]]

def test_sort_n_smallest_distances():
    box1 = solution_08.JunctionBox(0, 0, 0, 0)
    box2 = solution_08.JunctionBox(1, 1, 1, 1)
    box3 = solution_08.JunctionBox(2, 2, 3, 2)
    box4 = solution_08.JunctionBox(3, 3, 6, 3)
    boxes = [box1, box2, box3, box4]
    smallest_distances = solution_08.sort_n_smallest_distances(boxes, 3)
    assert len(smallest_distances) == 3
    assert smallest_distances[0][1:] == (0, 1)  # box1 to box2
    assert smallest_distances[1][1:] == (1, 2)  # box2 to box3
    assert smallest_distances[2][1:] == (2, 3)  # box3 to box4

def test_solve_a():
    solution_a = solution_08.solve_a('test_inputs/test_input_08.txt', 10)
    expected_a = 40
    assert solution_a == expected_a

def test_solve_b():
    solution_b = solution_08.solve_b('test_inputs/test_input_08.txt', 200)
    expected_b = 216 * 117  # x-coordinates of last connected boxes in test input
    assert solution_b == expected_b