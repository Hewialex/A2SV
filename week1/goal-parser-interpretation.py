class Solution:
    def interpret(self, command: str) -> str:
        word = ""

        for i in range(len(command)):
            if command[i] == "G":
                word += "G"
            elif command[i] == "("  and command[i+1] == "a":
                word += "al"
            elif command[i] == "("  and command[i+1] == ")":
                word += "o" 
            else:
                continue      
        return word