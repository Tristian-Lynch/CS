# vim: set tw=79 tb=4 sw=4 et
"""Module for a generic tree used in CS302 Lab 3.

This module defines a set of functions that can help build trees from a json
file to speed up testing.

@Author: Mohammad A. Noureddine (mohammad.noureddine@indstate.edu)
@Date: Oct 23, 2024
@Credit: This lab is based on a lab developed by Professor Matthew Boutell of
    Rose-Hulman. It has been reworked by Mohammad for compatibility with Python
    and CS302 class requirements.
"""

import json
import sys
from tree import Tree
from binary_tree import BinaryTree
from binary_node import BinaryNode
from node import Node


def _construct_binary_node(item, children):
    if len(children) > 2:
        print("Malformed json file")
        sys.exit(1)

    node = BinaryNode(item)
    for i, child_info in enumerate(children):
        if i == 0:
            node.left = _construct_binary_node(child_info["data"],
                                               child_info["children"])
        if i == 1:
            node.right = _construct_binary_node(child_info["data"],
                                                child_info["children"])

    return node


def _construct_node(item, children, arity):
    node = Node(arity, item)
    for child_info in children:
        node.add_child(
            _construct_node(child_info["data"], child_info["children"])
        )
    return node


def _build_binary_tree(name: str, data: any) -> BinaryTree:
    # construct the root node
    root_info = data["nodes"][0]
    root = _construct_binary_node(root_info["data"], root_info["children"])
    return BinaryTree(name, root)


def _build_tree(name: str, data: any, arity: int) -> Tree:
    if arity == 2:
        return _build_binary_tree(name, data)

    root_info = data["nodes"][0]
    root = _construct_node(root_info["data"], root_info["children"], arity)
    return Tree(arity, name, root)


def build_tree_from_json(fname: str) -> Tree:
    """Build a tree from an input json file.

    This is a helper function for building test cases.

    Args:
        fname (str):
            The name of the file containing the tree in json format.

    Returns:
        Tree: A (Binary)Tree built from the json file.
    """
    with open(fname, 'r') as f:
        data = json.load(f)

    name = data["tree_name"]
    arity = data["arity"]

    if len(data["nodes"]) == 0:
        return Tree(arity, name)

    return _build_tree(name, data, arity)


if __name__ == "__main__":
    test_file_name = "trees/tree_h7.json"
    tree = build_tree_from_json(test_file_name)
    print(tree)

