# vigenereSolver

## Simple solver
This is a simple vigenere solver.<br>
More it was a possibility for me to play a little with python. <br>
It only checks for letters of the alphabet and don't affect special characters <br>
If you can need it feel free to download, adapt, change ... go nuts :)

## Usage
### Use this type to decode a text from a file with a specific key
python3 vigenereSolver.py <path_to_encoded_file> <key_as_string>

### Use this type to brute-force key with a length from 1-7 
If the decoded text contains " the ", " for ", " is ", " are " <a style="color:#00F">and</a> " to " it prints the possible key
python3 vigenereSolver.py <path_to_encoded_file>
