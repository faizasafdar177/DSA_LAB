from collections import Counter, heapq
from typing import Dict, List, Tuple

class Node:
    def __init__(self, char: str = "", freq: int = 0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text: str) -> Node:
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node("", left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def encode_huffman_tree(root: Node) -> Dict[str, str]:
    def _encode(node: Node, path: str):
        if not node:
            return
        if node.char:
            huffman_code[node.char] = path
        _encode(node.left, path + "0")
        _encode(node.right, path + "1")

    huffman_code = {}
    _encode(root, "")
    return huffman_code

def huffman_encode(text: str, huffman_code: Dict[str, str]) -> str:
    return "".join(huffman_code[char] for char in text)

def huffman_decode(encoded_text: str, root: Node) -> str:
    decoded_text = ""
    node = root
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char:
            decoded_text += node.char
            node = root
    return decoded_text

if __name__ == "__main__":
    text = "huffman coding example"
    root = build_huffman_tree(text)
    huffman_code = encode_huffman_tree(root)
    
    print("Character Huffman Codes:")
    for char, code in huffman_code.items():
        print(f"{char}: {code}")

    encoded_text = huffman_encode(text, huffman_code)
    print("\nEncoded Text:", encoded_text)

    decoded_text = huffman_decode(encoded_text, root)
    print("\nDecoded Text:", decoded_text)
