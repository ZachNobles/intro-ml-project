from pathlib import Path
import time
import json
import ast
import os


def count_functions(tree):
    return sum(
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        for node in ast.walk(tree)
    )

def count_conditionals(tree):
    return sum(isinstance(node, ast.If) for node in ast.walk(tree))

def count_variables(tree):
    assigned = {
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)
    }
    parameters = {
        node.arg
        for node in ast.walk(tree)
        if isinstance(node, ast.arg)
    }
    return len(assigned | parameters)

def count_nonempty_lines(source):
    return sum(1 for line in source.splitlines() if line.strip())

def count_print_statements(tree):
    return sum(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "print"
        for node in ast.walk(tree)
    )

def analyze_loops(tree):
    loop_count = 0
    max_depth = 0

    def visit(node, current_depth=0):
        nonlocal loop_count, max_depth

        if isinstance(node, (ast.For, ast.AsyncFor, ast.While)):
            loop_count += 1
            current_depth += 1
            max_depth = max(max_depth, current_depth)

        for child in ast.iter_child_nodes(node):
            visit(child, current_depth)

    visit(tree)

    return loop_count, max_depth

def analyze_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        source = file.read()

    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as error:
        print(f"Syntax error: {error}")
        return

    input_type_index = source.find("# input type:")
    input_type = source[input_type_index+14:source.find("\n", input_type_index)] if input_type_index != -1 else None

    loop_count, max_depth = analyze_loops(tree)
    function_count = count_functions(tree)
    conditional_count = count_conditionals(tree)
    variable_count = count_variables(tree)
    nonempty_line_count = count_nonempty_lines(source)
    print_count = count_print_statements(tree)

    return input_type, {
        "loop_count": loop_count,
        "max_depth": max_depth,
        "function_count": function_count,
        "conditional_count": conditional_count,
        "variable_count": variable_count,
        "nonempty_line_count": nonempty_line_count,
        "print_count": print_count
    }


def main(dataset_path):
    start_time = time.time()
    script_dir = Path(__file__).resolve().parent
    dataset_dir = Path(dataset_path)
    dataset_dir = script_dir / dataset_dir
    dataset_dir = dataset_dir.resolve()

    index = dict()
    count = 0
    for root, _, files in os.walk(dataset_dir):
        for file in files:
            if file.endswith(".py"):
                count += 1
                print(f"\rAnalyzing file: {file}",end=" ")
                input_type, data = analyze_file(Path(root) / file)
                print(f"| input type: {input_type}, loop count: {data['loop_count']}, function count: {data['function_count']}...", end="")
                index[str(file)] = {"input_type": input_type, "data": data}
    print(f"\nAnalyzed {count} files in {time.time() - start_time:.2f} seconds.")

    output_file = script_dir / "index.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)


if __name__ == "__main__":
    dataset_path = "dataset"
    main(dataset_path)