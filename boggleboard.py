"""



  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing letters; this matrix represents a boggle board. You're
  also given a list of words.

  Write a function that returns an array of all the words contained in the
  boggle board.

  A word is constructed in the boggle board by connecting adjacent
  (horizontally, vertically, or diagonally) letters, without using any single
  letter at a given position more than once; while a word can of course have
  repeated letters, those repeated letters must come from different positions in
  the boggle board in order for the word to be contained in the board. Note that
  two or more words are allowed to overlap and use the same letters in the
  boggle board.

Sample Input
board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"],
],
words = [
  "this", "is", "not", "a", "simple", "boggle",
  "board", "test", "REPEATED", "NOTRE-PEATED",
]

Sample Output
["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]

Sample : Tree:

{
   "t":{
      "h":{
         "i":{
            "s":{
               "*":"this"
            }
         }
      },
      "e":{
         "s":{
            "t":{
               "*":"test"
            }
         }
      }
   },
   "i":{
      "s":{
         "*":"is"
      }
   },
   "n":{
      "o":{
         "t":{
            "*":"not"
         }
      }
   },
   "a":{
      "*":"a"
   },
   "s":{
      "i":{
         "m":{
            "p":{
               "l":{
                  "e":{
                     "*":"simple"
                  }
               }
            }
         }
      }
   },
   "b":{
      "o":{
         "g":{
            "g":{
               "l":{
                  "e":{
                     "*":"boggle"
                  }
               }
            }
         },
         "a":{
            "r":{
               "d":{
                  "*":"board"
               }
            }
         }
      }
   },
   "R":{
      "E":{
         "P":{
            "E":{
               "A":{
                  "T":{
                     "E":{
                        "D":{
                           "*":"REPEATED"
                        }
                     }
                  }
               }
            }
         }
      }
   },
   "N":{
      "O":{
         "T":{
            "R":{
               "E":{
                  "-":{
                     "P":{
                        "E":{
                           "A":{
                              "T":{
                                 "E":{
                                    "D":{
                                       "*":"NOTRE-PEATED"
                                    }
                                 }
                              }
                           }
                        }
                     }
                  }
               }
            }
         }
      }
   }
}


"""

def get_words_trie(words):
    words_trie = Trie()
    for word in words:
        words_trie.add(word)
    return words_trie.root

def boggle_board(board, words):

    # construction the Tries from words list:
    words_trie = get_words_trie(words)
    #word_key_found = "*"
    found_words = {}

    visited = [[False for letter in row] for row in board]

    # iterate over board
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, words_trie, visited, found_words)
    return list(found_words.keys())

def explore(i, j, board, trie_node, visited, final_words):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trie_node:
        return
    visited[i][j] = True
    trie_node = trie_node[letter]
    if "*" in trie_node:
        final_words[trie_node["*"]] = True
    neighboring_nodes = get_neigboring_indexes(i, j, board)
    for neighbor in neighboring_nodes:
        explore(neighbor[0], neighbor[1], board, trie_node, visited, final_words)
    visited[i][j] = False

def get_neigboring_indexes(i, j, board):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i - 1, j + 1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i + 1, j + 1])
    if i < len(board) - 1 and j > 0:
        neighbors.append([i + 1, j - 1])
    if i > 0:
        neighbors.append([i - 1, j])
    if i < len(board) - 1:
        neighbors.append([i + 1, j])
    if j > 0:
        neighbors.append([i, j - 1])
    if j < len(board[0]) - 1:
        neighbors.append([i, j + 1])
    return neighbors




class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word







if __name__ == '__main__':
    board = [
        ["t", "h", "i", "s", "i", "s", "a"],
        ["s", "i", "m", "p", "l", "e", "x"],
        ["b", "x", "x", "x", "x", "e", "b"],
        ["x", "o", "g", "g", "l", "x", "o"],
        ["x", "x", "x", "D", "T", "r", "a"],
        ["R", "E", "P", "E", "A", "d", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["N", "O", "T", "R", "E", "-", "P"],
        ["x", "x", "D", "E", "T", "A", "E"],
    ]

    words = [
        "this", "is", "not", "a", "simple", "boggle",
        "board", "test", "REPEATED", "NOTRE-PEATED",
    ]

    results = boggle_board(board, words)
    print(results)


