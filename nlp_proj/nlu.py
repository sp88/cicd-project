import tensorflow as tf


def nlu(text, tokenizer, model, intent_names, slot_names):
    inputs = tf.constant(tokenizer.encode(text))[None, :]  # batch_size = 1
    outputs = model(inputs)
    slot_logits, intent_logits = outputs

    slot_ids = slot_logits.numpy().argmax(axis=-1)[0, :]
    intent_id = intent_logits.numpy().argmax(axis=-1)[0]

    info = {"intent": intent_names[intent_id], "slots": {}}

    out_dict = {}
    # get all slot names and add to out_dict as keys
    predicted_slots = set([slot_names[s] for s in slot_ids if s != 0])
    for ps in predicted_slots:
      out_dict[ps] = []

    tokens = tokenizer.tokenize(text, add_special_tokens=True)

    # check if the text starts with a small letter
    # if text[0].islower():
    #   tokens = tokenizer.tokenize(text, add_special_tokens=True)
    # else:
    #   tokens = tokenizer.tokenize(text)
    for token, slot_id in zip(tokens, slot_ids):
        # add all to out_dict
        slot_name = slot_names[slot_id]

        if slot_name == "<PAD>":
            continue

        # collect tokens
        collected_tokens = [token]
        idx = tokens.index(token)

        # see if it starts with ##
        # then it belongs to the previous token
        if token.startswith("##"):
          # check if the token already exists or not
          if tokens[idx - 1] not in out_dict[slot_name]:
            collected_tokens.insert(0, tokens[idx - 1])

        # add collected tokens to slots
        out_dict[slot_name].extend(collected_tokens)

    # process out_dict
    for slot_name in out_dict:
        tokens = out_dict[slot_name]
        slot_value = tokenizer.convert_tokens_to_string(tokens)

        info["slots"][slot_name] = slot_value.strip()

    return info
