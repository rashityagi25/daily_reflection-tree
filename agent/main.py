
import json

with open("../tree/reflection-tree.json") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}

def run():
    current = "START"

    while True:
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

            # find decision
            next_node = None
            for n in nodes.values():
                if n.get("parent") == node["id"] and n["type"] == "decision":
                    next_node = n["rules"][answer]

            current = next_node

        elif node["type"] == "decision":
            continue

        elif node["type"] in ["reflection", "bridge", "summary"]:
            input("Press Enter to continue...")
            children = [n for n in nodes.values() if n.get("parent") == node["id"]]
            if children:
                current = children[0]["id"]
            else:
                current = node.get("target")

run()
