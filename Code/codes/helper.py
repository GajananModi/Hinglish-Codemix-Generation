import os
import pickle


def load_data(path):
    """
    Load Dataset from File
    """
    input_file = os.path.join(path)
    with open(input_file, "r") as f:
        data = f.read()

    return data


def preprocess_and_save_data(dataset_path, token_lookup, create_lookup_tables):
    """
    Preprocess Text Data
    """
    text = load_data(dataset_path)
    
    # Ignore notice, since we don't use it for analysing the data

    token_dict = token_lookup()
    for key, token in token_dict.items():
        text = text.replace(key, ' {} '.format(token))

    text = text.lower()
    text = text.split()

    train_text = text[:int(len(text)*0.7)]
    val_text = text[int(len(text)*0.7) : int(len(text)*0.9)]
    test_text = text[int(len(text)*0.9):int(len(text))]
	
    vocab_to_int, int_to_vocab = create_lookup_tables(text)
    
    train_int_text = [vocab_to_int[word] for word in train_text]
    val_int_text = [vocab_to_int[word] for word in val_text]
    test_int_text = [vocab_to_int[word] for word in test_text]

    pickle.dump((train_int_text, val_int_text, test_int_text, vocab_to_int, int_to_vocab, token_dict), open('preprocess.p', 'wb'))
    

def load_preprocess():
    """
    Load the Preprocessed Training data and return them in batches of <batch_size> or less
    """
    return pickle.load(open('preprocess.p', mode='rb'))


def save_params(params):
    """
    Save parameters to file
    """
    pickle.dump(params, open('params.p', 'wb'))


def load_params():
    """
    Load parameters from file
    """
    return pickle.load(open('params.p', mode='rb'))

def compute_perplexity(prob, length):
    return (1/prob)**(1/float(length))
