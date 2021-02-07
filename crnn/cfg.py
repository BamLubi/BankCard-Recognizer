# Preprocess
AUG_NBR = 80

SRC_IN_DIR = "../dataset/card_nbr/imgs"
AUG_OUT_DIR = "../dataset/card_nbr/augs"

TRAIN_TXT_PATH = "../dataset/card_nbr/train.txt"
VAL_TXT_PATH = "../dataset/card_nbr/val.txt"

# Training
NUM_CLASSES = len("0123456789_") + 1  # plus one for blank in CTC loss
MAX_LABEL_LENGTH = 26
DOWNSAMPLE_FACTOR = 4
VALIDATION_RATIO = 0.2

MODEL_OUT_DIR = "model/"
IMG_SIZE = (256, 32)
BATCH_SIZE = 32
EPOCH = 20

# CODE
DECODE_DICT = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '_'}
ENCODE_DICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '_': 10}
