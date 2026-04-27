import json

with open("../tree/reflection-tree.json") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}

def get_next(node_id):
    children = [n for n in nodes.values() if n.get("parent") == node_id]
    return children[0]["id"] if children else None

def run():
    current = "START"

    while current:
        node = nodes[current]
        print("\n" + node.get("text", ""))

        if node["type"] == "end":
            break

        elif node["type"] == "question":
            options = node["options"]
            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            choice = int(input("Choose: ")) - 1
            answer = options[choice]

            decision = [n for n in nodes.values() if n.get("parent") == current and n["type"] == "decision"][0]
            current = decision["rules"][answer]

        elif node["type"] == "reflection":
            input("Press Enter...")
            current = get_next(current)

        elif node["type"] == "bridge":
            input("Press Enter...")
            current = node["target"]

        elif node["type"] == "summary":
            input("Press Enter...")
            current = get_next(current)

        else:
            current = get_next(current)

run()
