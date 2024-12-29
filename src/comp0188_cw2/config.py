import os
from pymlrf.FileSystem import DirectoryHandler
from . import project_options

WANDB_PROJECT = "cw2_v2"

# Define ROOT_PATH based on the environment (Colab or local)
if project_options.collab:
    ROOT_PATH = "/content/drive/MyDrive/comp0188_2425/cw2"  # Path to the cw2 folder in Colab
else:
    ROOT_PATH = "../data/cw2"  # Path to the cw2 folder locally

# Ensure ROOT_PATH exists
if not os.path.exists(ROOT_PATH):
    raise Exception(f"You need to create the file path: {ROOT_PATH}")

# Define paths for train, validation, and test directories
_train_dh = DirectoryHandler(
    loc=os.path.join(ROOT_PATH, "train")
)

_val_dh = DirectoryHandler(
    loc=os.path.join(ROOT_PATH, "val")
)

_test_dh = DirectoryHandler(
    loc=os.path.join(ROOT_PATH, "test")
)

# Define paths for debug directory and its subdirectories
debug_dh = DirectoryHandler(
    loc=os.path.join(ROOT_PATH, "debug")
)

_debug_train_dh = DirectoryHandler(
    loc=os.path.join(debug_dh.loc, "train")
)

_debug_val_dh = DirectoryHandler(
    loc=os.path.join(debug_dh.loc, "val")
)

_debug_test_dh = DirectoryHandler(
    loc=os.path.join(debug_dh.loc, "test")
)

# Path for the transition_df.csv file
TRANSITION_DF_PATH = os.path.join(ROOT_PATH, "transition_df.csv")

if not os.path.exists(TRANSITION_DF_PATH):
    raise Exception(f"Transition CSV not found at: {TRANSITION_DF_PATH}")

# Use debug directories if debug mode is enabled
if project_options.debug:
    train_dh = _debug_train_dh
    val_dh = _debug_val_dh
    test_dh = _debug_test_dh
else:
    train_dh = _train_dh
    val_dh = _val_dh
    test_dh = _test_dh

# Ensure the directories are created
if not train_dh.is_created:
    train_dh.create()

if not val_dh.is_created:
    val_dh.create()

if not test_dh.is_created:
    test_dh.create()

# Helper function to list .h5 files in a directory
def get_h5_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".h5")]

# Get .h5 files for train, validation, and test
train_files = get_h5_files(train_dh.loc)
val_files = get_h5_files(val_dh.loc)
test_files = get_h5_files(test_dh.loc)

# Debugging logs (optional)
print(f"Train H5 Files: {train_files}")
print(f"Validation H5 Files: {val_files}")
print(f"Test H5 Files: {test_files}")
