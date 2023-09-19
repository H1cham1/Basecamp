Position = input("Please enter the position on the chessboard: ").upper()

White = ["A2", "A4", "A6", "A8",
         "B1", "B3", "B5", "B7",
         "C2", "C4", "C6", "C8",
         "D1", "D3", "D5", "D7",
         "E2", "E4", "E6", "E8",
         "F1", "F3", "F5", "F7",
         "G2", "G4", "G6", "G8",
         "H1", "H3", "H5", "H7"
         ]

Black = ["A1", "A3", "A5", "A7",
         "B2", "B4", "B6", "B8",
         "C1", "C3", "C5", "C7",
         "D2", "D4", "D6", "D8",
         "E1", "E3", "E5", "E7",
         "F2", "F4", "F6", "F8",
         "G1", "G3", "G5", "G7",
         "H2", "H4", "H6", "H8"
         ]

if Position in White: print("White")
elif Position in Black: print("Black")


