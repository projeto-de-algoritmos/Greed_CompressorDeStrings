class HuffmanCoding:
    def __init__(self, mesage):
        self.mesage = message
        self.heap = []
        self.codes = {}
    
    class HeapNode:
        def __init__(self, character, frequency):
            self.character = character
            self.frequency = frequency

        def __lt__(self, other):
            return self.frequency < other.frequency
        
        def __eq__(self, other):
            if(other == None):
                return False
            if(not isinstance(other, HeapNode)):
                return False
            return self.frequency == other.frequency

    def make_frequency_dict(message):
        frequency = {}
        for character in message:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency_dict):
    
    def merge_codes(self):
    
    def make_codes(self):
    
    def get_encoded_message(self, message):

    def pad_encoded_message(self, encoded_message):
    
    def get_byte_array(self, padded_encoded_message):

    def compress(self):
        message = input("Enter a message: ")
        message = text.strip()

        frequency = make_frequency_dict(message)

        self.make_heap(frequency)
        self.merge_codes()
        self.make_codes()

        encoded_message = get_encoded_message(message)
        padded_encoded_message = pad_encoded_message(encoded_message)

        byte_message = self.get_byte_array(padded_encoded_message)

        print(byte(byte_message))