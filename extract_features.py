
# Import the required modules
import argparse
import sys

def get_args():
    
    parser = argparse.ArgumentParser(description='Extract features for files in the directory using openSMILE')
    parser.add_argument("-i",                   # optional argument (no "-" for positional)
                        dest = "--input_dir",   # name of the attribute
                        action = "store",       # can be "store", "store_const", "store_true", etc.
                        # nargs = N for associating N args with a single action
                        # const = ... to hold constant values
                        # default = ... to set default value
                        type = str,             # check arg type
                        # choice = [.., .., ..] # restrict set of values
                        required = True,        # make an option required
                        # metavar = "XXX" for changing display name
                        help = "The directory of input audio files (wav)")
    parser.add_argument("-o", "--output_dir", type = str, required = True, help = "The directory of results")
    parser.add_argument("-c", "--config", type = str, required = True, help = "Configuration filename")
    args = parser.parse_args()
    
    return args

def main():
    args = get_args()
    print(args.input_dir)
    

# If running the file directly
if __name__ == "__main__":
    main()