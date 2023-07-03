import networkx as nx
import itertools

def NOT(value, dicti):
    if dicti.get(value) == 1:
        return 0
    else:
        return 1


def XOR(value1, value2, dicti):
    if dicti.get(value1) == dicti.get(value2):
        return 0
    else:
        return 1


def AND(value1, value2, dicti):
    if dicti.get(value1) == 1:
        if dicti.get(value2) == 1:
            return 1

    return 0


def OR(value1, value2, dicti):
    if dicti.get(value1) == 0:
        if dicti.get(value2) == 0:
            return 0
    return 1

# returns the list of input combinations corresponding to one iteration of the double for loop
def generate_binary_combinations(dict1):
    numbers_list = []
    for key in ['A', 'B', 'C', 'D']:
        numbers_list.append(dict1[key])
    binary_values = []

    for num in numbers_list:
        if num == 'X':
            binary_values.append([0, 1])
        else:
            binary_values.append([num])

    combination = list(itertools.product(*binary_values))
    return combination


def combine_dictionaries(dict1, dict2):
    result_dict = {}

    for key in ['A', 'B', 'C', 'D']:
        if dict1[key] == -1 or dict2[key] == -1:
            result_dict[key] = -1
        elif dict1[key] == 'X':
            result_dict[key] = dict2[key]
        elif dict2[key] == 'X':
            result_dict[key] = dict1[key]
        elif dict1[key] == dict2[key]:
            result_dict[key] = dict1[key]
        else:
            result_dict[key] = -1

    return result_dict


def call(required_value, graph, node_name, input_conditions):

    final_list = []
    if node_name in graph.nodes():
        operation = graph.nodes[node_name]
        if operation.get('expression') == '~':
            marker = 0
            inputs = input_conditions.copy()
            child = list(graph.successors(node_name))
            if child == "A":
                marker = 1
                if inputs.get('A') != required_value:
                    if inputs.get('A') == 'X':
                        inputs.update({'A': required_value})
                    elif inputs.get('A') == 1-required_value:
                        inputs.update({'A': -1})
            elif child == "B":
                marker = 1
                if inputs.get('B') != required_value:
                    if inputs.get('B') == 'X':
                        inputs.update({'B': required_value})
                    elif inputs.get('B') == 1-required_value:
                        inputs.update({'B': -1})
            elif child == "C":
                marker = 1
                if inputs.get('C') != required_value:
                    if inputs.get('C') == 'X':
                        inputs.update({'C': required_value})
                    elif inputs.get('C') == 1-required_value:
                        inputs.update({'C': -1})
            elif child == "D":
                marker = 1
                if inputs.get('D') != required_value:
                    if inputs.get('D') == 'X':
                        inputs.update({'D': required_value})
                    elif inputs.get('D') == 1-required_value:
                        inputs.update({'D': -1})
            else:
                final_list = call(1-required_value, graph, child[0], inputs).copy()
            if marker == 1:
                combinations = generate_binary_combinations(inputs)
                final_list += combinations
        else:

            for i in range(2):
                for j in range(2):
                    input_for_child1 = input_conditions.copy()
                    input_for_child2 = input_conditions.copy()
                    result = -1
                    if operation.get('expression') == "&":
                        result = i & j
                    elif operation.get('expression') == "|":
                        result = i | j
                    elif operation.get('expression') == "^":
                        result = i ^ j
                    if result == required_value:
                        children = list(graph.successors(node_name))

                        for index, child in enumerate(children, start=1):
                            if index == 1:
                                if child == "A":
                                    if input_for_child1.get('A') != i:
                                        if input_for_child1.get('A') == 'X':
                                            input_for_child1.update({'A': i})
                                        elif input_for_child1.get('A') == ~i:
                                            input_for_child1.update({'A': 'X'})
                                elif child == "B":
                                    if input_for_child1.get('B') != i:
                                        if input_for_child1.get('B') == 'X':
                                            input_for_child1.update({'B': i})
                                        elif input_for_child1.get('B') == ~i:
                                            input_for_child1.update({'B': 'X'})
                                elif child == "C":
                                    if input_for_child1.get('C') != i:
                                        if input_for_child1.get('C') == 'X':
                                            input_for_child1.update({'C': i})
                                        elif input_for_child1.get('C') == ~i:
                                            input_for_child1.update({'C': 'X'})
                                elif child == "D":
                                    if input_for_child1.get('D') != i:
                                        if input_for_child1.get('D') == 'X':
                                            input_for_child1.update({'D': i})
                                        elif input_for_child1.get('D') == ~i:
                                            input_for_child1.update({'D': 'X'})
                                else:
                                    call(i, graph, child, input_for_child1)
                            if index == 2:
                                if child == "A":
                                    if input_for_child2.get('A') != j:
                                        if input_for_child2.get('A') == 'X':
                                            input_for_child2.update({'A': j})
                                        elif input_for_child2.get('A') == ~j:
                                            input_for_child2.update({'A': 'X'})
                                elif child == "B":
                                    if input_for_child2.get('B') != j:
                                        if input_for_child2.get('B') == 'X':
                                            input_for_child2.update({'B': j})
                                        elif input_for_child2.get('B') == ~j:
                                            input_for_child2.update({'B': 'X'})
                                elif child == "C":
                                    if input_for_child2.get('C') != j:
                                        if input_for_child2.get('C') == 'X':
                                            input_for_child2.update({'C': j})
                                        elif input_for_child2.get('C') == ~j:
                                            input_for_child2.update({'C': 'X'})
                                elif child == "D":
                                    if input_for_child2.get('D') != j:
                                        if input_for_child2.get('D') == 'X':
                                            input_for_child2.update({'D': j})
                                        elif input_for_child2.get('D') == ~j:
                                            input_for_child2.update({'D': 'X'})
                                else:
                                    call(j, graph, child, input_for_child2)
                        final_from_here = combine_dictionaries(input_for_child1, input_for_child2)
                        combinations = generate_binary_combinations(final_from_here)
                        combinations = list(combinations)
                        final_list += combinations
    return final_list


def generate_bad_value(lines, dic, faulty_net, value_due_to_fault):
    value_due_to_fault = 1 - value_due_to_fault
    for line in lines:
        if line.strip() == "":
            continue
        else:
            lhs, rhs = line.split("=")
            lhs = lhs.strip()
            rhs = rhs.strip()
            if lhs != faulty_net:
                if '~' in rhs:
                    operator = 'NOT'
                    inputs = rhs.replace('~', '').strip()
                elif '&' in rhs:
                    operator = 'AND'
                    inputs = [input_node.strip() for input_node in rhs.split('&')]
                elif '|' in rhs:
                    operator = 'OR'
                    inputs = [input_node.strip() for input_node in rhs.split('|')]
                else:
                    operator = 'XOR'
                    inputs = [input_node.strip() for input_node in rhs.split('^')]
                dic[lhs] = operate(operator, inputs, dic)
            else:
                dic.update({faulty_net: value_due_to_fault})
    return dic["Z"]


def generate_good_value(lines, dic):
    for line in lines:
        if line.strip() == "":
            continue
        else:
            lhs, rhs = line.split("=")
            lhs = lhs.strip()
            rhs = rhs.strip()
            if '~' in rhs:
                operator = 'NOT'
                inputs = rhs.replace('~', '').strip()
            elif '&' in rhs:
                operator = 'AND'
                inputs = [input_node.strip() for input_node in rhs.split('&')]
            elif '|' in rhs:
                operator = 'OR'
                inputs = [input_node.strip() for input_node in rhs.split('|')]
            else:
                operator = 'XOR'
                inputs = [input_node.strip() for input_node in rhs.split('^')]
            update_it = operate(operator, inputs, dic)
            dic.update({lhs: update_it})
    return dic["Z"]


def operate(operator, inputs, dic):
    if operator == 'AND':
        return AND(inputs[0], inputs[1], dic)
    elif operator == 'OR':
        return OR(inputs[0], inputs[1], dic)
    elif operator == 'XOR':
        return XOR(inputs[0], inputs[1], dic)
    else:
        return NOT(inputs, dic)


# Read the circuit file and initialize a dictionery with four inputs
file = open("circuit.txt", "r")
content = file.read()
dic = {'A': '', 'B': '', 'C': '', 'D': ''}
file.close()

# Read the fault file
file = open("fault.txt", "r")
fault_file_content = file.read()
for read_line in fault_file_content.split("\n"):
    if read_line.strip() == "":
        continue
    LHS, RHS = read_line.split("=")
    LHS = LHS.strip()
    RHS = RHS.strip()
    if 'FAULT_AT' in LHS:
        faulty_node = RHS
    elif 'FAULT_TYPE' in LHS:
        if RHS == 'SA0':
            required_value = 1
        else:
            required_value = 0
file.close()

# A Graph in which each node is wire/net and stores the operation to be performed on its children
# It is a directed acyclic graph
G = nx.DiGraph()
test_vectors = []

lines = content.split("\n")

for line in lines:
    if line.strip() == "":
        continue

    lhs, rhs = line.split("=")

    lhs = lhs.strip()
    rhs = rhs.strip()
    dic.update({lhs: ''})
    G.add_node(lhs, expression=None)

    if "&" in rhs:
        G.add_node(lhs, expression="&")
        rhs1, rhs2 = rhs.split("&")
        rhs1 = rhs1.strip()
        rhs2 = rhs2.strip()
        G.add_node(rhs1)
        G.add_node(rhs2)
        G.add_edge(lhs, rhs1)
        G.add_edge(lhs, rhs2)
    if "|" in rhs:
        G.add_node(lhs, expression="|")
        rhs1, rhs2 = rhs.split("|")
        rhs1 = rhs1.strip()
        rhs2 = rhs2.strip()
        G.add_node(rhs1)
        G.add_node(rhs2)
        G.add_edge(lhs, rhs1)
        G.add_edge(lhs, rhs2)
    if "^" in rhs:
        G.add_node(lhs, expression="^")
        rhs1, rhs2 = rhs.split("^")
        rhs1 = rhs1.strip()
        rhs2 = rhs2.strip()
        G.add_node(rhs1)
        G.add_node(rhs2)
        G.add_edge(lhs, rhs1)
        G.add_edge(lhs, rhs2)
    if "~" in rhs:
        G.add_node(lhs, expression="~")
        rhs1, rhs2 = rhs.split("~")
        rhs2 = rhs2.strip()
        G.add_node(rhs2)
        G.add_edge(lhs, rhs2)

# Initialize another dictionary for required input conditions that brings controllability at the faulty node
# 'X' represents Don't Care value
input_cases = {'A': 'X', 'B': 'X', 'C': 'X', 'D': 'X'}

# Output is a list of possible input combinations
output = call(required_value, G, faulty_node, input_cases)
for every in output:
    dic.update({'A': every[0]})
    dic.update({'B': every[1]})
    dic.update({'C': every[2]})
    dic.update({'D': every[3]})
    expected = generate_good_value(lines, dic)
    actual = generate_bad_value(lines, dic, faulty_node, required_value)
    # print("expected", expected)
    # print("actual", actual)
    if expected != actual:
        vector = list(every)
        test_vectors.append(vector)
print(len(test_vectors))
print(len(output))
