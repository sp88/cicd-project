import os
import tensorflow as tf
from tensorflow import keras

# print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print(tf.__version__, tf.config.list_physical_devices())


# checkpoint_path = f"{os.getcwd()}/nlp_proj"+"/saved_model/cp-{epoch:04d}.ckpt"
# checkpoint_dir = os.path.dirname(checkpoint_path)

# print(checkpoint_dir)
# latest = tf.train.latest_checkpoint(checkpoint_dir)
# print(latest)


# loaded_model = JointIntentAndSlotFillingModel(
#     intent_num_labels=len(intent_map), slot_num_labels=len(slot_map))
# loaded_model.load_weights(latest)