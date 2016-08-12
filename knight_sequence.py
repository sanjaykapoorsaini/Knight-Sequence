"""
PROBLEM:

Knight Sequences

We want to find all 10-key sequences that can be keyed into the keypad in the following manner:

The initial keypress can be any of the keys.
Each subsequent keypress must be a knight move from the previous keypress.
There can be at most 2 vowels in the sequence.
A knight move is made in one of the following ways:
1. Move two steps horizontally and one step vertically.
2. Move two steps vertically and one step horizontally.
There is no wrapping allowed on a knight move.
Below are some examples of knight moves:

OWNER- SANJAY KUMAR  

"""
              
#Identify which key identities are vowels ON THE BASIS OF INDEX
isVowel = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0] 

#For each key, list the next legal set of moves
# VaLid moves as per the keyIdentity list mentioned below..
 
validMoves =[[7,11],        #A
            [8,10,12],      #B
            [5,9,11,13],    #C
            [6,12,14],      #D
            [7,13],         #E
            [2,12,15],      #F (1) not valid for 2 moves followed by 1 move rule
            [3,13,16],      #G
            [0,4,10,14,15,17], #H
            [1,11,16],      #I 
            [2,12,17],      #J (3) not valid for 2 moves followed by 1 move rule
            [1,7,16],       #K
            [0,2,8,17],     #L
            [1,3,5,9],      #M
            [2,4,6,15],     #N
            [3,7,16],       #O
            [5,7,13],       #1
            [6,8, 10, 14],  #2 (K) & (O) not valid for 2 moves followed be 1 move rule
            [7,9,11]]       #3

       
def TraverseKeySequences(key_array, remaining_keys, vowelsAllowed):          
    """Returns Valid knight sequence path count Recursively """
     
    sequences = 0      
    if remaining_keys > 0:
        remaining_keys = remaining_keys - 1 
        # Evaluate each possible key press in the allowed key path and only include the press if
        # the vowel count restriction is not violated.                    
        for key_index in key_array: 
            value = 0                   
            if (vowelsAllowed or (not isVowel[key_index])):     
                if remaining_keys:     # continue  evaluate possible key combinations...   
                    value = TraverseKeySequences((validMoves[key_index]) , remaining_keys, vowelsAllowed - isVowel[key_index]) 
                else:                    
                    value = 1    
                     
            sequences += value
                            
    return sequences 

if __name__ == '__main__':
    """main function"""    
    
    allowableVowels = 2                                                  # Allowed vowels
    totalKeysInSequence = 10                                             # sequence length    
    
    enteredValue = str(raw_input('Please enter Max key sequences.. (This is optional by default sequence length is 10).. Please Press Enter :) '))
    if enteredValue:
        if 11 > int(enteredValue) > 0 :
            totalKeysInSequence = int(enteredValue)
        else:
            print ("Entered Value is not in range So "  )
         
    # First the key identity which makes the rest of the code easier to read.
    keyIdentity = [ {'A':0}, {'B':1}, {'C':2}, {'D':3}, {'E':4}, {'F':5}, {'G':6}, {'H':7}, {'I':8}, {'J':9}, {'K':10}, {'L':11}, {'M':12}, {'N':13}, {'O':14}, {'1':15}, {'2':16}, {'3' :17}]
    
    print ("Total number of valid "+str(totalKeysInSequence)+ " key sequences are: " + str(TraverseKeySequences(xrange(len(keyIdentity)), totalKeysInSequence, allowableVowels)))  
        
