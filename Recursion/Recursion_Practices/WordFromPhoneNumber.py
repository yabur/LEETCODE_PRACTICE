# input = "1,2,3,4,5,6,7"
# Create a HashTable
hashTable = {
        '0': "",
        '1': "",
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
}

# Root
def getWordsFromPhoneNumber(phoneNumber):
    phoneNumber = phoneNumber.replace("0", "").replace("1", "")
    result = []
  
    if len(phoneNumber) == 0:
        return "-1"
    else:
        return result
    helper(phoneNumber, 0, [], result) 
def helper(phoneNumber, i, slate, result):
    # Base Case
    if i == len(phoneNumber) and len(slate) > 0:
            result.append("".join(slate))
    else:
        for j in hashTable[phoneNumber[i]]:
            slate.append(j)
            helper(phoneNumber, i+1, slate, result)
            slate.pop()

if __name__ == '__main__':
    input_str = "101010"
    print(getWordsFromPhoneNumber(input_str))
