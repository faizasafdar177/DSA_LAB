from collections import defaultdict

# Function to add cash flow
def add_cash_flow(graph, from_person, to_person, amount):
    graph[from_person][to_person] += amount

# Function to minimize cash flow
def minimize_cash_flow(graph):
    def get_min_index(arr):
        min_idx = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        return min_idx

    def get_max_index(arr):
        max_idx = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_idx]:
                max_idx = i
        return max_idx

    def min_cash_flow_rec(amount):
        mx_credit = get_max_index(amount)
        mx_debit = get_min_index(amount)

        if amount[mx_credit] == 0 and amount[mx_debit] == 0:
            return

        min_value = min(-amount[mx_debit], amount[mx_credit])
        amount[mx_credit] -= min_value
        amount[mx_debit] += min_value

        print(f"Person {mx_debit} pays {min_value} to Person {mx_credit}")

        min_cash_flow_rec(amount)

    amount = [0] * len(graph)
    for person in graph:
        for other_person in graph[person]:
            amount[person] -= graph[person][other_person]
            amount[other_person] += graph[person][other_person]

    min_cash_flow_rec(amount)

if __name__ == "__main__":
    n = 3  # Number of people
    graph = defaultdict(lambda: defaultdict(int))

    add_cash_flow(graph, 0, 1, 1000)
    add_cash_flow(graph, 1, 2, 5000)
    add_cash_flow(graph, 2, 0, 2000)

    print("Cash flow graph:")
    for person in graph:
        for other_person in graph[person]:
            print(f"Person {person} owes {graph[person][other_person]} to Person {other_person}")

    print("\nMinimized cash flow:")
    minimize_cash_flow(graph)
