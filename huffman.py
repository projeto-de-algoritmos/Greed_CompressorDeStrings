import heapq
class HuffmanCoding:
    def __init__(self, message):
        self.mesage = message
        self.heap = []
        self.codes = {}
        self.left = None
        self.right = None
    
    class HeapNode:
        def __init__(self, character, frequency):
            self.character = character
            self.frequency = frequency
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.frequency < other.frequency
        
        def __eq__(self, other):
            if(other == None):
                return False
            if(not isinstance(other, HeapNode)):
                return False
            return self.frequency == other.frequency

    def make_frequency_dict(self, message):
        frequency = {}
        for character in message:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency_dict):
        for key in frequency_dict:
            node = self.HeapNode(key, frequency_dict[key])
            heapq.heappush(self.heap, node)
    
    def merge_codes(self):
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.frequency + node2.frequency)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)
    
    def make_codes_helper(self, root, current_code):
        if(root == None):
            return
        
        if(root.character != None):
            self.codes[root.character] = current_code

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)
    
    def get_encoded_message(self, message):
        encoded_message = ""
        
        for character in message:
            encoded_message += self.codes[character]
        
        return encoded_message

    # def pad_encoded_message(self, encoded_message):
    
    def get_byte_array(self, encoded_message):
        b = bytearray()
        for i in range(0, len(encoded_message), 8):
            byte = encoded_message[i:i+8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        message = input("Enter a message: ")
        message = message.strip()

        frequency = self.make_frequency_dict(message)

        self.make_heap(frequency)
        self.merge_codes()
        self.make_codes()

        encoded_message = self.get_encoded_message(message)
        # padded_encoded_message = pad_encoded_message(encoded_message)

        byte_message = self.get_byte_array(encoded_message)
        #byte_message = self.get_byte_array(padded_encoded_message)

        print(encoded_message)