
# Import the required modules
import argparse
import os
from subprocess import call

# Function for extracting features with openSMILE (Return whether successed)
def extract_features(args):
    # Check input directory (if not exist -> error)
    if not os.path.exists(args.input_dir):
        print "Error: input directory not exist"
        return False
    for data_type in ["train", "test"]:
        path = os.path.join(args.input_dir, data_type)
        if not (os.path.exists(path)):
            print "Error: input directory missing train or test directories"
            return False
    
    # Check output directory (if not exist -> create one)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    for data_type in ["train", "test"]:
        path = os.path.join(args.output_dir, data_type)
        if not os.path.exists(path):
            os.makedirs(path)
            
    # Iterate over wav audio files in input directory
    
    
    return True
    

# Obtaining args from terminal
def get_args():
    
    parser = argparse.ArgumentParser(description='Extract features for files in the directory using openSMILE')
    
    parser.add_argument("-i",                   # optional argument (no "-" for positional)
                        "--input_dir",   # name of the attribute (dest)
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
    parser.add_argument("-l", "--label", type = str, required = True, help = "Label filename")
    args = parser.parse_args()
    
    return args

def main():
    # Obtaining terminal args
    args = get_args()
    
    # Extracting features according to args
    print(args)
    
    if not extract_features(args):
        print "Failed to extract features"
    else:
        print "Successfully extracted features"

# If running the file directly
if __name__ == "__main__":
    main()